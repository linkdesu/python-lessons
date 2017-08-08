# -*- coding: utf-8 -*-
"""
    1_module
"""

# 导入内置模块
import sys, os

# 导入内置模块并赋予别名
import sys as system

# 只导入内置模块的部分功能
from os import walk, remove

# 导入自定义模块，并使用相对导入 https://www.python.org/dev/peps/pep-0328/
from . import mymodule
from .root_module import a_func, b_func

# 两个容易遇到的问题：
# 循环导入，a 导入了 b ，b 也导入了 a
# 覆盖导入，自定义模块使用了诸如 sys、os、math 等内置模块名