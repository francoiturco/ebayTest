from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class items:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.size = (By.XPATH, '//span[@class="cbx x-refine__multi-select-cbx"]')
        self.see_all = (By.XPATH, '//span[contains(text(),"ver todo")]')
        self.brand = (By.XPATH, '//span[contains(text(),"PUMA")]')
        self.apply = (By.XPATH, '//button[@aria-label="Aplicar"]')
        self.quantity_results = (By.XPATH, '//span[@class="BOLD"]')
        self.select = (By.XPATH, '//span[@class="expand-btn__cell"]')
        self.sort = (By.XPATH, '//a[@_sp="p2351460.m4116.l5869.c5"]')
        self.titles = (By.XPATH, '//a[@class="s-item__link"]')
        self.prices = (By.XPATH, '//span[@class="s-item__price"]')

    def selec_brand(self):
        self.driver.find_elements(*self.see_all)[1].click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.brand)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.apply)).click()

    def selec_size(self):
        self.driver.find_elements(*self.size)[4].click()

    def print_quantity(self):
        print(self.driver.find_elements(*self.quantity_results)[13].text)

    def order_by(self):
        self.driver.find_elements(*self.select)[3].click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sort)).click()

    def print(self, number):
        for i in range(number):
            print(self.driver.find_elements(*self.titles)[i].text)
            print(self.driver.find_elements(*self.prices)[i].text)
