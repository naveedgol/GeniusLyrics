import requests

def extract_token():
    token = open("API_token.txt", "r")
    return token.read()


# def lyric_scraper(url):


def search(song, artist):
    headers = {"Authorization": "Bearer " + extract_token()}
    search_url = 'http://api.genius.com/search'
    search_data = {'q': song + " " + artist}
    search_results = requests.get(search_url, params=search_data, headers=headers).json()

    for match in search_results["response"]["hits"]:
        if artist == match["result"]["primary_artist"]["name"]:
            # print(match["result"]["url"])
            #lyric_scraper(match["result"]["url"])
            break

search("Antidote", "Travis Scott")