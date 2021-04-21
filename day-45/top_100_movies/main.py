from bs4 import BeautifulSoup
import requests

url = "http://news.tabonline.co.za/2020-Full-Results?fname=TURFFONTEIN%20STANDSIDE@31.12.2020.xml"
response = requests.get(url=url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find_all("table")[1]
print(table)
# gallery = soup.find("div", {"class": "gallery"})

# movies = []
# for item in gallery.find_all("h3"):
#     movies.append(item.text)
    
# movies[-1] = f"1) {movies[-1]}"
# movies[movies.index("Trainspotting")] = "49) Trainspotting"
# movies[movies.index("2) The Princess Bride")] = "93) The Princess Bride"



# movies = soup.find_all(name="h3", class_="title")
# all_movies = [movie.text for movie in movies]

# #reversing list
# data = all_movies[::-1]
# data[0] = f"1) {data[0]}"
# print(data)

# with open("top100_movies.csv", "w") as f:
#     for movie in data:
#         f.write(f"{movie}\n")