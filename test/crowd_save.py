# _*_ coding:utf-8 _*_
import unittest
import requests
import json
import sys
sys.path.append('..')
from insight_test.lib.case_log import log_case_info
from insight_test.lib.read_excel import *
from insight_test.config.config import *
from insight_test.lib.get_token import *
from requests.packages import urllib3

urllib3.disable_warnings()


class CrowdSave(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()
        logging.info(cls.token)
        cls.bfileId = get_bfileId()
        print(cls.bfileId)
        cls.data_list = excel_to_list("/insight_test/data/test_user_data.xlsx", "CrowdSave")

    def test_crowd_save_normal(self):
        case_data = get_test_data(self.data_list, 'crowd_save_normal')
        if not case_data:
            logging.error('用例数据不存在')
        url = case_data.get('url')
        data = {"crowdId": "",
            "name": "测试64",
            "org": "20005",
            "business": "1",
            "bfileId": self.bfileId,
            "province": "310000",
            "dataType": "userid",
            "createdType": "file"}
        headers = {"token": self.token,"Content-Type":"application/json;charset=utf-8"}
        # headers = {"Content-Type": "application/json;charset=utf-8"}
        expect_res = case_data.get('expect_res')
        res = requests.post(url=url,headers=headers,data=json.dumps(data))
        print(res.text)
        log_case_info('crowd_save_normal', url, data, expect_res, res.text)
        self.assertIn(res.json()["resMsg"],expect_res)
        crowdId = res.json()['obj']['crowdId']
        ypath = r'C:\Users\xuhong\PycharmProjects\untitled\insight_test\lib\token.yaml'
        print(ypath)
        t = {"crowdId": crowdId}
        with open(ypath, 'a', encoding='utf-8') as f:
            yaml.dump(t, f)

    def test_crowd_save_repeat(self):
        case_data = get_test_data(self.data_list,'crowd_save_repeat')
        if not case_data:
            logging.error('用例数据不存在')
        url = case_data.get('url')
        data = {"crowdId": "",
            "name": "测试59",
            "org": "20005",
            "business": "1",
            "bfileId": self.bfileId,
            "province": "310000",
            "dataType": "userid",
            "createdType": "file"}
        headers = {"token": self.token,"Content-Type":"application/json;charset=utf-8"}
        # headers = {"Content-Type": "application/json;charset=utf-8"}
        expect_res = case_data.get('expect_res')
        res = requests.post(url=url,headers=headers,data=json.dumps(data))
        log_case_info('crowd_save_repeat', url, data, expect_res, res.text)
        print(res.text)
        self.assertIn(res.json()["resMsg"],expect_res)

    def test_crowd_save_name_empty(self):
        case_data = get_test_data(self.data_list, 'crowd_save_name_empty')
        if not case_data:
            logging.error('用例数据不存在')
        url = case_data.get('url')
        data = {"crowdId": "",
                "name": "",
                "org": "20005",
                "business": "1",
                "bfileId": self.bfileId,
                "province": "310000",
                "dataType": "userid",
                "createdType": "file"}
        headers = {"token": self.token, "Content-Type": "application/json;charset=utf-8"}
        # headers = {"Content-Type": "application/json;charset=utf-8"}
        expect_res = case_data.get('expect_res')
        res = requests.post(url=url, headers=headers, data=json.dumps(data))
        log_case_info('crowd_save_repeat', url, data, expect_res, res.text)
        print(res.text)
        self.assertIn(res.json()["resMsg"], expect_res)




if __name__ == '__main__':  # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)  # 运行所有用例
