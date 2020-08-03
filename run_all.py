import os,sys
import unittest,time

from config import setting
from common.sendMail import send_mail
from common.newReport import new_report
from package.HTMLTestRunner import HTMLTestRunner

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def add_case(test_path=setting.TEST_CASE):
    """
    加载所有测试用例
    @param test_path:测试用例
    @return:TestSuite
    """
    discover = unittest.defaultTestLoader.discover(test_path,pattern="*API.py")
    return discover

def run_case(all_case,result_path=setting.TEST_REPOST):
    """
    执行所有测试用例
    @param all_case:
    @param result_path:
    @return:None
    """
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = result_path+"/"+now+"result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title = "XXX接口自动化测试报告")
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPOST)  # 调用模块生成最新的报告
    send_mail(report)

if __name__ == '__main__':
    cases = add_case()
    run_case(cases)