import sys
import os

# 添加tools/lib目录到Python路径，以便能够导入本地的evernote库
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools', 'lib'))

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

from tools.note import EvernoteManager

# 使用示例
if __name__ == "__main__":
    auth_token = "S=s1:U=6c1:E=1982fcd1282:C=1980bc08c68:P=1cd:A=en-devtoken:V=2:H=be4ed29dd7f171b47e32a185ce2bd5f4"
    if auth_token == "your developer token":
        print("Please fill in your developer token")
        print("To get a developer token, visit " \
              "https://sandbox.evernote.com/api/DeveloperToken.action")
        exit(1)

    evernote_manager = EvernoteManager(auth_token)
    #notebooks = evernote_manager.listNotebooks()
    
    print(f"evernote_manager: {evernote_manager}")