import requests
from bs4 import BeautifulSoup

#extract custom genius api token from txt file, obtained from https://genius.com/api-clients
def extract_token():
    token = open("API_token.txt", "r")
    return token.read()

# def txt_export(lyrics):

#Genius api lacks getting lyrics, manually scrape results
def lyric_scraper(url):
    source = requests.get(url).text
    source_soup = BeautifulSoup(source, "html.parser")
    lyrics = source_soup.find("lyrics")
    print(lyrics.get_text().strip())
    # txt_export(lyrics.get_text().strip())

#Search Genius for a song with corresponding artist
def search(song, artist):
    headers = {"Authorization": "Bearer " + extract_token()}
    search_url = 'http://api.genius.com/search'
    search_data = {'q': song + " " + artist}
    search_results = requests.get(search_url, params=search_data, headers=headers).json()

    for match in search_results["response"]["hits"]:
        if artist == match["result"]["primary_artist"]["name"]:
            print(match["result"]["url"])
            lyric_scraper(match["result"]["url"])
            return

    #indicate a fail to fetch

search("Antidote", "Travis Scott")