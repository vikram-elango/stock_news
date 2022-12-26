import requests
from twilio.rest import Client


TWILLIO_ACCOUNT_SID="TWILLIO_ACCOUNT_SID"
TWILLIO_AUTH_TOKEN="TWILLIO_AUTH_TOKEN"

account_sid=TWILLIO_ACCOUNT_SID
auth_token=TWILLIO_AUTH_TOKEN
STOCK = "TSLA"
COMPANY_NAME = "tesla"
API_KEY="API_KEY"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

response=requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={API_KEY}")
data=response.json()


price2=float(data["Time Series (Daily)"][f"2022-12-{21}"]["4. close"])
price1=float(data["Time Series (Daily)"][f"2022-12-{22}"]["4. close"])

if price1-price2<0 and (price2-price1)/abs(price1)*100>5:
    print(f"GET NEWS")
    response2=requests.get(f" https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&apiKey=apiKey")
    data2=response2.json()
    for i in range(1,4):
        client=Client(account_sid,auth_token)
        message=client.messages.create(
            body=f"{STOCK}: {round((price2-price1)/abs(price1)*100)}% 📈\n"
                 f"Headline: {data2['articles'][i]['title']}\n"
                 f"Brief: {data2['articles'][i]['description']}\n",
            from_="+twillio_number",
            to="+your_number"
        )

elif price1-price2>0 and (price1-price2)/abs(price1)*100>5:
    print(f"GET NEWS")
    response3=requests.get(f" https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&apiKey=apiKey")
    data3=response3.json()
    for i in range(1,4):
        client=Client(account_sid,auth_token)
        message = client.messages.create(
            body=f"{STOCK}: {round((price1 - price2) / abs(price1) * 100)}% 📉\n"
                 f"Headline: {data3['articles'][i]['title']}\n"
                 f"Brief: {data3['articles'][i]['description']}\n",
            from_="+twillio_number",
            to="+your_number"
        )

