from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get("http://192.168.60.146:8080/demo1.html")

if __name__ == '__main__':
    action_chains = ActionChains(driver)
    dd_link = driver.find_element_by_link_text('当当')
    action_chains.key_down(Keys.CONTROL).click(dd_link).key_up(Keys.CONTROL).perform()
    time.sleep(3)

    window_handles = driver.window_handles
    for i in window_handles:
        driver.switch_to.window(i)
        if driver.title.__contains__('当当'):
            break

    time.sleep(3)

    driver.quit()


