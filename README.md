# Spotify En Çok Dinlenen Sanatçı Analizi ve Karışık Playlist Oluşturucu

Bu proje, Spotify API'sini kullanarak en çok dinlediğiniz sanatçıları analiz eder ve bu sanatçıların popüler şarkılarına dayalı olarak rastgele bir playlist oluşturur.

## Başlangıç

### Gereksinimler

- Python 3.x yüklü olmalı
- Bir Spotify geliştirici hesabı (ücretsiz) ve API kimlik bilgilerine sahip bir Spotify Uygulaması

## Kurulum

1. Bu depoyu klonlayın:

   ```bash
   https://github.com/ugurcomptech/SpotiMix-Top-Tracks-Analysis-Playlist-Creator.git
   cd SpotiMix-Top-Tracks-Analysis-Playlist-Creator
    ```

2. Gerekli paketleri pip ile kurun:
     ```bash
     pip install -r requirements.txt
     ```

## Kullanım

1. **Bir Spotify Uygulaması oluşturun ve API kimlik bilgilerinizi alın:**

   - [Spotify Geliştirici Kontrol Paneli'ne](https://developer.spotify.com/dashboard/applications) gidin.
   - Yeni bir uygulama oluşturun ve Client ID, Client Secret ve Redirect URI bilgilerinizi kaydedin.

2. **Komut satırı argümanları ile betiği çalıştırın:**

   Aşağıdaki komutu çalıştırarak betiği çalıştırın. Parametreleri kendi Spotify API bilgilerinizle doldurun.

   ```bash
   python app.py --client-id SIZIN_CLIENT_ID --client-secret SIZIN_CLIENT_SECRET --redirect-uri SIZIN_REDIRECT_URI --username SIZIN_SPOTIFY_KULLANICI_ADI --limit 20
   ```

3. SIZIN_CLIENT_ID, SIZIN_CLIENT_SECRET, SIZIN_REDIRECT_URI, SIZIN_SPOTIFY_KULLANICI_ADI yerine kendi bilgilerinizi girin.

4. Ayrıca, --limit parametresini kullanarak playlistteki maksimum şarkı sayısını ayarlayabilirsiniz.

5. Betik, en çok dinlediğiniz sanatçıları analiz edecek ve belirtilen şarkı sayısı ile rastgele bir playlist oluşturacaktır.


## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.
