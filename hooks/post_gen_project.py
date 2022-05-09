import os

venv_pipeline = f"""
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip3 install -r requirements.txt
"""

# 配置项目下数据项目虚拟环境
os.system(venv_pipeline)
