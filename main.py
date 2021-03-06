import requests
import sys
from bs4 import BeautifulSoup

#extract custom genius api token from txt file, obtained from https://genius.com/api-clients
def extract_token():
    token = open("/Library/iTunes/Scripts/API_token.txt", "r")
    return token.read()

def txt_export(lyrics):
    lyrics_file = open("/Library/iTunes/Scripts/lyrics.txt", "w", encoding='utf-8')
    lyrics_file.write(lyrics)

#Genius api lacks getting lyrics, manually scrape results
def lyric_scraper(url):
    source = requests.get(url).text
    source_soup = BeautifulSoup(source, "html.parser")
    lyrics = source_soup.find("lyrics")
    return lyrics.get_text().strip()

#Search Genius for a song with corresponding artist
def search(artist, song):
    headers = {"Authorization": "Bearer " + extract_token()}
    search_url = 'http://api.genius.com/search'
    search_data = {'q': song + " " + artist}
    search_results = requests.get(search_url, params=search_data, headers=headers).json()

    for match in search_results["response"]["hits"]:
        if artist == match["result"]["primary_artist"]["name"]:
            return match["result"]["url"]

def export_lyrics(artist, song):
    song_url = search(artist, song)
    if song_url:
        song_lyrics = lyric_scraper(song_url)
        txt_export(song_lyrics)
    else:
        txt_export("Lyrics not found")

export_lyrics(sys.argv[1], sys.argv[2])
