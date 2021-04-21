#%%
import requests
from bs4 import BeautifulSoup
import smtplib
import datetime

MY_EMAIL = "anadevmanuel@gmail.com"
PASSWORD = "cCuiKjXuwg82Whm"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept-Language': 'en'
}

url = "https://www.amazon.com/Apple-MacBook-16-Inch-Storage-2-6GHz/dp/B081FWLDZ2/ref=sr_1_27?crid=3CKIKJVFJQJGZ&dchild=1&keywords=apple+macbook+air&qid=1611801832&s=electronics&sprefix=apple+mac%2Celectronics%2C233&sr=1-27"
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "lxml")

price = soup.find(id="priceblock_ourprice").text
#%%
now = datetime.datetime.now()
send_time = now.strftime('%H')

if send_time == "19":
    print("Sending email")
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="anhacorrea@gmail.com", 
            msg=f"Subject:It is time to buy your new laptop.\n\nThe price is {price}\nHere is the link: {url}"
        )


# %%
