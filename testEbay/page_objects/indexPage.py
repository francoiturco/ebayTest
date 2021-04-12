from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class index:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.search_bar = (By.ID, 'gh-ac')
        self.search_button = (By.ID, 'gh-btn')

    def search_item(self, item):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.search_bar)).send_keys(item)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.search_button)).click()