import configparser
import unittest

from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.url = self.config.get('ABCMouse', 'url')
        self.email = self.config.get('ABCMouse', 'email')

        #options = Options()
        #options.add_argument("--headless=new")
        #self.driver = webdriver.Chrome(options=options)

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
