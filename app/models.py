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

    def __init__(self, author, title, description, url, url_to_Image, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_Image = url_to_Image
        self.content = content
       