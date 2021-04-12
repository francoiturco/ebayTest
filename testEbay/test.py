import unittest
from selenium import webdriver
import time
from page_objects.indexPage import index
from page_objects.itemsPage import items

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('testEbay/driver/chromedriver.exe')
        self.driver.get('https://www.ebay.com/')
        self.index = index(self.driver)
        self.items = items(self.driver)

    def test_ebay(self):
        self.index.search_item('shoes')
        self.items.selec_brand()
        self.items.selec_size()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()