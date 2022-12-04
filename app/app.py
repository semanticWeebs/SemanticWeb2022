from flask import Flask, render_template
from flask import jsonify
from flask import request
import pandas as pd
from utils import subset

app = Flask(__name__)

data_film = pd.read_csv("./data/data_film_preprocesing_data_2.csv")


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/get_films")
def films():
    page = request.args.get("name_cinema", default="")
    year = request.args.get("year", default="")
    year_op = request.args.get("year op", default="=")
    country = request.args.get("country", default="").split("|")

    country = [i.strip() for i in country]
    if len(country[0]) == 0:
        country = ""

    lang = request.args.get("lang", default="").split()
    ganre = request.args.get("ganre", default="").split("|")

    actor = request.args.get("actror", default="").split("|")

    ganre = [i.strip() for i in ganre]
    if len(ganre[0]) == 0:
        ganre = ""

    actor = [i.strip() for i in actor]
    if len(actor[0]) == 0:
        actor = ""
    if len(lang) == 0:
        lang = ""
    if len(country) == 0:
        country = ""
    print(page, year, country, lang, actor)

    global data_film
    data = subset(
        name_film=page,
        year=year,
        year_op=year_op,
        lang=lang,
        actor=actor,
        produser="",
        country=country,
        genre=ganre,
        data=data_film,
    )

    try:
        return data[:100].to_html()
    except:
        return data.to_html()


# if __name__ == "__main__":
#     app.run(host="0.0.0.0")
