import requests
url="https://api.open-meteo.com/v1/forecast"
params={"latitude":12.97,"longitude":77.59,"current":"temperature_2m,relativehumidity_2m"}
response=requests.get(url,params=params,timeout=15)
if response.status_code==200:
    data=response.json()
    print("weather in Bangalore")
    print("Temperature:",data["current"]["temperature_2m"],"°C")
    print("Humidity:",data["current"]["relativehumidity_2m"],"%")
else:
    print("Error:",response.status_code)