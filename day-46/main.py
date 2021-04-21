#%%
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
print(date)


url = f"https://www.billboard.com/charts/hot-100/{date}"

page = requests.get(url=url)
soup = BeautifulSoup(page.content, "html.parser")

songs = [song.text for song in soup.find_all(class_="chart-element__information__song")]

client_id = "a754d747d187497d8b8caf58e22ac5c7"
clieent_secret = "435721261ede47d4bbb35ced86b8d87a"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a754d747d187497d8b8caf58e22ac5c7",
                                               client_secret="435721261ede47d4bbb35ced86b8d87a",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))
# %%
