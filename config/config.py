# _*_ coding:utf-8 _*_
import logging
import os


# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前文件的绝对路径的上一级，__file__指当前文件

data_path = os.path.join(prj_path,'data') # 数据目录
test_path = os.path.join(prj_path,'test') # 用例目录，暂时在项目目录下

log_file = os.path.join(prj_path,'log','log.txt')
report_path = os.path.join(prj_path,'report','report.html')

logger = logging.getLogger()  # 实例化一个logger对象
logger.setLevel(logging.DEBUG)  # 设置初始显示级别


# log配置
# 创建一个文件句柄
file_handle = logging.FileHandler("C:/Users/xuhong/PycharmProjects/untitled/insight_test/log/log.txt",encoding="UTF-8",mode='a')

# 创建一个输出格式
fmt = logging.Formatter('[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
                        )

file_handle.setFormatter(fmt) # 文件句柄设置格式

logger.addHandler(file_handle) # logger对象绑定文件句柄


# file = open("../../log/log.txt",encoding='utf-8',mode='a')
# logging.basicConfig(level=logging.DEBUG,
#                     stream=file,
#                     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S'
#                     )

# file.close()

# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = '123456'
db = 'insight_db'

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '136214170@qq.com'
smtp_password = 'muwrlrgsnpdabhfb'

sender = smtp_user # 发件人
receiver = 'xuhong-sj@bestpay.com.cn' # 收件人
subject ='接口测试报告' # 邮件主题

if __name__ == '__main__':
    logging.info('hello')

