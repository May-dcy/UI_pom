import os
from conf.cms_path import *
from configparser import ConfigParser

class Read_Ini(ConfigParser):   #定义了一个类，继承了ConfigParser类里面的方法和属性

    def __init__(self,filename):
        super(Read_Ini,self).__init__()  #继承了父类的构造方法
        self.read(filename)      #读取ini文件

    def read_data_ini(self,section=None, option=None):
        '''
        封装一个获取section对应的option里面的value值
        :return:
        '''
        value = self.get(section,option)   #通对应的option拿到value值
        return value
file = os.path.join(data_path,"data.ini")
read = Read_Ini(file)


# url = read.read_data_ini("test_data","url")
# print(url)
