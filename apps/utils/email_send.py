#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time    : 2020/2/16 20:10
# @Author  : Leon Zhou
# @Email   : zx-leon@163.com
# @File    : email_send.py
# @Software: PyCharm
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = 'Leon在线网注册激活链接'
        email_body = f'请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{code}'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = 'Leon在线网密码重置'
        email_body = f'请点击下面的链接激活你的账号：http://127.0.0.1:8000/reset/{code}'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str



