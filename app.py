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

@app.route("/play/<game>")
def index(game):
    try:
        global right_g
        global left_rating_g
        global right_rating_g

        left = get_random_id()
        right = get_random_id()
        
        right_g = right
        left_title = left["title"]
        right_title = right["title"]
        left_poster = left["image"]
        right_poster = right["image"]

        if game == "rating":
            left_rating = left["imDbRating"]
            left_rating_g = left_rating
            right_rating = right["imDbRating"]
            right_rating_g = right_rating
            name = "Which is rated higher?"
        elif game == "popularity":
            left_rating = left["imDbRatingCount"]
            left_rating_g = left_rating
            right_rating = right["imDbRatingCount"]
            right_rating_g = right_rating
            name = "Which is more popular?"
        else:
            left_rating = left["year"]
            left_rating_g = left_rating
            right_rating = right["year"]
            right_rating_g = right_rating
            name = "Which is the newer release?"

        return render_template("index.html", left_title=left_title, right_title=right_title, left_poster=left_poster, right_poster=right_poster, score=score, left_rating=left_rating, highscore=highscore, game=game, name=name)
    except:
        return render_template("error.html")


@app.route("/play/<game>/<score>/<id>")
def id(game, score, id):
    try: 
        global left_rating_g
        global right_rating_g
        global right_g
        global highscore
        highscore = int(highscore)
        score = int(score)

        if right_rating_g > left_rating_g and id == "left":
            random_id = get_random_id()
            background = random_id["image"]
            return render_template("tap.html", highscore=highscore, score=score, background=background, game=game)
        elif right_rating_g < left_rating_g and id == "right":
            random_id = get_random_id()
            background = random_id["image"]
            return render_template("tap.html", highscore=highscore, score=score, background=background, game=game)
        else:
            score += 1
            if score > highscore:
                highscore = score

            left = right_g
            left_title = left["title"]
            left_poster = left["image"]
            

            right = get_random_id()
            right_g = right
            right_title = right["title"]
            right_poster = right["image"]

            if game == "rating":
                left_rating = left["imDbRating"]
                left_rating_g = left_rating
                right_rating = right["imDbRating"]
                right_rating_g = right_rating
                name = "Which is rated higher?"
            elif game == "popularity":
                left_rating = left["imDbRatingCount"]
                left_rating_g = left_rating
                right_rating = right["imDbRatingCount"]
                right_rating_g = right_rating
                name = "Which is more popular?"
            else:
                left_rating = left["year"]
                left_rating_g = left_rating
                right_rating = right["year"]
                right_rating_g = right_rating
                name = "Which is the newer release?"
            
            return render_template("index.html", left_title=left_title, left_poster=left_poster, right_title=right_title, right_poster=right_poster, score=score, left_rating=left_rating, highscore=highscore, game=game, name=name)
    except:
        return render_template("error.html")

app.run(debug=True)