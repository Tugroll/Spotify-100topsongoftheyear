import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
the_Date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")
URL = "https://www.billboard.com/charts/hot-100/"+the_Date

class SoupManager:
    def __init__(self):
        self.response = requests.get(url=URL, headers=header)
        self.soup = BeautifulSoup(self.response.text,"html.parser")


    def scraping_songs_as_list(self):
        all_songs = [songs.getText().strip() for songs in self.soup.select("li ul li h3")]
        return all_songs