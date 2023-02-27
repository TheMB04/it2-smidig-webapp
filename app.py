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
def home():
    pass


@app.route("/0")
def index():
    #left = get_random_title()
    #right = get_random_title()
    #left_poster = get_poster(left)
    #right_poster = get_poster(right)
    left = "The Dark Knight"
    right = "The Wolf of Wall Street"
    left_poster = "/static/test_bilder/The Dark Knight.jpg"
    right_poster = "/static/test_bilder/The Wolf of Wall Street.jpg"
    return render_template("index.html", left=left, right=right, left_poster=left_poster, right_poster=right_poster)


@app.route("/id")
def id():
    left = right
    left_poster = right_poster
    right = get_random_title()
    right_poster = get_poster(right)
    return render_template("index.html", left=left, left_poster=left_poster, right=right, right_poster=right_poster)


@app.route("/tap")
def tap():
    pass

app.run(debug=True)