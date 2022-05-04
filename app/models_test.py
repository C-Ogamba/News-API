import unittest
from models import Articles
from models import Sources


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles(12,'Python','https://s.yimg.com/os/creatr-uploaded-images/2022-01/11d8ecc0-8054-11ec-b7fb-dadff007f52b','Spotify is the leading music streaming service','https://lifehacker.com/the-quickest-way-to-cancel-spotify-premium-and-delete-y-1848452121','us','2022-01-31T18:00:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles)) 

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(
            12, 'Python', 'A thrilling new story', '/khsj//ha27hbs', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

if __name__ == '__main__':
    unittest.main()