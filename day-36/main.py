import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
import math

account_sid ="ACdfefee402711a051b1f4b3141a879ffa"
auth_token = "f10181b1a6830c46f581b745a04bf5ce"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#API_KEY_ALPHAVANTAGE="0WDZC89PHTSOVYRJ"
#API_KEY_NEWSAPI="06c5a85bfb34457e92db7cbc952e151f"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

emogi = ""

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": os.environ.get("API_KEY_ALPHAVANTAGE")
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": os.environ.get("API_KEY_NEWSAPI")
}

#Getting date
yesterday_date = str(datetime.today() - timedelta(days=1)).split(' ', 1)[0]
day_before_yesterday = str(datetime.today() - timedelta(days=2)).split(' ', 1)[0]

#Requesting API data - Stocks
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()

#Requesting API data - News
news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#yesterday_stock = . [new_value for (key, value) in dictionary.items()]

yesterday_stock_price = float(stock_data['Time Series (Daily)'][yesterday_date]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_stock_price = float(stock_data['Time Series (Daily)'][day_before_yesterday]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff_stock_price = abs(float(yesterday_stock_price) - float(day_before_yesterday_stock_price))

if float(yesterday_stock_price) > float(day_before_yesterday_stock_price):
    emogi = "🔺"
else:
    emogi = "🔻"
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_perct_price = (diff_stock_price / yesterday_stock_price) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_perct_price > 5:
    #print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    articles = news_data['articles'][:3]


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    for article in articles:
        title = article['title']
        description = article['description']
        msg = f"{COMPANY_NAME}: {emogi}{math.ceil(diff_perct_price)}%\nHeadline: {title}\nBrief: {description}"
        print(msg)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=msg,
                from_='+16193562614',
                to='+17022046034'
            )
        print(message.status)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

