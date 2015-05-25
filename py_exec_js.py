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

    # driver.set_window_size(1120, 550)
    # driver.execute_script("console.log('Hello, world!')")
    # driver.execute_script('/home/chenwei/workspace/pythonProject/TestTornadoServer/pjs/hello.js')
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
def test_4():
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    # driver.execute_script("window.blah = function () {document.body.innerHTML='testing';}")
    # driver.execute_script("blah()")
    driver.get('test.html')
    driver.quit()
def test_5():
    pass
    driver = webdriver.PhantomJS()
    driver.get(base_url)

    time.sleep(3)

    # driver.find_element_by_id('test_alert').click()
    data = driver.find_element_by_id('test_alert').text

    # data = driver.find_element_by_id('mytest').text
    # data = driver.find_element_by_id('mytest').is_displayed()

    print(data)
    # print(driver.current_url)
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
    # driver.execute_script()
    # driver.get("https://duckduckgo.com/")
    # driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
    # driver.find_element_by_id("search_button_homepage").click()
    # print driver.current_url


    driver.get(base_url)


    driver.find_element_by_id('fromjssubmit').click()
    # data = driver.find_element_by_id('test_alert').text
    # print(data)
    # print(driver.page_source)
    print(driver.current_url)
    driver.quit()

if __name__ == '__main__':
    pass
    # test_6()
    # test()
    # test_1()
    test_2()
    # test_3()
    # test_4()
    # import os
    # print(os.environ['HTTP_PROXY'])
