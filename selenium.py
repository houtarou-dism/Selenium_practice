import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
 
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("https://www.google.com/")
 
search_word = driver.find_element_by_name("q")
search_word.send_keys("セキュリティキャンプ全国大会")
time.sleep(3)
search_word.submit()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='rso']/div/div/div[1]/div/div/div[1]/a").click()   #xpath　クリック
driver.maximize_window()   #ウィンドウ最大

time.sleep(3)

target = driver.find_element_by_class_name("ipar_camp_top_btnarea")   #スクロール処理
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='ipar_main']/div[4]/div/div[1]/div[3]/a").click()

#driver.current_url   カレントurl
time.sleep(3)
target = driver.find_element_by_id("section4")   #スクロール処理
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='ipar_main']/div[3]/div/div[2]").click()   #講義一覧

time.sleep(3)
target = driver.find_element_by_id("list_d3-c5")   #スクロール処理
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()

time.sleep(5)
driver.close()

"""
elements_a = driver.find_elements_by_css_selector("#rso .rc .r a")

for elem in elements_a:
    url = elem.get_property("href")
    print(url)

driver.close()
"""
