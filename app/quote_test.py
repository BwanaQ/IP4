import unittest
from models import quote
Quote = quote.Quote


class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(12, 'Title', 'Python Must Be Crazy',
                               'Body goes Here...', 'test Author', '27', '27/11/2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quote))


if __name__ == '__main__':
    unittest.main()
