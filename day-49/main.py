#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\\Users\\LadyDeveloper\\Documents\\Projetos\\software\\geckodriver.exe")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2387160029&f_LF=f_AL&geoId=103644278&keywords=junior%20developer&location=United%20States")

wait = WebDriverWait(driver, 20)
sign_in = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"cta-modal__primary-btn")))
# WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[3]/a[1]"))).click()
sign_in.click()
username = driver.find_element_by_id('username')
username.send_keys("anhacorrea@hotmail.com")

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("XTBuS7mRE9aVTWf")

button = driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button')
button.send_keys(Keys.ENTER)

apply_job = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ember460"]')))
apply_job.click()

next_step = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button/span')
next_step.click()

resume_step = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
resume_step.click()

authorized = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/div/div/div/fieldset/div/div[1]/label')
authorized.click()

review = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
review.click()

submit = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]/span')
submit.click()

driver.quit()
# %%
