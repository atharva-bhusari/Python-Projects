import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.in/dp/B09WQY65HN?pf_rd_r=V8ZH07JZKS0JH17X4FMH&pf_rd_p=5836967a-e07d-4336-90ee-f6cdf7f6cad0&pd_rd_r=81d5a7a7-1845-42e9-8aea-1939afca1592&pd_rd_w=cksII&pd_rd_wg=ybr61&ref_=pd_gw_unk"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36/1ghD7CpK-01",
    "Accept-Language" : "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1].replace(",","")
price_as_float = float(price_without_currency)

title = soup.find(id="title").get_text().strip()
print(title)

BUY_PRICE = 18000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )