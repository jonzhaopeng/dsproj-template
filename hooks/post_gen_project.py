"""
配置项目下数据项目venv环境
"""

import os
import sys
import subprocess


subprocess.check_call(
    [sys.executable, '-m', 'venv', '--system-site-packages', '.venv'])

os.system('source .venv/bin/activate')

subprocess.check_call(
    [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
