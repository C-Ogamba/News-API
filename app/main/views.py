from flask import render_template
from . import main
from ..requests import get_news

@main.route('/')
def index():

    news = get_news()
    title = "CURRENTNEWS"
    return render_template("index.html",title = title, articles = news)