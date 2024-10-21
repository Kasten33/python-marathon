import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

lat = 40.71
lon = -111.89

parameters = {
    "lat": lat,
    "lng": lon,
    "formatted": 0
}
def ISS():


    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    ISSLat = float(data["iss_position"]["latitude"])
    ISSLon = float(data["iss_position"]["longitude"])

    if lat-5 <= ISSLat <= lat+5 and lon-5 <= ISSLon <= -lon+5:
        return True

def night():
    response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status() 
    data = response2.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour






    if time_now >= sunset or time_now <= sunrise:
        return True



while True:
    time.sleep(300)

    if ISS() and night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email, 
            to_addrs=email,
            Subject="Look Up",
            msg="The ISS is above you in the sky"
           )
        connection.close() 
