from flask import Flask, render_template
import requests as req
from random import randint
import json


app = Flask(__name__)


fil = open("shows.json", encoding = "utf-8")
data_shows = json.load(fil)
fil.close()


fil2 = open("movies.json", encoding = "utf-8")
data_movies = json.load(fil2)
fil2.close()


#url_shows = "https://imdb-api.com/en/API/Top250TVs/k_u4wphtij"
#resultat_shows = req.get(url_shows, headers = { 'User-agent': 'MB' })
#data_shows = resultat_shows.json()


#url_movies = "https://imdb-api.com/en/API/Top250Movies/k_u4wphtij"
#resultat_movies = req.get(url_movies, headers = { 'User-agent': 'MB' })
#data_movies = resultat_movies.json()


def get_random_id():
    random = randint(0, 499)
    if random >= 250:
        title = data_movies["items"][(499-random)]
    else:
        title = data_shows["items"][random]
    return title


def get_poster(title):
    return title["image"]


#@app.route("/")
def home():
    pass


@app.route("/")
def index():
    left = get_random_id()
    right = get_random_id()
    left_title = left["title"]
    right_title = right["title"]
    left_poster = left["image"]
    right_poster = right["image"]
    #left = "The Dark Knight"
    #right = "The Wolf of Wall Street"
    #left_poster = "/static/test_bilder/The Dark Knight.jpg"
    #right_poster = "/static/test_bilder/The Wolf of Wall Street.jpg"
    return render_template("index.html", left_title=left_title, right_title=right_title, left_poster=left_poster, right_poster=right_poster)


@app.route("/id")
def id():
    left_title = right_title
    left_poster = right_poster
    right = get_random_id()
    right_title = right["title"]
    right_poster = right["image"]
    return render_template("index.html", left_title=left_title, left_poster=left_poster, right_title=right_title, right_poster=right_poster)


@app.route("/tap")
def tap():
    pass

app.run(debug=True)