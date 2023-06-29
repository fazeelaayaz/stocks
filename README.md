# Stock Price and News Notification

This Python script retrieves the daily stock price of TESLA (TSLA) from the Alpha Vantage API and sends a notification containing the price difference and relevant news headlines using the Twilio API.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `twilio`
- Alpha Vantage API key
- NewsAPI API key
- Twilio account SID and auth token
- Twilio phone number (sender)
- Recipient phone number (receiver)

## Installation

1. Clone the repository or download the script file.

2. Install the required Python libraries using pip:

   ```shell or python terminal
   pip install requests
   pip install twilio

### Obtain the necessary API keys and Twilio account information.

Create a file named config.py in the same directory as the script.

In the config.py file, define the following variables with your API keys and Twilio account information:

python
Copy code
API_KEY_STOCK = "YOUR_ALPHA_VANTAGE_API_KEY" (https://www.alphavantage.co/support/#api-key)
API_KEY_NEWS = "YOUR_NEWSAPI_API_KEY"        (https://newsapi.org/)
ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"      (https://www.twilio.com/en-us)
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
RECIPIENT_PHONE_NUMBER = "YOUR_RECIPIENT_PHONE_NUMBER"
Make sure to replace the placeholders with your actual values.

### Run the script:

Write the following command in microsoft powershell
python stock_price_notification.py

### Usage
The script retrieves the daily adjusted closing prices of TSLA stock using the Alpha Vantage API.

It calculates the price difference and percentage change between the most recent closing price and the previous day's closing price.

If the percentage change is greater than 1%, it fetches the latest news articles related to TESLA using the NewsAPI. (Difference can be set according to personal preference).

It constructs a notification message containing the stock price change and headlines with brief descriptions of the news articles.

The script sends the notification message to the specified recipient using the Twilio API.
