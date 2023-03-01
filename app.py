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
        id = data_movies["items"][(499-random)]
    else:
        id = data_shows["items"][random]
    return id

score = 0
highscore = 0

score2 = 1


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/rating")
def index():
    if score == 1:
        return right
    else:
        left = get_random_id()
        right = get_random_id()
        left_title = left["title"]
        right_title = right["title"]
        left_poster = left["image"]
        right_poster = right["image"]
        left_rating = left["imDbRating"]
        right_rating = right["imDbRating"]
        return render_template("index.html", left_title=left_title, right_title=right_title, left_poster=left_poster, right_poster=right_poster, score2=score2)


@app.route("/rating/<score2>/<id>")
def id(score2, id):
    global score
    score += 1
    score2 = int(score2)
    score2 += 1
    if score == 1:
        left = index()
        left = index()
        left_title = left["title"]
        left_poster = left["image"]
        left_rating = left["imDbRating"]
    else:
        left_title = right_title
        left_poster = right_poster
        left_rating = right_rating
    right = get_random_id()
    right_title = right["title"]
    right_poster = right["image"]
    right_rating = right["imDbRating"]
    return render_template("index.html", left_title=left_title, left_poster=left_poster, right_title=right_title, right_poster=right_poster, score2=score2)


@app.route("/tap")
def tap():
    pass

app.run(debug=True)