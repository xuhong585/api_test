import unittest
from insight_test.test.fileupload import FileUpload
from insight_test.test.crowd_save import CrowdSave
from insight_test.lib.HTMLTestReportCN import HTMLTestRunner
from insight_test.config.config import *
from insight_test.lib.send_email import send_email
from insight_test.lib.login_token import *


logging.info("====================== 测试开始 =======================")

write_token(login_token())

suite = unittest.TestSuite()
suite.addTests([FileUpload('test_01')])
suite.addTests([CrowdSave('test_crowd_save_normal'),CrowdSave('test_crowd_save_repeat'),CrowdSave('test_crowd_save_name_empty')])


# with open("C:/Users/xuhong/PycharmProjects/untitled/insight_test/report/report.html",'wb') as f:
#     HTMLTestRunner(stream=f,title="Api Test",description="测试描述",tester='11').run(suite)

f = open("C:/Users/xuhong/PycharmProjects/untitled/insight_test/report/report.html", 'wb')
HTMLTestRunner(stream=f,title="Api Test",description="测试描述",tester='11').run(suite)
f.close()

send_email('C:/Users/xuhong/PycharmProjects/untitled/insight_test/report/report.html')  # 发送邮件
logging.info("======================= 测试结束 =======================")