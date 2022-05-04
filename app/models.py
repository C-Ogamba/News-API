class Sources:
    """
    Sources class to define sources object
    """

    def __init__(self, name, description, url, category, language):
       
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language


class Articles:
    """
    Articles class to define articles object
    """

    def __init__(self, author, title, description, url, urlToImage, content, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt
       