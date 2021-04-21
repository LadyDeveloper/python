from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path ="C:\\Users\\LadyDeveloper\\Documents\\Projetos\\software\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')
cookie.click()
money = driver.find_element_by_id('money').text
store = [store.text.strip().split('-') for store in driver.find_elements_by_css_selector('#store div b')]
