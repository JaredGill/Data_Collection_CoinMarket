import string
from Scraper import CoinScraper
import unittest
from unittest.mock import patch, Mock, call
import time

class ScraperTestCase(unittest.TestCase):

    #setUP runs before every test
    def setUp(self):
        self.s = CoinScraper()
        #self.coin_data = CoinScraper('https://coinmarketcap.com/currencies/bitcoin/')
        self.url = "https://coinmarketcap.com/"
    
    #tearDown runs after every test
    def tearDown(self):
        self.s.driver.quit()
        #self.coin_data.driver.quit()
        del self.s.driver
        return

    #When using patch to test methods being tested, it should be called in the class where it is used from, not where defined
    #Can mock any method such as time.sleep or send_keys
    #e.g. @patch('selenium.webdriver.remote.webelement.Webelement.send_keys')
    @patch('scraper.CoinScraper.get_links')
    @patch('scraper.CoinScraper.get_image')
    @patch('scraper.CoinScraper.get_text_data')
    def test_data_scrape(self, 
                        mock_get_links: Mock, 
                        mock_get_image: Mock, 
                        mock_get_text_data: Mock):

        #pass 3 to method so it scrapes 3 different coins
        self.s.data_scrape(3)
        mock_get_links.assert_called_once

        #mock_get_image.assert_has_calls(calls=)
        image_call_count = mock_get_image.call_count
        self.assertEqual(image_call_count, 3)

        text_call_count = mock_get_text_data.call_count
        self.assertEqual(text_call_count, 3)
        

    def test_get_links(self):
        #get_links without scrolling only returns first 12 coin links
        links = self.s.get_links()
        #self.s.close_popup()
        #1st and last url, right lenthg and type
        first_url = "https://coinmarketcap.com/currencies/bitcoin/"
        last_url = "https://coinmarketcap.com/currencies/avalanche/"
        length_urls = 13
        self.assertEqual(first_url, links[0])
        #as top 100 crytpos change daily, last url may fail
        self.assertEqual(last_url, links[11])
        self.assertEqual(length_urls, len(links))
        self.assertIsInstance(links, list)
        
    def test_data_scrape(self):
        iterations = self.s.data_scrape(3)
        #self.s.close_popup()
        number_of_coins = 3
        self.assertEqual(number_of_coins, iterations)
        self.assertIsInstance(iterations, int)
    
    def test_get_image(self):
        #Dont want to call several methods to test this, instead give url to specific page
        self.s.driver.get('https://coinmarketcap.com/currencies/bitcoin/')
        img = self.s.get_image()
        #img = self.coin_data.get_image()
        url = 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'
        name = 'BTC'
        self.assertEqual(url, img[0])
        self.assertEqual(name, img[1])

    def test_get_text_data(self):
        self.s.driver.get('https://coinmarketcap.com/currencies/bitcoin/')
        data = self.s.get_text_data()
        #data = self.coin_data.get_text_data()
        time.sleep(2)
        id_match = "Bitcoin (BTC)"
        self.assertEqual(id_match, data[1])
        self.assertIsInstance(data[1], str)


unittest.main(argv=[''], verbosity=2, exit=False)
#verbosity denotes detail of pass/fail
#exit = false doesnt reset ipkernal


#python-m unittest name