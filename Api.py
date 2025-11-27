import requests

API_KEY = "YOUR_APİ_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "London"

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric', 
    'lang': 'en' 
}

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status() 
    data = response.json()

    print(data)
    print(f"Şehir: {data['name']}")
    print(f"Sıcaklık: {data['main']['temp']} °C")
    print(f"Açıklama: {data['weather'][0]['description'].capitalize()}")

except requests.exceptions.RequestException as e:
    print(f"Hata oluştu: {e}")
except KeyError:
    print("API yanıtında beklenen veri bulunamadı.")