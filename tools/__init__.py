import sys
import os

# 设置项目路径，确保能正确导入本地库
def setup_path():
    """
    设置Python路径，添加tools/lib目录到搜索路径，以便能够导入本地的evernote库。
    这个函数应该在所有需要使用本地evernote库的模块开始时调用。
    """
    # 获取当前文件的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 添加lib目录到Python路径
    lib_path = os.path.join(base_dir, 'lib')
    if lib_path not in sys.path:
        sys.path.append(lib_path)

# 自动执行路径设置
setup_path()