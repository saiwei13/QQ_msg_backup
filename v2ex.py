import re
import requests
from mock_login.base_client import BaseClient

__author__ = 'chenwei'

class V2EX(BaseClient):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

        self.index_url = 'http://v2ex.com'
        self.sign_url = 'http://v2ex.com/signin'
        self.mission_url = 'http://v2ex.com/mission/daily'

        self.config_section = 'v2ex'
        '''配置文件字段'''
        self.config_cookies = 'cookies'
        '''配置文件字段'''

    def sign_in(self):
        '''
        登陆操作
        :return :  True  登陆成功
                   False 登陆失败
        '''
        resp = self.session.get(self.sign_url)
        once = re.search(r'value="(\d+)" name="once"', resp.text).group(1)
        post_data={
                'u': self.username,
                'p': self.password,
                'once': once,
                'next': '/'
        }

        rsp = self.session.post(
            url=self.sign_url,
            data=post_data,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': resp.url
            }
        )
        ''':type : requests.Response'''
        if rsp.url[:-1]== self.sign_url:
            print("登陆失败 url=",rsp.url)
            return False
        elif rsp.url[:-1] == self.index_url:
            print("登陆成功")
            return True
        else :
            print("登陆失败 url=",rsp.url)
            return False

    def has_sign_in(self):
        resp = self.session.get(self.index_url)
        return 'signout' in resp.text

    def get_reward(self):
        '''
        领取登陆奖励
        :return:
        '''
        resp = self.session.get(self.mission_url)

        if '每日登录奖励已领取' in resp.text:
            print('每日登录奖励已领取')
            return;

        if '/balance' not in resp.text:
            print('return  url ='+resp.url)
            # print(resp.text)
            return

        once = re.search(r'once=(\d+)\'', resp.text).group(1)
        rsp = self.session.get(
            url='https://www.v2ex.com/mission/daily/redeem?once=%s' % once,
            headers={'Referer': resp.url}
        )
        ''':type : requests.Response'''

        if '每日登录奖励已领取' in rsp.text:
            print('奖励领取成功')


if __name__ == '__main__':

    from mock_login.utils import config_file

    import configparser
    cf = configparser.ConfigParser()
    cf.read(config_file)

    v2ex = V2EX(
        username=cf.get('v2ex','username'),
        password=cf.get('v2ex','password')
    )
    v2ex.load_cookies()
    if not v2ex.has_sign_in():
        print('还没登陆')
        if v2ex.sign_in():
            v2ex.save_cookies()
            v2ex.get_reward()
    else:
        print('已登陆')
        v2ex.get_reward()