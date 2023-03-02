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

right_g = 0
right_rating_g = 0
left_rating_g = 0


@app.route("/")
def home():
    try:
        random_id = get_random_id()
        background = random_id["image"]
        return render_template("home.html", background=background)
    except:
        return render_template("error.html")

@app.route("/rating")
def index():
    global right_g
    global left_rating_g
    global right_rating_g

    try:
        left = get_random_id()
        right = get_random_id()
        
        right_g = right
        left_title = left["title"]
        right_title = right["title"]
        left_poster = left["image"]
        right_poster = right["image"]
        left_rating = left["imDbRating"]
        left_rating_g = left_rating
        right_rating = right["imDbRating"]
        right_rating_g = right_rating

        return render_template("index.html", left_title=left_title, right_title=right_title, left_poster=left_poster, right_poster=right_poster, score=score, left_rating=left_rating, highscore=highscore)
    except:
        return render_template("error.html")


@app.route("/rating/<score>/<id>")
def id(score, id):
    global left_rating_g
    global right_rating_g
    global right_g
    global highscore
    highscore = int(highscore)
    score = int(score)
    try:       
        if right_rating_g > left_rating_g and id == "left":
            if score > highscore:
                highscore = score
            random_id = get_random_id()
            background = random_id["image"]
            return render_template("tap.html", highscore=highscore, score=score, background=background)
        elif right_rating_g < left_rating_g and id == "right":
            if score > highscore:
                highscore = score
            random_id = get_random_id()
            background = random_id["image"]
            return render_template("tap.html", highscore=highscore, score=score, background=background)
        else:
            score += 1
            if score > highscore:
                highscore = score

            left = right_g
            left_title = left["title"]
            left_poster = left["image"]
            left_rating = left["imDbRating"]
            left_rating_g = left_rating

            right = get_random_id()
            right_g = right
            right_title = right["title"]
            right_poster = right["image"]
            right_rating = right["imDbRating"]
            right_rating_g = right_rating

            return render_template("index.html", left_title=left_title, left_poster=left_poster, right_title=right_title, right_poster=right_poster, score=score, left_rating=left_rating, highscore=highscore)
    except:
        return render_template("error.html")

app.run(debug=True)