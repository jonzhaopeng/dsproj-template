
"""
完成数据项目工作环境的初始化
"""
import os
import sys
import subprocess

subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'spyder'])

if os.name != 'nt':
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'autoenv'])
    #  判断当前shell 类型
    if environ['SHELL'] == '/bin/zsh'
        os.system("""echo "source `which activate.sh`" >> ~/.zshrc""")
    if environ['SHELL'] == '/bin/bash'
        os.system("""echo "source `which activate.sh`" >> ~/.bashrc""")
