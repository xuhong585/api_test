# coding:utf-8
import yaml
import os


cur = os.path.dirname(os.path.realpath(__file__))
def get_token(yamlName="token.yaml"):

    p = os.path.join(cur,"token.yaml")
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t['token']

def get_bfileId(yamlName="token.yaml"):
    p = os.path.join(cur, "token.yaml")
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t['bfileId']






if __name__=='__main__':
    print(get_token())