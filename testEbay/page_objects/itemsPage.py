import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class items:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.size = (By.XPATH, '//span[@class="cbx x-refine__multi-select-cbx"]')
        self.see_all = (By.XPATH, '//span[contains(text(),"ver todo")]')
        self.brand = (By.XPATH, '//span[contains(text(),"SCOTT")]')
        self.brand_text = (By.XPATH, '//a[@_sp="p2351460.m43632.l8567"]')
        self.size_text = (By.XPATH, '//a[@_sp="p2351460.m43632.l8567"]')
        self.apply = (By.XPATH, '//button[@aria-label="Aplicar"]')
        self.quantity_results = (By.XPATH, '//span[@class="BOLD"]')
        self.select = (By.XPATH, '//span[@class="expand-btn__cell"]')
        self.sort = (By.XPATH, '//a[@_sp="p2351460.m4116.l5869.c5"]')
        self.titles = (By.XPATH, '//a[@class="s-item__link"]')
        self.prices = (By.XPATH, '//span[@class="s-item__price"]')

    def item_find(self):
        return self.driver.find_elements(*self.quantity_results)[12].text

    def selec_brand(self, brand):
        self.driver.find_elements(*self.see_all)[3].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.brand)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apply)).click()
    
    def assert_brand(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.brand_text)).text

    def selec_size(self, number):
        self.driver.find_elements(*self.size)[number].click()

    def assert_size(self):
        return self.driver.find_elements(*self.size_text)[2].text

    def print_quantity(self):
        print(self.driver.find_elements(*self.quantity_results)[11].text)

    def order_by(self):
        self.driver.find_elements(*self.select)[3].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sort)).click()

    def assert_prices(self, number):
        array_price = []
        for i in range(number):
            array_price.append(self.driver.find_elements(*self.prices)[i].text)
        prices1 = []
        prices2 = []
        for i in range(len(array_price)):
            prices1.append(array_price[i].replace(" ", ""))
            prices2.append(prices1[i].strip('USD'))
        prices3 = [float(x) for x in prices2]
        array = sorted(prices3)
        tc = unittest.TestCase('__init__')
        tc.assertTrue (array[0] <= array[1] <= array[2] <= array[3] <= array[4])
    
    def print(self, number):
        prices1 = []
        prices2 = []
        for i in range(number):
            prices1.append((self.driver.find_elements(*self.prices)[i].text).replace(" ", ""))
            prices2.append(prices1[i].strip('USD'))
        prices3 = [float(x) for x in prices2]
        for i in range(number):
            print(self.driver.find_elements(*self.titles)[i].text)
            #print(self.driver.find_elements(*self.prices)
            print(prices3[i])

    def order_title(self, number):
        array_title = []
        for i in range(number):
            array_title.append(self.driver.find_elements(*self.titles)[i].text)
        array_title_ascend = sorted(array_title)
        for i in range(number):
            print(array_title_ascend[i])

    def order_price(self, number):
        array_price = []
        for i in range(number):
            array_price.append(self.driver.find_elements(*self.prices)[i].text)
        prices1 = []
        prices2 = []
        for i in range(len(array_price)):
            prices1.append(array_price[i].replace(" ", ""))
            prices2.append(prices1[i].strip('USD'))
        prices3 = [float(x) for x in prices2]
        array_price_descendt = sorted(prices3, reverse=True)
        for i in range(number):
            print(array_price_descendt[i])
