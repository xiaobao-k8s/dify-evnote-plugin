# 导入已经设置好路径的tools模块
from tools import setup_path

from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.note import EvernoteManager

class listNotebooks(Tool):
    def __init__(self, runtime, session):
        super().__init__(runtime, session)
        auth_token = runtime.credentials["auth_token"]
        sandbox = runtime.credentials["sandbox"]
        china = runtime.credentials["china"]
        self.evernoteManager = EvernoteManager(auth_token, sandbox, china)
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        执行列出笔记本的操作，调用 EvernoteManager 实例的 listNotebooks 方法获取笔记本列表，
        并将结果以 JSON 消息的形式通过生成器返回。

        :param tool_parameters: 包含工具调用所需参数的字典，当前方法未使用该参数。
        :return: 一个生成器，生成 ToolInvokeMessage 类型的消息，包含笔记本列表信息。
        """
        # 调用 EvernoteManager 实例的 listNotebooks 方法获取笔记本列表，
        # 并使用 create_json_message 方法将结果封装为 JSON 消息，
        # 最后通过生成器返回该消息
        yield self.create_json_message(self.evernoteManager.listNotebooks())
