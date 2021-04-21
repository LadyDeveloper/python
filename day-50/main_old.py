#%%
import selenium
from selenium import webdriver
import time

path = "C:\\Users\LadyDeveloper\Documents\Projetos\software\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.amazon.com/Lenovo-Ideapad-Computer-Quad-Core-I7-7500U/dp/B08HN8ZSSW/ref=sr_1_8?crid=37JRRL8S26FMT&dchild=1&keywords=laptops+on+sale&qid=1613322898&refinements=p_n_feature_five_browse-bin%3A13580788011%7C13580790011&rnid=2257851011&s=pc&sprefix=lap%2Caps%2C306&sr=1-8")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

time.sleep(5)
 
driver.quit()
# %%

