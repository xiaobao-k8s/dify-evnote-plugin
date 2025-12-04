import sys
import os

# 添加tools目录到Python路径以便导入工具模块
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))

# 导入通用路径设置模块
from tools import setup_path

from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class EvnoteProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            from tools.note import EvernoteManager

            auth_token = credentials["auth_token"]
            sandbox = credentials["sandbox"]
            china = credentials["china"]

            evernote_manager = EvernoteManager(auth_token, sandbox, china)
            
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
