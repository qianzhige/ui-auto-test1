from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    # driver.get 打开一个指定网页
    driver.get("http://192.168.60.146:8080/demo1.html")
    # 等待几秒
    time.sleep(1)
    #定位元素
    input_el = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/input")
    # 输入值
    input_el.send_keys("只要E的够快,队友问号就追不上你")
    time.sleep(1)
    # clean : 清除
    input_el.clear()
    time.sleep(1)



    # 定位元素 通过 id 去定位
    file_el = driver.find_element_by_id('file1')
    file_el.send_keys('C:/Users/Administrator/Desktop/1560155219(1).jpg')
    time.sleep(1)

    # 定位元素 通过 name 去定位
    radio_els = driver.find_elements_by_name('radio')
    print(type(radio_els))
    # 操作元素 , 点击
    radio_els[0].click()
    time.sleep(1)
    radio_els[1].click()
    time.sleep(1)

    # input_demo(driver)

    checkbox_els = driver.find_elements_by_class_name('checkbox')
    print(checkbox_els)
    checkbox_els[0].click()
    time.sleep(1)
    checkbox_els[1].click()
    time.sleep(1)
    checkbox_els[2].click()
    time.sleep(1)

    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    button_el.click()
    # 输入弹框中的值
    time.sleep(1)
    driver.switch_to.alert.send_keys('我不知道说啥')#暂时不执行
    time.sleep(1)
    # 确认弹窗
    driver.switch_to.alert.accept()
    time.sleep(1)
    # 取消弹窗
    # driver.switch_to.alert.dismiss()

    driver.find_element_by_xpath('//input[@type="password"]').send_keys('123456')
    number_el = driver.find_element_by_xpath('//input[@type="number"]')
    number_el.send_keys('20')
    time.sleep(1)

    selector_el = driver.find_element_by_css_selector(
        'body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select ')

    s = Select(selector_el)

    s.select_by_index(1)
    time.sleep(1)
    s.select_by_value('z1')
    time.sleep(1)
    s.select_by_visible_text('周龙3')
    time.sleep(1)

    driver.find_element_by_link_text('当当').click()
    time.sleep(3)
    driver.back()
    time.sleep(1)
    driver.find_element_by_partial_link_text('度娘').click()
    time.sleep(3)
    driver.back()
    time.sleep(1)
    driver.forward()
    time.sleep(3)
    driver.refresh()
    time.sleep(3)

    # 关闭浏览器
    driver.quit()
    # driver.close()  也可以关闭浏览器,但是无法关闭驱动程序 ,一般用quit ,关闭的更彻底


    pass