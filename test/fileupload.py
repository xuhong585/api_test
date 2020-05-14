# _*_ coding:utf-8 _*_
import unittest
import json
import requests
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)).split('insight_test')[0])
from insight_test.lib.read_excel import *
from insight_test.config.config import *
from insight_test.lib.case_log import log_case_info
from insight_test.lib.get_token import *
from requests.packages import urllib3
urllib3.disable_warnings()


class FileUpload(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.token = get_token()
        print(cls.token)
        logging.info(cls.token)
        cls.data_list = excel_to_list('C:/Users/xuhong/PycharmProjects/untitled/insight_test/data/test_user_data.xlsx', 'FileUpload') # 读取该测试类所有用例数据
        # cls.data_list 同 self.data_list 都是该类的公共属性


    def test_01(self):
        case_data = get_test_data(self.data_list,'test_01')
        if not case_data:
            logging.error('用例数据不存在')
        url = case_data.get('url')
        params = json.loads(case_data.get('params'))
        headers ={"token":self.token}
        # file =json.loads(case_data.get('data'))
        file = {'name': open(r'C:\Users\xuhong\Desktop\sdcc.txt','rb'),'Content-Disposition':'form-data',
        'Content-Type':'text/plain','filename':'sdcc.txt'}
        expect_res = case_data.get('expect_res')
        # res = requests.post(url=url,params=params,headers=headers,files=file)
        res = requests.post(url=url,headers=headers,params=params,files=file)
        print(res.json())
        self.assertIn(res.json()['resMsg'],expect_res)
        bfileId = res.json()['obj']['bfileId']
        ypath = r'C:\Users\xuhong\PycharmProjects\untitled\insight_test\lib\token.yaml'
        print(ypath)
        t = {"bfileId": 'aaa'}
        with open(ypath, 'a', encoding='utf-8') as f:
            yaml.dump(t, f)


if __name__ == '__main__':
    unittest.main(verbosity=2)


