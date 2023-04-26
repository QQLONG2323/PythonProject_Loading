import requests
from bs4 import BeautifulSoup
import re
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

res = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW",headers = headers)

res.encoding = 'utf-8'


soup = BeautifulSoup(res.text,'html.parser')
data = soup.find('table', {'title': '牌告匯率'}).find('tbody')

csvFile = open('台灣銀行匯率.csv','w+', encoding='utf-8', newline='')

try:
    writer = csv.writer(csvFile)
    writer.writerow(['幣別', '現金買入', '現金賣出'])
    for row in data.find_all('tr'):
        currency = row.find('div', {'class': 'visible-phone'}).text.strip()  # 幣別
        buy_rate = row.find('td', {'data-table': '本行現金買入'}).text.strip()  # 現金買入
        sell_rate = row.find('td', {'data-table': '本行現金賣出'}).text.strip()  # 現金賣出
        print(currency, buy_rate, sell_rate)
        tdRow = [currency, buy_rate, sell_rate]
        writer.writerow(tdRow)
finally:
    csvFile.close()