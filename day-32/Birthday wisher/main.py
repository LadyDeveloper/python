import datetime as dt
import smtplib
import random


MY_EMAIL = "anadevmanuel@gmail.com"
PASSWORD = "cCuiKjXuwg82Whm"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt", encoding='cp437') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="anadevmanuel@yahoo.com", 
            msg=quote
        )




# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1990, month=12, day=15, hour=2)
# print(date_of_birth)