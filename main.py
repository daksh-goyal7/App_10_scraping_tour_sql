import requests
import selectorlib
from send_email import send_email
import time
import sqlite3

#SQL implementation
connection=sqlite3.connect('data1.db')
cursor=connection.cursor()

URL="https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def scrape(url):
    response=requests.get(url,headers=HEADERS)
    source=response.text
    return source
def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
    value=extractor.extract(source)["tours"]
    return value

def store(extracted):
    with open("data.txt","a") as file:
        file.write(extracted+"\n")

def read(extracted):
    with open("data.txt","r") as file:
        return file.read()
while True:
    scraped=scrape(URL)
    extracted=extract(scraped)
    print(extracted)
    content=read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            values=extracted.split(',')
            values=[item.strip() for item in values]
            cursor.execute("Insert Into events Values(?,?,?)",values)
            connection.commit()
            send_email(extracted)
    time.sleep(5)
