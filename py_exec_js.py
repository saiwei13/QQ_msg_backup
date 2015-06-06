import threading
from selenium.webdriver.common.by import By

__author__ = 'chenwei'


from selenium.webdriver import Proxy, DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
import time

__author__ = 'chenwei'

from selenium import webdriver

base_url = 'http://127.0.0.1:8888'

def test():
    pass
    base_url = 'http://www.baidu.com'
    driver = webdriver.PhantomJS()
    driver.get(base_url)
    print(driver.current_url)
    data = driver.find_element_by_id('cp').text
    print(data)
    # print(driver.current_url)
    driver.quit()

def test_1():
    from ghost import Ghost
    ghost = Ghost()
    page, extra_res = ghost.open('http://www.baidu.com')

    print(page.http_status)
    print(ghost.content)

def test_3():
    driver = webdriver.Firefox()
    driver.get("http://m.mail.10086.cn")
    driver.implicitly_wait(30)
    driver.find_element_by_id("ur").send_keys("手机号")
    driver.find_element_by_id("pw").send_keys("密码")
    driver.find_element_by_class_name("loading_btn").click()
    driver.quit()


def test_6():
    from ghost import Ghost

    base_url = 'http://127.0.0.1:8888'

    ghost = Ghost()
    ghost.open(base_url)
    # page, extra_res = ghost.open(base_url)
    # print(page.http_status)
    # print(ghost.content)

def test_2():
    driver = webdriver.PhantomJS()
    # driver.set_window_size(1120, 550)
    driver.get(base_url)
    driver.find_element_by_id('username').send_keys('username')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('test_ajax').click()
    print(driver.current_url)
    driver.quit()

def test_3():
    driver = webdriver.Firefox()

    # driver = webdriver.PhantomJS()
    # driver.set_window_size(1120, 550)
    driver.get("https://ssl.ptlogin2.qq.com/check?pt_tea=1&uin=2081374195&appid=501004106&js_ver=10124&js_type=0&login_sig=&u1=http://w.qq.com/proxy.html&r=0.5679909912869334")
    # driver.find_element_by_id('username').send_keys('username')
    # driver.find_element_by_id('password').send_keys('123456')
    # driver.find_element_by_id('test_ajax').click()
    print(driver.current_url)
    print(driver.page_source)
    # driver.quit()

def get_encrypt_pwd():
    '''获取加密密码'''

    print('get_encrypt_pwd()')
    base_url = "http://127.0.0.1:8888/encrypt"
    driver = webdriver.PhantomJS()
    driver.get(base_url)
    print(base_url)
    driver.find_element_by_id('salt').send_keys('\x00\x00\x00\x00\x7c\x0f\x3f\xf3')
    driver.find_element_by_id('pwd').send_keys('gguuss')
    driver.find_element_by_id('vcode').send_keys('')
    driver.find_element_by_id('bt_01').click()
    print(driver.current_url)
    driver.quit()

    print('quit()')


def worker(str):

    print(str)
    print (threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print (threading.currentThread().getName(), 'Exiting')

def test_thread():
    w = threading.Thread(name='get_encrypt_pwd', target=get_encrypt_pwd)
    w.start()


if __name__ == '__main__':

    s = "ptuiCB('0','0','http://ptlogin4.web2.qq.com/check_sig?pttype=1&uin=2081374195&service=login&nodirect=0&ptsigx=26ec0347eb5084a199eaf9f7dad05afccdaf4e86055b2c37dcbb1a90aeb234038afc5bb272e734768ac7a0c9184d6bef3a9fec1f9fcb83c0231adc0760a0c8a0&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&f_url=&ptlang=2052&ptredirect=100&aid=501004106&daid=164&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=1&pt_aid=0&pt_aaid=0&pt_light=0&pt_3rd_aid=0','0','\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x81', 'rtokie')"
    s = s[7:-1]
    print(s)



    # w = threading.Thread(name='worker', target=worker('3'))
    # w2 = threading.Thread(target=worker) # use default name
    #
    # w.start()
    # w2.start()

    # print('hello world')
    #
    # action = [0, 0];

    # import time
    # print(int(time.time()))

    # salt = '\x00\x00\x00\x00\x7c\x0f\x3f\xf3';
    # print(bytes(salt,encoding='utf8'))

    # pass
    #
    # get_encrypt_pwd();
    # test_6()
    # test()
    # test_1()
    # test_3()
    # test_3()
    # test_4()
    # import os
    # print(os.environ['HTTP_PROXY'])
