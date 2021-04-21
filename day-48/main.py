from selenium import webdriver


chrome_driver_path ="C:\\Users\\LadyDeveloper\\Documents\\Projetos\\software\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')

# time = [li.text for li in driver.find_elements_by_tag_name('time')]
time = [li.text for li in driver.find_elements_by_css_selector('.event-widget > div:nth-child(1) > ul:nth-child(3) > li > time')]
events = [li.text for li in driver.find_elements_by_css_selector('.event-widget > div:nth-child(1) > ul:nth-child(3) > li > a')]

dict_events = {}

for item in range(len(events)):
    dict_events[item] = {
        "name": events[item],
        "time": time[item]
    }
print(dict_events)

driver.quit()