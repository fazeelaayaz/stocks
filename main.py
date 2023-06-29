import requests
import os
from twilio.rest import Client
from config import API_KEY_STOCK, API_KEY_NEWS, ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_PHONE_NUMBER

client = Client(ACCOUNT_SID, AUTH_TOKEN)

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": API_KEY_STOCK
}

response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

difference = round(yesterday_closing_price - day_before_yesterday_closing_price, 2)

diff_percent = round((difference / yesterday_closing_price) * 100, 2)
up_down = ''
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

if abs(diff_percent) > 1:

    news_param = {
        "apiKey": API_KEY_NEWS,
        "qInTitle": "TESLA",
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_param)
    data_news = news_response.json()["articles"]
    data_news_list = data_news[:3]
    format_news = [f"TESLA: {up_down}{diff_percent}%\nHeadline: {news['title']}. \nBrief: {news['description']}" for news in data_news_list]
    for news in format_news:
        message = client.messages.create(
            body=news,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )


