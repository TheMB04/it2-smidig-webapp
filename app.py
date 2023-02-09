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


@app.route("/")
def index():
    navn = "Higher or Lower"
    left_random = randint(0, 499)
    right_random = randint(0, 499)

    if left_random >= 250:
        left = data_movies["items"][(499-left_random)]["title"]
    else:
        left = data_shows["items"][left_random]["title"]

    if right_random >= 250:
        right = data_movies["items"][(499-right_random)]["title"]
    else:
        right = data_shows["items"][right_random]["title"]
    return render_template("index.html", navn=navn, left=left, right=right)

app.run(debug=True)