from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "Your CLIENT_ID"
CLIENT_SECRET = "Your CLIENT_SECRET"

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n"
)
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"
year = date[:4]
print(year)

response = requests.get(BILLBOARD_URL)
response.raise_for_status()
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")
song_1 = soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")

songs = soup.find_all(
    name="h3",
    id="title-of-a-story",
    class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
    "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
    "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
    "u-max-width-230@tablet-only",
)

top_100 = []
top_100.append(song_1.getText().strip("\n\t"))
for song in songs:
    track = song.getText()
    top_100.append(track.strip("\n\t"))


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Username",
    )
)

user_data = sp.current_user()
user_id = user_data["id"]
print(user_id)

URIs = []

for song in top_100:
    track_data = sp.search(
        q=f"{song} year:{year}",
        type="track",
    )
    try:
        song_uri = track_data["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} doesn't exist on spotify")
    else:
        URIs.append(song_uri)

new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100 Hits!",
    description=f"Billboard Hot 100 songs for the week of {date}",
    public=False,
)

sp.playlist_add_items(playlist_id=new_playlist["id"], items=URIs)
