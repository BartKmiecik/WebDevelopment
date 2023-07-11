import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

import requests
from bs4 import BeautifulSoup

# date = input('What day you want to go back in time? YYYY-MM-DD')
date = '1992-04-21'
url = f'https://www.billboard.com/charts/hot-100/{date}'
request = requests.get(url=url)

soup = BeautifulSoup(request.text, 'html.parser')
titles = soup.select('ul li ul li h3', class_='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021'
                                              ' lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max'
                                              ' a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')
# for title in titles:
#     print(title.text.strip())

id = '2d3a5c6d56c74e3295a3c04fb6156ce5'
secret = '856c0f618f684ee1a0a22175b4506769'
print('Finished with titles')


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri="https://example.com/",
                                               scope='playlist-modify-private'))

username = sp.current_user()['id']
playlist = sp.user_playlist_create(username,'1992-04-21_Billboard_100', public=False, collaborative= False, description='Test')
songs_uri = []

# for track in titles:
#     result = sp.search(q=f'track:{track.text.strip()} year:1992', type='track')
#     uri = result['tracks']['items'][0]['uri']
#     songs_uri.append(uri)
#     sp.playlist_add_items(playlist['id'], uri)

for track in titles:
    result = sp.search(q=f'track:{track.text.strip()} year:1992', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uri.append(uri)
    except:
        print(f'Can\'t find the song: {track.text.strip()}')

sp.playlist_add_items(playlist['id'], songs_uri)

