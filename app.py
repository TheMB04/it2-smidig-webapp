from flask import Flask, render_template
import requests as req
import geocoder as geo
from random import randint


app = Flask(__name__)

url_shows = "https://imdb-api.com/en/API/Top250TVs/k_u4wphtij"
resultat_shows = req.get(url_shows, headers = { 'User-agent': 'MB' })
data_shows = resultat_shows.json()

url_movies = "https://imdb-api.com/en/API/Top250Movies/k_u4wphtij"
resultat_movies = req.get(url_movies, headers = { 'User-agent': 'MB' })
data_movies = resultat_movies.json()

left_random = randint(0, 499)



@app.route("/")
def index():
    navn = "Higher or Lower"
    left = 
    right = data_movies["items"][0]["title"]
    return render_template("index.html", navn=navn, left=left, right=right)

app.run(debug=True)