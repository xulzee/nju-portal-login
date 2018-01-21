"""
    南京大学网络接入系统自动登录脚本。
    通过模拟发送POST请求。
"""
import urllib.request
import urllib.parse
import json
import time
user = {  # 登录账号密码
    'id': 'abc',
    'password': '123'
}
form_title = '南京大学网络接入系统'
login_url = 'http://p.nju.edu.cn/portal_io/login'  # 登录post的URL
logout_url = 'http://p.nju.edu.cn/portal_io/logout'  # 登出post的URL
info_url = 'http://p.nju.edu.cn/portal_io/proxy/userinfo'


def login():  # 登录
    data = urllib.parse.urlencode({  # 转换post的form并编码
        'username': user['id'],
        'password': user['password']
    }).encode('utf-8')
    post = urllib.request.urlopen(url=login_url, data=data)
    return json.loads(post.read().decode('utf-8'))  # 获得登录信息


def logout():  # 登出
    post = urllib.request.Request(url=logout_url, method='POST')
    con = urllib.request.urlopen(post)
    return json.loads(con.read().decode('utf-8'))

if __name__ == '__main__':
    login = login()

