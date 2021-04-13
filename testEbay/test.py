import unittest
from selenium import webdriver
import time
from page_objects.indexPage import index
from page_objects.itemsPage import items
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        #option.add_argument('--headless')
        self.driver = webdriver.Chrome('testEbay/driver/chromedriver.exe', chrome_options=option)
        self.driver.get('https://www.ebay.com/')
        self.driver.implicitly_wait(10)
        self.index = index(self.driver)
        self.items = items(self.driver)

    def test_ebay(self):
        self.index.search_item('bikes')
        self.assertTrue(self.items.item_find() == 'bikes',)
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()
        self.items.order_by()
        self.items.print(5)
        self.items.order_title(3)
        self.items.order_price(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()