from bs4 import BeautifulSoup
import requests
import smtplib
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers={"Accept-Language":"en-US"})
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
# fraction = soup.find(name="span", class_="a-price-fraction").getText()
def StartTracking():
    while True:
        now = datetime.now()
        if now.hour == 9 and now.minute == 0:
            if price <= "100":
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(
                    from_addr=email, 
                    to_addrs=email,
                    msg=f"Subject:Price Drop\n\nThe price of the item you are tracking has dropped to {price}.\n\n"
                )
                connection.close()
            else:
                print("Price is still too high")
                break
        else:
            print("Not the right time")
            break

StartTracking() 