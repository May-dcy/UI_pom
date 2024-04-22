'''
此模块是用来读取excel表格的工具类
读取exce表格需要用到xlrd模块
dos窗口输入：pip install xlrd
'''
import xlrd
from conf.cms_path import *
import os
class Read_Excel(object):

    def __init__(self,filename,sheet_Name):
        #先打开一个excel表格
        self.workbook=xlrd.open_workbook(filename)
        #进入到sheet页面
        self.sheetName=self.workbook.sheet_by_name(sheet_Name)

    def get_excel_data(self,row,col):
        '''
        封装了一个通过行和列来获取excel表格里面数据的工具方法
        '''
        value = self.sheetName.cell(row,col).value
        return value
file = os.path.join(data_path,"data.xls")   #把data的路径和data.xls文件名进行拼接
excel = Read_Excel(file,"Sheet1")
url = excel.get_excel_data(1,0)  #根据索引去取第二行第一列的url地址
print(url)