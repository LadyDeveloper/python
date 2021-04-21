from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_webdriver_path = "C:\\Users\\LadyDeveloper\\Documents\\Projetos\\software\\chromedriver.exe"
driver = webdriver.Chrome(chrome_webdriver_path)
driver.get('https://www.appbrewery.co/p/newsletter')



email = driver.find_element_by_name("email")
submit = driver.find_element_by_name("commit")

email.send_keys("anhacorrea@hotmail.com")
submit.send_keys(Keys.ENTER)
