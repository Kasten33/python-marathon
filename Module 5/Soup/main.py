from bs4 import BeautifulSoup
import requests

response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movieTitles = [movie.getText() for movie in movies]


with open("movies.txt", mode="w", encoding="utf-8") as file:
    for n in range(len(movieTitles) -1, -1, -1):
        file.write(f"{movieTitles[n]}\n")
