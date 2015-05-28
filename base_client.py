__author__ = 'chenwei'

from requests.utils import cookiejar_from_dict, dict_from_cookiejar
import configparser
from utils import config_file

cf = configparser.ConfigParser()
cf.read(config_file)

class BaseClient:
    '''
    抽象 : QQ,微信,人人网,v2ex[已登录],知乎[已登录],百度,淘宝,12306
    '''
    def __init__(self):
        pass

    def sign_in(self):
        '''登录'''
        pass

    def has_sign_in(self):
        '''是否登录'''
        pass

    def loginout(self):
        '''注销'''
        pass

    def register(self):
        '''注册'''
        pass

    def load_cookies(self):
        '''加载cookies'''
        print("load_cookies()")

        if cf.has_option(self.config_section,self.config_cookies):
            ##string to dict
            d = eval(cf.get(self.config_section,self.config_cookies))
            self.session.cookies.update(cookiejar_from_dict(d))

    def clear_cookies(self):
        pass
    def save_cookies(self):
        '''保存cookies'''
        print("save_cookies()")
        cookies = dict_from_cookiejar(self.session.cookies)

        self.write_config(self.config_section,self.config_cookies,str(cookies))

    def write_config(self,section,key,value):
        '''
        写入配置文件
        :param section:
        :param key:
        :param value:
        '''
        if cf.has_section(section):
            cf.set(section,key,value);
            cf.write(open(config_file,"w"))
        else:
            cf.add_section(section)
            cf.set(section,key,value);
            cf.write(open(config_file,"w"))