import threading
import requests
import random2
import os
from requests.utils import dict_from_cookiejar
import time

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

        print("SmartQQ  init() username="+username+" , password="+password)

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

        ##自定义
        self.vcode=''
        self.encrypt_pwd=''

        ##check 界面，如果没看仔细看，好多坑
        self.salt =''
        self.cap_cd = ''
        self.pt_verifysession=''

        self.js_ver = '10125'


        self.ptwebqq=''
        self.clientid = 53999199
        self.status = 'online'

        self.index_url = 'http://w.qq.com/'
        self.check_url = 'https://ssl.ptlogin2.qq.com/check'
        self.captcha_url = 'https://ssl.captcha.qq.com/getimage'
        self.login_url = 'https://ssl.ptlogin2.qq.com/login'
        self.login_2_url = 'http://d.web2.qq.com/channel/login2'

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

        msg = '';

        if rsp.status_code == 200:
            with open(pic_path, 'wb') as f:

                for chunk in rsp.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
                f.close()

            msg = json.dumps({'resp_code':0,'resp_msg':'success'})
        else:
            msg = json.dumps({'resp_code':rsp.status_code,'resp_msg':rsp.content})
            pass

        return msg;

        print('--------finish-------ddd---')

    def del_captcha(self,path):
        if os.path.isfile(path):
            os.remove(path)

    def del_cache(self):
        '''清除缓存'''
        self.vcode=''
        self.encrypt_pwd=''
        self.ptwebqq=''

    def check_vc(self):
        '''check 返回的东西，要仔细看，都是坑'''
        print('check_vc()')

        self.del_cache();

        self.session.get(self.index_url)

        url = self.check_url+ \
                             '?pt_tea=1' \
                             '&uin=%s' \
                             '&appid=501004106' \
                             '&js_ver=%s' \
                             '&js_type=0' \
                             '&login_sig=' \
                             '&u1=http://w.qq.com/proxy.html' \
                             '&r=%s' % (self.username,self.js_ver,str(random2.random()))
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
        print('check url = '+url)
        rsp = self.session.get(url)
        ''':type : requests.Response'''
        if rsp.status_code == 200 :
            # s = "ptui_checkVC('0','!UFV','\x00\x00\x00\x00\x7c\x0f\x3f\xf3','e322f75cb753410b90762a1d05153515118fa46e6186800fba28ab7de4760b6a90e7ad3444b39b48d52eb6819efb231ab1d9379fefd72a14','0');"
            s = rsp.content.decode(encoding='UTF-8')  #bytes  --> str
            print('check rsp : ',s)
            s = s[13:-2]
            s = s.replace('\'','')
            s = s.split(',')

            if s[0] == '0':
                print('不需要验证码')
                self.vcode=s[1]
                self.salt = s[2]
                self.cap_cd = ''
                self.pt_verifysession = s[3]
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

    def __get_encrypt_pwd(self):

        # print('get_encrypt_pwd()')

        '''私有方法：　获取加密密码'''
        from selenium import webdriver
        base_url = "http://127.0.0.1:8888/encrypt"
        driver = webdriver.PhantomJS()
        driver.get(base_url)

        # print(base_url)

        # print('__get_encrypt_pwd()  self.salt = ',self.salt);
        # print('__get_encrypt_pwd()  self.password = ',self.password)
        # print('__get_encrypt_pwd()  self.vcode = ',self.vcode)

        # driver.find_element_by_id('salt').send_keys('\x00\x00\x00\x00\x7c\x0f\x3f\xf3')
        # driver.find_element_by_id('salt').send_keys(self.salt)
        driver.find_element_by_id('salt').send_keys(bytes(self.salt,encoding='utf8'))
        driver.find_element_by_id('pwd').send_keys(self.password)
        driver.find_element_by_id('vcode').send_keys(self.vcode)
        driver.find_element_by_id('bt_01').click()
        print(driver.current_url)
        driver.quit()
        print('__get_encrypt_pwd()  finish()')

    def get_encrypt_pwd(self):
        '''获取加密密码'''
        w = threading.Thread(name='worker', target=self.__get_encrypt_pwd)
        w.start()

    def sign_in(self):

        print('sign_in()')

        if not self.encrypt_pwd:
            self.get_encrypt_pwd()
        else:
            self.sign_in_first()


    def sign_in_first(self):
        '''第一次登录'''
        print('encrypt_pwd.length=',len(self.encrypt_pwd))
        print('u = '+self.username)
        print('vcode = '+self.vcode)
        # print('encrypt_pwd = '+self.encrypt_pwd)

        cookies = dict_from_cookiejar(self.session.cookies)
        self.pt_verifysession = cookies['ptvfsession']
        # print('pt_verifysession='+self.pt_verifysession)

        par = {
            'u':self.username,
            'p':self.encrypt_pwd,
            'verifycode':self.vcode,
            'webqq_type':10,
            'remember_uin':1,
            'login2qq':1,
            'aid':501004106,
            'u1':'http://w.qq.com/proxy.html?login2qq=1&webqq_type=10',
            'h':1,
            'ptredirect':0,
            'ptlang':2052,
            'daid':164,
            'from_ui':1,
            'pttype':1,
            'dumy':'',
            'fp': 'loginerroralert',
            'action':'0-17-8156',     ##改变 ##写死
            'mibao_css':'m_webqq',
            't':1,
            'g':1,
            'js_type':0,
            'js_ver':self.js_ver,
            'login_sig':'',
            'pt_randsalt':0,
            'pt_vcode_v1':0,
            'pt_verifysession_v1':self.pt_verifysession, ##改变
        }

        from urllib.parse import urlencode

        url = self.login_url+'?%s' %   urlencode(par)

        # print('login_url = '+url)

        self.session.headers.update({
            'Accept': '*/*',
            'Referer': 'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http//w.qq.com/proxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        })

        rsp = self.session.get(url)
        # print(rsp.content.decode(encoding='UTF-8'))

        print(rsp.content)

        ''':type : requests.Response'''
        if rsp.status_code == 200 :
            cookies = dict_from_cookiejar(self.session.cookies)
            try:
                if cookies['ptwebqq']:
                    self.ptwebqq = cookies['ptwebqq']
                    # self.sign_in_second();
                    self.getvfwebqq()
            except Exception as e:
                print(e)
            # print(cookies)
            # print(rsp.headers)
        else:
            print(rsp.status_code)


    def getvfwebqq(self):
        ''''''
        print('getvfwebqq()')

        url = 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq=%s&clientid=53999199&psessionid=&t=%s' % (self.ptwebqq,str(int(time.time())))

        self.session.headers.update({
            'Accept': '*/*',
            'Referer':'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1',
            'Content-Type': 'utf-8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Accept':'*/*',
        })

        rsp = self.session.get(url)
        ''':type : requests.Response'''
        print(rsp.status_code)
        print(rsp.url)
        print(rsp.content)

        if rsp.status_code == 200 :
            self.sign_in_second()
        else:
            print('else return')



    def sign_in_second(self):
        '''第二次post登录'''
        print('sign_in_second()')

        header = {
            'Origin': 'http://d.web2.qq.com',
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': "http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2",
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4'
        }

        # str_tmp = '{"ptwebqq"="%s","clientid"=%s,"psessionid"="","status"="%s"}' % (self.ptwebqq,self.clientid,self.status)

        # data = 'r=%7B%22status%22%3A%22online%22%2C%22ptwebqq%22%3A%22' + self.ptwebqq + '%22%2C%22passwd_sig%22%3A%22%22%2C%22clientid%22%3A%22'+self.clientid+'%22%2C%22psessionid%22%3Anull%7D&clientid='+self.clientid+'&psessionid=null'

        # data = 'r=%7B%22ptwebqq%22%3A%22'+self.ptwebqq+'%22%2C%22clientid%22%3A'+self.clientid+'%2C%22psessionid%22%3A%22%22%2C%22status%22%3A%22online%22%7D'
        #
        # post_data = {
        #     'r':str_tmp
        # }
        #
        # print('post_data = ',post_data)

        # cookies = dict_from_cookiejar(self.session.cookies)
        # print('cookies = ',cookies)
        # return;

        post_data = 'r=%7B%22ptwebqq%22%3A%22'+self.ptwebqq+'%22%2C%22clientid%22%3A'+str(self.clientid)+'%2C%22psessionid%22%3A%22%22%2C%22status%22%3A%22online%22%7D'

        rsp = self.session.post(
            url=self.login_2_url,
            data=post_data,
            headers=header,
        )
        ''':type : requests.Response'''

        print(rsp.status_code)
        # print(rsp.headers)
        print(rsp.url)
        print(rsp.content)

        if rsp.status_code == 200 :
            pass
        else:
            pass

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

if __name__ == '__main__':

    # print('start')
    # import time
    # time.sleep(3)
    # print('finish ')



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

    qq.ptwebqq = 'dea75142dc6e91fd609e47c9c7c3fcd63d5d48f1a5631d2e2480825cab90d6b4'
    # # post_data=r'{"ptwebqq": "%s","clientid": "%s","psessionid": "","status":"%s"}' % (qq.ptwebqq,qq.ptwebqq,qq.status)
    # post_data='r:{"ptwebqq"="%s","clientid"=%s,"psessionid"="","status"="%s"}' % (qq.ptwebqq,qq.clientid,qq.status)
    # print(post_data)
    #
    #
    # str_tmp = json.dumps(
    #     {
    #         "ptwebqq":qq.ptwebqq,
    #         "clientid":qq.clientid,
    #         "status":qq.status
    #     })
    #
    # tmp  = 'r:'+str_tmp
    #
    # print(tmp)

    # str_tmp = json.dumps({"ptwebqq":qq.ptwebqq,"clientid":qq.clientid,"status":qq.status})

    # print(type(str_tmp))
    # print(str_tmp)

    # post_data='r:{"ptwebqq"="%s","clientid"=%s,"psessionid"="","status"="%s"}' % (qq.ptwebqq,qq.clientid,qq.status)

    # str_tmp = '{"ptwebqq"="%s","clientid"=%s,"psessionid"="","status"="%s"}' % (qq.ptwebqq,qq.clientid,qq.status)
    #
    # post_data = {
    #     'r':str_tmp
    # }

    post_data = 'r=%7B%22ptwebqq%22%3A%22'+qq.ptwebqq+'%22%2C%22clientid%22%3A'+str(qq.clientid)+'%2C%22psessionid%22%3A%22%22%2C%22status%22%3A%22online%22%7D'

    print(post_data)
    #
    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    #
    rsp = qq.session.post(
        'http://127.0.0.1:8888/test',
            data=post_data,
            headers=header)

    ''':type : requests.Response'''
    print(rsp.status_code)
    print(rsp.url)
    print(rsp.content)



    #
    # qq.check_vc();
    #
    # if qq.cap_cd :
    #     qq.get_captcha()


    # qq.test()