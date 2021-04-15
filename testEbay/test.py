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
        self.driver = webdriver.Chrome('testEbay/driver/chromedriver.exe', chrome_options = option)
        self.driver.get('https://www.ebay.com/')
        self.driver.implicitly_wait(10)
        self.index = index(self.driver)
        self.items = items(self.driver)

    @unittest.skip('bla')
    def test_1search_bikes(self):
        self.index.search_item('bikes')
        self.assertTrue(self.items.item_find() == 'bikes')

    @unittest.skip('bla')
    def test_2search_brand(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.assertTrue(self.items.assert_brand, 'SCOTT')

    @unittest.skip('bla')
    def test_3search_size(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.assertTrue(self.items.assert_size, '29 pulgadas')

    @unittest.skip('bla')
    def test_4print_quantities(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()

    @unittest.skip('bla')
    def test_5order_by_price_ascendant(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()
        self.items.order_by()

    @unittest.skip('bla')
    def test_6assert_first_five(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()
        self.items.order_by()
        self.items.assert_prices(5)

    @unittest.skip('bla')
    def test_7print_items(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()
        self.items.order_by()
        self.items.assert_prices(5)
        self.items.print(5)

    @unittest.skip('bla')
    def test_8print_titles(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()
        self.items.order_by()
        self.items.assert_prices(5)
        self.items.print(5)
        print('-------------------------------------------------------------------')
        self.items.order_title(5)

    #@unittest.skip('bla')
    def test_9print_prices(self):
        self.index.search_item('bikes')
        self.items.selec_brand('SCOTT')
        self.items.selec_size(14)
        self.items.print_quantity()
        print(' ')
        self.items.order_by()
        self.items.assert_prices(5)
        self.items.print(5)
        print(' ')
        self.items.order_title(5)
        print(' ')
        self.items.order_price(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()