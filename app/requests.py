from app import app
import urllib.request,json
from app.models import Sources, Articles

#getting api key
api_key = None
#getting the news base url
base_url = None


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = "https://newsapi.org/v2/everything?q=kenya&from=2022-05-03&to=2022-05-01&sortBy=popularity&language=en&apikey=a3d94bd7e332493fab43f0c5ad7de4ea"
    

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')
        url = news_item.get('url')

        

        if urlToImage:
            news_object = Articles(author, title, description,content,url, publishedAt,urlToImage)
            news_results.append(news_object)

    return news_results

def get_news_sources():
    '''
    Function that gets the json response to our url request
    '''
    
    get_sources_url = "https://newsapi.org/v2/sources?category=general&language=en&apikey=a3d94bd7e332493fab43f0c5ad7de4ea"

    with urllib.request.urlopen(get_sources_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results_sources(news_results_list)


    return news_results



def process_results_sources(source_list):
    '''
    Function that processes the source list result and transform them to a list of Objects
    '''
    source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Sources(
             name, description, url, category, language)
        source_results.append(source_object)

    return source_results