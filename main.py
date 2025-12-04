import sys
import os

# 获取当前文件的绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))
# 添加tools/lib目录到Python路径，以便能够导入本地的evernote库
sys_path_to_add = os.path.join(base_dir, 'tools', 'lib')
sys.path.append(sys_path_to_add)

from dify_plugin import Plugin, DifyPluginEnv

plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=120))

if __name__ == '__main__':
    plugin.run()
