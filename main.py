import datetime
import yagmail
from decouple import config
import pandas as pd
from news import NewsFeed

df = pd.read_excel('peoples.xlsx')
userID = config('userID', default='')
password = config('password', default='')

for index, row in df.iterrows():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # initialize news feed for each user
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)

    email = yagmail.SMTP(user=userID, password=password)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi, {row['name']}\n See what's on about {row['interest']} today. \n"
                        f"{news_feed.get()} \n Yagmur")
