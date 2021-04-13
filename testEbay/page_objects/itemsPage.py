from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class items:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.size = (By.XPATH, '//span[@class="cbx x-refine__multi-select-cbx"]')
        self.see_all = (By.XPATH, '//span[contains(text(),"ver todo")]')
        self.brand = (By.XPATH, '//span[contains(text(),"SCOTT")]')
        self.apply = (By.XPATH, '//button[@aria-label="Aplicar"]')
        self.quantity_results = (By.XPATH, '//span[@class="BOLD"]')
        self.select = (By.XPATH, '//span[@class="expand-btn__cell"]')
        self.sort = (By.XPATH, '//a[@_sp="p2351460.m4116.l5869.c5"]')
        self.titles = (By.XPATH, '//a[@class="s-item__link"]')
        self.prices = (By.XPATH, '//span[@class="s-item__price"]')

    def selec_brand(self, brand):
        self.driver.find_elements(*self.see_all)[3].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.brand)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apply)).click()

    def selec_size(self, number):
        self.driver.find_elements(*self.size)[number].click()

    def print_quantity(self):
        print(self.driver.find_elements(*self.quantity_results)[11].text)

    def order_by(self):
        self.driver.find_elements(*self.select)[3].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sort)).click()

    def print(self, number):
        for i in range(number):
            print(self.driver.find_elements(*self.titles)[i].text)
            print(self.driver.find_elements(*self.prices)[i].text)

    def order_title(self, number):
        array_title = []
        for i in range(number):
            array_title.append(self.driver.find_elements(*self.titles)[i].text)
        array_title_ascend = sorted(array_title)
        print(array_title_ascend)

    def order_price(self, number):
        array_price = []
        for i in range(number):
            array_price.append(self.driver.find_elements(*self.prices)[i].text)
        array_price_descendt = sorted(array_price, reverse=True)
        print(array_price_descendt)