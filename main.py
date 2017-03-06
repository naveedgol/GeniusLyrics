import requests
import sys
from bs4 import BeautifulSoup

#extract custom genius api token from txt file, obtained from https://genius.com/api-clients
def extract_token():
    token = open("API_token.txt", "r")
    return token.read()

def txt_export(lyrics):
    lyrics_file = open("lyrics.txt", "w")
    lyrics_file.write(lyrics)

#Genius api lacks getting lyrics, manually scrape results
def lyric_scraper(url):
    source = requests.get(url).text
    source_soup = BeautifulSoup(source, "html.parser")
    lyrics = source_soup.find("lyrics")
    # print(lyrics.get_text().strip())
    return lyrics.get_text().strip()

#Search Genius for a song with corresponding artist
def search(artist, song):
    headers = {"Authorization": "Bearer " + extract_token()}
    search_url = 'http://api.genius.com/search'
    search_data = {'q': song + " " + artist}
    search_results = requests.get(search_url, params=search_data, headers=headers).json()

    for match in search_results["response"]["hits"]:
        if artist == match["result"]["primary_artist"]["name"]:
            # print(match["result"]["url"])
            return match["result"]["url"]

    #indicate a fail to fetch

def export_lyrics(artist, song):
    song_url = search(artist, song)
    song_lyrics = lyric_scraper(song_url)
    txt_export(song_lyrics)

export_lyrics("Drake", "Still Here")