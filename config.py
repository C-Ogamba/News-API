class Config:
    '''
    General configuration parent class
    '''
    get_news_url = "https://newsapi.org/v2/everything?q=kenya&from=2022-05-03&to=2022-05-01&sortBy=popularity&language=en&apikey='a3d94bd7e332493fab43f0c5ad7de4ea'"
    get_sources_url = "https://newsapi.org/v2/everything?q=us&from=2022-05-03&to=2021-05-01&sortBy=popularity&language=en&apikey='a3d94bd7e332493fab43f0c5ad7de4ea'"



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True