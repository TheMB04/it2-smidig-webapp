from flask import Flask, render_template
import requests as req
from random import randint


app = Flask(__name__)

url_shows = "https://imdb-api.com/en/API/Top250TVs/k_u4wphtij"
resultat_shows = req.get(url_shows, headers = { 'User-agent': 'MB' })
data_shows = resultat_shows.json()

url_movies = "https://imdb-api.com/en/API/Top250Movies/k_u4wphtij"
resultat_movies = req.get(url_movies, headers = { 'User-agent': 'MB' })
data_movies = resultat_movies.json()

def get_random_title():
    random = randint(0, 499)

    if random >= 250:
        title = data_movies["items"][(499-random)]["title"]
    else:
        title = data_shows["items"][random]["title"]

    return title


def get_poster(title):
    url_poster = f"https://imdb-api.com/en/API/SearchSeries/k_u4wphtij/{title}"
    resultat_poster = req.get(url_poster, headers = { 'User-agent': 'MB' })
    data_poster = resultat_poster.json()
    return data_poster["results"][0]["image"]


@app.route("/")
def index():
    navn = "Higher or Lower"
    left = get_random_title()
    right = get_random_title()
    return render_template("index.html", navn=navn, left=left, right=right)

app.run(debug=True)