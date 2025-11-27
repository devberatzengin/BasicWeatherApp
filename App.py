from flask import Flask, request, jsonify, render_template # render_template eklenmeli
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "YOUR_APİ_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def ana_sayfa():
    return render_template('index.html') 


@app.route('/api/hava-durumu')
def hava_durumu_al():
    city = request.args.get('sehir')

    if not city:
        return jsonify({'hata': 'Lütfen bir şehir adı girin.'}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'tr'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get('cod') == 404:
             return jsonify({'hata': f'{city} için hava durumu bilgisi bulunamadı.'}), 404

        hava_bilgisi = {
            'sehir': data['name'],
            'sicaklik': data['main']['temp'],
            'hissedilen': data['main']['feels_like'],
            'aciklama': data['weather'][0]['description'].capitalize(),
            'nem': data['main']['humidity'],
        }

        return jsonify(hava_bilgisi)

    except requests.exceptions.RequestException as e:
        return jsonify({'hata': f'Harici API bağlantı hatası: {e}'}), 500
    except Exception:
        return jsonify({'hata': 'Sunucu tarafında beklenmeyen bir hata oluştu.'}), 500

if __name__ == '__main__':
    app.run(debug=True)