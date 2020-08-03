import xlrd as xr
from config import setting

class ReadExcel():
    """读取excel文件数据"""
    def __init__(self,file_name,Sheetname="Sheet1"):
        self.data = xr.open_workbook(file_name)
        self.table = self.data.sheet_by_name(Sheetname)

        #获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def read_data(self):
        """
        读取模板excel
        @return:
        """
        if self.nrows>1:
            #获取第一行的内容、列表格式
            keys = self.table.row_values(0)
            listApiData = []
            #每一行的内容、列表格式
            for col in  range(1,self.nrows):
                values = self.table.row_values(col)
                #key,values 转换为字典
                api_dict = dict(zip(keys,values))
                listApiData.append(api_dict)
            #最后返回的是list中包含字典
            return listApiData
        else:
            print("表格是空的！")
            return None