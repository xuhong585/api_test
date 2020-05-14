import smtplib # 用于建立smtp连接
import sys
sys.path.append('..')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # 邮件需要专门的MIME格式
from insight_test.config.config import *

def send_email(report_file):



    msg = MIMEMultipart() # 混合MIME格式
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8')) # 添加html格式邮件正文（会丢失css格式）


    # 2. 组装Email头（发件人，收件人，主题）
    msg['From'] = '136214170@qq.com' # 发件人
    msg['To'] = 'xuhong-sj@bestpay.com.cn' # 收件人
    msg['Subject'] = 'Insight Test Report' # 邮件主题

    # 3. 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8') # 二进制格式打开
    att1["ContentoType"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"' # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        # 4. 连接smtp服务器并发送邮件
        smtp = smtplib.SMTP_SSL(smtp_server) # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user, smtp_password) # 用户名和密码
        smtp.sendmail(sender,receiver, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()


