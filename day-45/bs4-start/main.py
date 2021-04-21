from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("a", {"class": "storylink"})
titles = soup.find_all("a", class_="storylink")
for title in titles:
    # print(title.text)
    pass


article_text = soup.find("a", {"class": "storylink"})
article_link = article_text.get("href")
article_upvote = soup.find("span", "score" ).text
print(article_text.text)
print(article_link)
print(article_upvote)


















# with open("website.html", "r", encoding="utf-8") as df:
#     data = df.read()

# soup = BeautifulSoup(data, "html.parser")

# anchor_tags =soup.findAll("a")

# for tag in anchor_tags:
#     # print(tag.get("href"))
#     pass


# company_url = soup.select_one("p a")

# selecting_class = soup.select_one (".heading")
# print(selecting_class.getText())
# print(selecting_class.string)
# print(selecting_class.text)