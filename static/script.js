const sonucKutusu = document.getElementById('sonuc-kutusu');

function getWeather() {
    const sehirInput = document.getElementById('sehir-input');
    const sehirAdi = sehirInput.value.trim();

    if (sehirAdi === "") {
        sonucKutusu.innerHTML = `<p class="hata">Lütfen sorgulamak için bir şehir adı girin.</p>`;
        return;
    }

    sonucKutusu.innerHTML = `<p>Hava durumu bilgisi yükleniyor...</p>`;

    const URL = `http://127.0.0.1:5000/api/hava-durumu?sehir=${sehirAdi}`;

    fetch(URL)
        .then(response => response.json())
        .then(data => {
            if (data.hata) {
                sonucKutusu.innerHTML = `<p class="hata">Hata: ${data.hata}</p>`;
            } else {
                gosterHavaDurumu(data);
            }
        })
        .catch(error => {
            console.error('İstek sırasında hata oluştu:', error);
            sonucKutusu.innerHTML = `<p class="hata">Bağlantı Hatası: Web servisine ulaşılamıyor (Flask çalışıyor mu?).</p>`;
        });
}


function gosterHavaDurumu(havaVerisi) {
    const html = `
        <h2>${havaVerisi.sehir}</h2>
        <p><strong s-atyle="text-align: center">Sıcaklık:</strong> ${havaVerisi.sicaklik.toFixed(1)} °C</p>
        <p><strong>Hissedilen:</strong> ${havaVerisi.hissedilen.toFixed(1)} °C</p>
        <p><strong>Genel Durum:</strong> ${havaVerisi.aciklama}</p>
        <p><strong>Nem:</strong> %${havaVerisi.nem}</p>
    `;
    sonucKutusu.innerHTML = html;
}