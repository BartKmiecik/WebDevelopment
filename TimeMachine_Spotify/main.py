import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

import requests
from bs4 import BeautifulSoup

# date = input('What day you want to go back in time? YYYY-MM-DD')
# url = f'https://www.billboard.com/charts/hot-100/{date}'
# request = requests.get(url=url)
#
# soup = BeautifulSoup(request.text, 'html.parser')
# titles = soup.select('ul li ul li h3', class_='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021'
#                                               ' lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max'
#                                               ' a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')
# for title in titles:
#     print(title.text.strip())

id = '2d3a5c6d56c74e3295a3c04fb6156ce5'
secret = '856c0f618f684ee1a0a22175b4506769'

# spotipy.oauth2.SpotifyOAuth(id,secret,'www.https://example.com/')

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=id,
#                                                            client_secret=secret))
#
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri="https://example.com/",
                                               scope='playlist-modify-private'))

# print(sp.user_playlists(sp.current_user()))

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = sp.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
