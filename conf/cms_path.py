'''
ui自动化po设计模式
此模块是配置项目的路径和每个包的绝对路径，为我们后面引用路径提供基础
'''
#涉及到路径需要导入os模块
import os
#定义项目的路径
base_path = os.path.dirname(os.path.dirname(__file__))   #获取当前运行脚本的绝对路径（去掉最后一个路径）
#定义data的路径
data_path = os.path.join(base_path,"data")
#pages路径
pages_path = os.path.join(base_path,"public","pages")
#utiles路径
utiles_path = os.path.join(base_path,"public","utiles")
#report路径
report_path = os.path.join(base_path,"report")
#testcase路径
testcase_path = os.path.join(base_path,"testcase")

