import os,sys
import unittest,requests,ddt

from config import setting
from common.readExcel import ReadExcel
from common.sendRequests import SendRequests
from common.writeExcel import writeExcel
import common.log

log = common.log.logger
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

test_data = ReadExcel(setting.SOURCE_FILE,"Sheet1").read_data()

@ddt.ddt
class Test_API(unittest.TestCase):
    #执行测试用例前的fixture
    def setUp(self):
        self.session = requests.session()

    # 执行测试用例后的fixture
    def tearDown(self):
        pass

    @ddt.data(*test_data)
    def test_api(self,data):
        rowNum = int(data["ID"].split("_")[2])
        log.info("执行测试用例：%s","正在执行用例->{0}".format(data["ID"]))
        log.info("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        log.info("请求参数: {0}".format(data['params']))
        log.info("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        #发送请求
        re = SendRequests().sendRequests(self.session,data)
        #获取返回值
        self.result = re.json()
        log.info("页面返回信息：%s "% re.content.decode("utf-8"))
        # 请求状态码
        result_status_code = re.status_code
        #获取excel表格数据的状态码、相应状态码和消息
        readstatus_code = int(data["status_code"])
        read_code = int(data["code"])
        readData_msg = data["msg"]
        if readstatus_code == result_status_code and read_code == self.result["code"] and readData_msg == self.result["msg"]:
            OK_data = "PASS"
            log.info("用例测试结果：{0}---->{1}".format(data["ID"],OK_data))
            writeExcel(setting.TARGET_FILE).write_data(rowNum+1,OK_data)
        if readstatus_code != result_status_code or read_code != self.result["code"] or readData_msg != self.result["msg"]:
            NOT_data = "FAIL"
            log.info("用例测试结果：{0}---->{1}".format(data["ID"],NOT_data))
            writeExcel(setting.TARGET_FILE).write_data(rowNum + 1,NOT_data)
        self.assertEqual(result_status_code,readstatus_code,"返回实际结果是->:%s " % result_status_code)
        self.assertEqual(self.result["code"],read_code,"返回实际结果是->:%s "% read_code)
        self.assertEqual(self.result["msg"],readData_msg,"返回实际结果是->:%s "% self.result["msg"])

if __name__ == '__main__':
    unittest.main()