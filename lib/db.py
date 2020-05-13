# _*_ coding:utf-8 _*_
import pymysql
from insight_test.config.config import *



# 获取链接方法
def get_db_conn():
    conn = pymysql.connect(host =db_host,
                           port=db_host,
                           user=db_user,
                           passwd=db_passwd,
                           db = db,
                           charset ='utf8')
    return conn

# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn() # 获取连接
    cur = conn.cursor() # 建立游标
    logging.debug(sql) # 输出执行的sql
    cur.execute((sql)) # 执行sql
    conn.commit()
    result = cur.fetchall() # 获取所有查询结果
    logging.debug(result) # 输出查询结果
    cur.close() # 关闭游标
    conn.close() # 关闭连接
    return result # 返回结果

# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql) # 输出执行的sql
    try:
        cur.execute(sql)
        conn.commit() # 提交更改
    except Exception as e:
        conn.rollback() # 回滚
        logging.error(str(e)) # 输出错误信息
    finally:
        cur.close()
        conn.close()

# 封装常用数据库操作
def check_user(name):
    sql = "select * from user where name ='{}'".format(name)
    result = query_db(sql)
    logging.debug(result)
    return True if result else False

def add_user(name,password):
    sql = "insert into user (name,passwd) values ('{}','{}')".format(name,password)
    logging.debug(sql)
    change_db(sql)

def del_user(name):
    sql = "delete from user where name ='{}'".format(name)
    logging.debug(sql)
    change_db(sql)

