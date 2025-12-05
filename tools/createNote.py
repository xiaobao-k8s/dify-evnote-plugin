# 导入已经设置好路径的tools模块
from tools import setup_path

from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.note import EvernoteManager

class createNote(Tool):
    def __init__(self, runtime, session):
        super().__init__(runtime, session)
        auth_token = runtime.credentials["auth_token"]
        sandbox = runtime.credentials["sandbox"]
        china = True  # 固定使用国内网站(app.yinxiang.com)
        self.evernoteManager = EvernoteManager(auth_token, sandbox, china)
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        执行创建笔记的操作，根据传入的参数调用 EvernoteManager 来创建笔记，并返回创建结果。

        :param tool_parameters: 包含创建笔记所需参数的字典，应包含 'title'、'content' 和 'book_name' 键。
        :return: 生成器，生成 ToolInvokeMessage 类型的消息，包含创建结果或错误信息。
        """
        # 从传入的参数中提取笔记标题
        title = tool_parameters["title"]
        content = tool_parameters["content"]
        book_name = tool_parameters["book_name"]
        try:
            createNote = self.evernoteManager.createNote(title, content, book_name)
        except Exception as e:
            yield self.create_json_message({"error": str(e)})
            return

        result = {
            "guid": createNote.guid,
        }

        yield self.create_json_message(result)
