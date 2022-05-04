from flask import render_template

from app.models import Sources
from . import main
from ..requests import get_news, get_news_sources

@main.route('/')
@main.route('/index')
def index():

    Articles = get_news()
    Sources = get_news_sources()
    return render_template("index.html",Sources = Sources, Articles = Articles)