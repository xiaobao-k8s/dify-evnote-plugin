# 导入已经设置好路径的tools模块
from tools import setup_path

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

class EvernoteManager:
    def __init__(self, auth_token, sandbox=True, china=True):
        self.auth_token = auth_token
        self.sandbox = sandbox
        self.china = china
        self.client = EvernoteClient(token=self.auth_token, sandbox=self.sandbox, china=self.china)
        self.user_store = self.client.get_user_store()
        self.check_version()
        self.note_store = self.client.get_note_store()

    def check_version(self):
        """
        检查Evernote API版本是否兼容。
        如果版本不兼容，将抛出异常。
        """
        try:
            version_ok = self.user_store.checkVersion(
                "Evernote EDAMTest (Python)",
                UserStoreConstants.EDAM_VERSION_MAJOR,
                UserStoreConstants.EDAM_VERSION_MINOR
            )
            if not version_ok:
                raise RuntimeError("Evernote API版本不兼容")
        except Exception as e:
            raise RuntimeError(f"检查API版本失败: {str(e)}") from e

    def listNotebooks(self):
        """
        获取笔记本列表，若列表已缓存则直接返回，否则从印象笔记服务获取并缓存。

        :return: 包含笔记本信息的字典，键为 'notes'，值为笔记本信息字典列表。
        """
        # 检查对象是否已经有缓存的笔记本列表
        if hasattr(self, 'notebook_list'):
            return {"notes": self.notebook_list}
        
        try:
            notebooks = self.note_store.listNotebooks()
        except Exception as e:
            raise RuntimeError(f"获取笔记本列表失败: {str(e)}") from e

        # 将 Notebook 对象转换为字典列表
        self.notebook_list = []
        if notebooks:
            for notebook in notebooks:
                notebook_dict = {
                    'guid': notebook.guid,
                    'name': notebook.name,
                    'defaultBook': notebook.defaultNotebook,
                    # 可根据需要添加更多字段
                }
                self.notebook_list.append(notebook_dict)
        return {"notes": self.notebook_list}

    def getNotebookGuid(self, book_name: str) -> str | None:
        """
        根据笔记本名称获取对应的笔记本 GUID。

        :param book_name: 要查找的笔记本名称。
        :return: 匹配的笔记本 GUID，如果未找到则返回 None。
        """
        if not book_name:
            return None
            
        notebook_data = self.listNotebooks()
        # 从返回结果中安全获取笔记本列表
        notebooks = notebook_data.get('notes', [])
        for notebook in notebooks:
            if notebook.get('name') == book_name:
                return notebook.get('guid')
        return None

    def createNote(self, title: str, content: str, note_book_name= None) -> Types.Note:
        """
        在指定笔记本或默认笔记本中创建新笔记。

        :param title: 笔记的标题。
        :param content: 笔记的内容。
        :param note_book_name: 可选参数，指定笔记本的名称。若未提供，则使用默认笔记本。
        :return: 创建好的笔记对象。
        """
        # 参数验证
        if not title:
            raise ValueError("笔记标题不能为空")
            
        if not content:
            raise ValueError("笔记内容不能为空")

        note = Types.Note()
        note.title = title

        if note_book_name:
            notebook_guid = self.getNotebookGuid(note_book_name)
            if not notebook_guid:
                raise ValueError(f"未找到名为 {note_book_name} 的笔记本")
            note.notebookGuid = notebook_guid

        # 构建符合 ENML 标准的笔记内容
        note.content = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
            f'<en-note>{content}</en-note>'
        )

        try:
            created_note = self.note_store.createNote(note)
            return created_note
        except Exception as e:
            raise RuntimeError(f"创建笔记失败: {str(e)}") from e