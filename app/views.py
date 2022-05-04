from flask import render_template

from app.models import Sources, Articles
from .main import main
from .requests import get_news, get_news_sources

@main.route('/')
@main.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    Article = get_news()
    Source = get_news_sources()
    return render_template("index.html",Source = Source, Article = Article)