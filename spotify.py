import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import argparse

# Argümanları ayrıştırın
parser = argparse.ArgumentParser(description='Otomatik Playlist Analiz ve Oluşturma')
parser.add_argument('--client-id', required=True, help='Spotify API Client ID')
parser.add_argument('--client-secret', required=True, help='Spotify API Client Secret')
parser.add_argument('--redirect-uri', required=True, help='Spotify API Redirect URI')
parser.add_argument('--username', required=True, help='Spotify Username')
parser.add_argument('--limit', type=int, required=True, help='Maksimum şarkı sayısı (max: 30)')
args = parser.parse_args()

# Spotify API'ye erişim için oturum açma işlemi (kullanıcı girişi)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=args.client_id, client_secret=args.client_secret, redirect_uri=args.redirect_uri, scope='user-library-read user-top-read playlist-modify-public'))

# Kullanıcının en çok dinlediği 10 sanatçıları al
top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')

# Tüm sanatçıların popüler şarkılarını toplayacak liste
all_artist_tracks = []

# Sanatçıların popüler şarkılarını al
for artist in top_artists['items']:
    artist_id = artist['id']
    artist_tracks = sp.artist_top_tracks(artist_id, country='TR')
    all_artist_tracks.extend(artist_tracks['tracks'])

# Rastgele karışık bir şekilde şarkıları seçin
random.shuffle(all_artist_tracks)
selected_tracks = all_artist_tracks[:args.limit]  # Kullanıcının belirlediği şarkı sayısı sınırlaması

# Kullanıcının playlistini oluştur
playlist_name = "En Çok Dinlenen Sanatçıların Karışık Şarkıları"
playlist_description = "En çok dinlenen 10 sanatçının rastgele karışık şarkıları"

playlist = sp.user_playlist_create(args.username, playlist_name, public=True, description=playlist_description)
playlist_id = playlist['id']

# Şarkıları playliste ekle
track_uris = [track['uri'] for track in selected_tracks]
sp.playlist_add_items(playlist_id, track_uris)

print(f"{playlist_name} adlı playlist oluşturuldu.")
