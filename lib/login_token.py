import requests
import json
import os
import yaml



# 获取token的方法
def login_token():
    login_url = 'http://172.17.39.130:8030/login/login'
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    data = {"username": "WE7xWB6FI2b3G3J0pstkaQ==", "password": "UgRse2+QEJ7Jzq55f9O6oQ==", "env": "NEWTEST"}
    res = requests.post(url=login_url, data=json.dumps(data), headers=headers)
    print(res.json())
    token = res.json()["data"]["token"]

    ipconfigs_url = 'http://172.17.39.130:8030/login/ipConfigs'
    headers = {"Referer": "http://172.17.39.130:8030/static/dist/index.html?env=NEWTEST&sysType=insight",
               "token": token}
    res = requests.post(url=ipconfigs_url, headers=headers)

    sms_url = 'http://172.17.39.130:8030/login/directSmsLogin'
    headers = {"Content-Type": "application/json;charset=UTF-8",
               "Referer": "http://172.17.39.130:8030/static/dist/index.html?env=NEWTEST&sysType=insight",
               "token": token}
    data = {"webloginmessageCode": "123456", "sysType": "INSIGHT", "env": "NEWTEST",
            "url": "http://172.17.39.19:8030/webpage/dist/index.html", "username": "WE7xWB6FI2b3G3J0pstkaQ=="}
    res = requests.post(url=sms_url, data=json.dumps(data), headers=headers)

    return token


def write_token(value):
    curpath= os.path.dirname(os.path.realpath(__file__))
    ypath = os.path.join(curpath,'token.yaml')
    print(ypath)
    t = {"token":value}
    with open(ypath,'w',encoding='utf-8') as f:
        yaml.dump(t,f)


if __name__=='__main__':
    write_token(login_token())

