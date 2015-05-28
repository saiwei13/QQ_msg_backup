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
    driver.set_window_size(1120, 550)
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

if __name__ == '__main__':
    pass
    # test_6()
    # test()
    # test_1()
    test_3()
    # test_3()
    # test_4()
    # import os
    # print(os.environ['HTTP_PROXY'])
