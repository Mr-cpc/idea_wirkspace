import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from basic.bupt_2017_11_24.login import Login

lg = Login()
lg.login()