import requests
import random2
import os

__author__ = 'chenwei'

from base_client import BaseClient
import json

#验证码图片路径
pic_path = "static/img/pic.jpg"



'''
json 协议：

check:
    rsp:    {resp_code:0,resp_msg:'需要验证码',resp_data:true}
            {resp_code:0,resp_msg:'不需要验证码',resp_data:false}

            {resp_code:1001,resp_msg:'请求失败',resp_data:false}

'''



class SmartQQ(BaseClient):
    ''''''
    def __init__(self, username, password):


        print("SmartQQ  init() 初始化")

        self.username = username
        self.password = password
        self.session = requests.session()

        ## check 使用
        self.pt_tea = '1';
        self.appid = '501004106';
        self.js_ver = '10123';
        self.js_type = 0;
        self.login_sig ='';
        self.u1 = 'http://w.qq.com/proxy.html'
        # self.r =

        self.salt =''
        self.cap_cd = ''

        self.index_url = 'http://w.qq.com/'
        self.check_url = 'https://ssl.ptlogin2.qq.com/check'
        self.captcha_url = 'https://ssl.captcha.qq.com/getimage'

        self.config_section = 'qq'
        '''配置文件字段'''
        self.config_cookies = 'cookies'
        '''配置文件字段'''

    def get_captcha(self):

        '''获取验证码'''

        print('get_captcha()')

        rsp = self.session.get(self.index_url)

        url = self.captcha_url+ \
                             '?aid=501004106' \
                             '&r=%s' \
                             '&uin=%s' \
                             '&cap_cd=%s' \
                              % (str(random2.random()),self.username,self.cap_cd)

        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Referer':'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'
        })

        rsp = self.session.get(url)
        ''':type : requests.Response'''

        print(rsp.url)

        # print(rsp.status_code)
        # print(rsp.content)
        # s = rsp.content.decode(encoding='UTF-8');
        # print()


        with open(pic_path, 'wb') as f:
            for chunk in rsp.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
            f.close()

        print('--------finish-------ddd---')

    def del_captcha(self,path):
        if os.path.isfile(path):
            os.remove(path)

    def check_vc(self):
        print('check_vc()')

        url = self.check_url+ \
                             '?pt_tea=1' \
                             '&uin=%s' \
                             '&appid=501004106' \
                             '&js_ver=10124' \
                             '&js_type=0' \
                             '&login_sig=' \
                             '&u1=http://w.qq.com/proxy.html' \
                             '&r=%s' % (self.username,str(random2.random()))
        print(url)

        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Referer':'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'
        })

        # proxies = {
        #     "http": "http://127.0.0.1:8118",
        #     "https": "http://127.0.0.1:8118",
        # }

        rsp = self.session.get(url)
        ''':type : requests.Response'''
        if rsp.status_code == 200 :
            # s = "ptui_checkVC('0','!UFV','\x00\x00\x00\x00\x7c\x0f\x3f\xf3','e322f75cb753410b90762a1d05153515118fa46e6186800fba28ab7de4760b6a90e7ad3444b39b48d52eb6819efb231ab1d9379fefd72a14','0');"
            s = rsp.content.decode(encoding='UTF-8')  #bytes  --> str
            s = s[13:-2]
            s = s.replace('\'','')
            s = s.split(',')

            if s[0] == '0':
                print('不需要验证码')
                self.salt = s[2]
                self.cap_cd = ''
                print('salt='+self.salt)
                self.del_captcha(pic_path)
                tmp = json.dumps({'resp_code':0,'resp_msg':'不需要验证码','resp_data':False})
            elif s[0] == '1':
                print('需要验证码')
                self.cap_cd = s[1];
                self.salt = s[2]
                print('salt='+self.salt+" ,  cap_cd="+self.cap_cd)
                tmp = json.dumps({'resp_code':0,'resp_msg':'需要验证码','resp_data':True})
        else :
            print(rsp.status_code)
            print(rsp.content)
            tmp = json.dumps({'resp_code':rsp.status_code,'resp_msg':rsp.content,'resp_data':False})
        return tmp;


    def test(self):
        s = "ptui_checkVC('0','!UFV','\x00\x00\x00\x00\x7c\x0f\x3f\xf3','e322f75cb753410b90762a1d05153515118fa46e6186800fba28ab7de4760b6a90e7ad3444b39b48d52eb6819efb231ab1d9379fefd72a14','0');"
        s = s[13:-2]
        print(s)
        s = s.replace('\'','')
        print(s)
        s = s.split(',')

        print('--------------------------------')

        for i in range(0,len(s)):
            print(s[i])
        # print(len(s[0]))
        # print(len(s[1]))


    def test2(self):
        pass
if __name__ == '__main__':

    # tmp = 'ss'
    # tmp2 = tmp+'dd'
    # print(tmp2)

    from utils import config_file

    import configparser
    cf = configparser.ConfigParser()
    cf.read(config_file)

    qq = SmartQQ(
        username=cf.get('qq','username'),
        password=cf.get('qq','password')
    );

    qq.check_vc();

    if qq.cap_cd :
        qq.get_captcha()


    # qq.test()