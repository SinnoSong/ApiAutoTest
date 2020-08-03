import os,sys

#获取文件目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

#配置文件的文件地址
TEST_CONFIG = os.path.join(BASE_DIR,"data","config.ini")
#测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,"data","APITestCase.xlsx")
#测试用例执行结果excel
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","APITestCaseResult.xlsx")
#测试用例报告html
TEST_REPOST = os.path.join(BASE_DIR,"report")
#测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testcase")
