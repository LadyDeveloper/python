#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


CHROME_DRIVER_PATH = 'C:\\Users\\LadyDeveloper\\Documents\\Projetos\\software\\geckodriver.exe'
SIMILAR_ACCOUNT = 'weightlosstransformations'
INSTA_USER = 'Mighty_Athenix'
INSTA_PASSWORD = 'hE88XxhMSh2eJSa'


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Firefox(executable_path=path)


    def login(self):
        print('Called login')
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(3)
        username = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
        username.send_keys(INSTA_USER)
        password = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD)
        sleep(3)
        button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
        button.send_keys(Keys.ENTER)
        sleep(4)
        login_info = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        login_info.click()
        sleep(2)
        login_notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        login_notifications.click()



    def find_followers(self):
        print('Called find_followers')
        search = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        search.send_keys(Keys.ENTER)
        sleep(4)
        select_item = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div')
        select_item.click()
        sleep(4)
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(3)
        # ul = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul')
        # li = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')
        scroll_page = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for _ in range(10):
            scroll_page.send_keys(Keys.PAGE_DOWN)
            sleep(2)
        count = 1
        for button in  self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li/div/div/button'):
            print(button.text, count)
            button.click()
            sleep(4)
            count += 1
       

    def follow(self):
        print('Called follow')


        # self.driver.quit()



insta_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

# %%
