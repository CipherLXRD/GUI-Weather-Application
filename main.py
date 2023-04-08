import datetime
import requests

api_key = "aebf681c14fef7c76407c4c8fe9141fe"
units = "metric"
url = f"https://api.openweathermap.org/data/2.5/onecall?lat=25.3176&lon=82.9739&exclude=current,minutely,hourly&appid={api_key}&units=metric"

response = requests.get(url)

forecast_data = response.json()["daily"]
datalist = []
for forecast in forecast_data:
    date = datetime.datetime.fromtimestamp(forecast["dt"]).strftime('%Y-%m-%d')
    
    high_temp = forecast["temp"]["max"]
    low_temp = forecast["temp"]["min"]
    
    print(f"{date}: High: {high_temp}°C, Low: {low_temp}°C")
    datalist.append([date, high_temp, low_temp])

from tkinter import *
window=Tk()






window.title('WEATHER')
window.geometry("900x600")
window.mainloop()
