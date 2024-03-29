from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class ProductsPage(Base_page):
    RESULTS_TITLE = (By.XPATH, "//a[@class='line-item-title main-product-title']")
    VEZI_DETALII_COS_BTN = (By.XPATH, "//i[@class='em em-cart2 navbar-icon']")
    ADD_TO_CART = (By.XPATH, '//div[@data-pnk="D07R8RMBM"]//button')
    ACCEPT_COOKIES_BUTTON = (By.XPATH,'//button[@class="btn btn-primary js-accept gtm_h76e8zjgoo btn-block"]')

    def add_to_cart(self):
        self.chrome.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.chrome.find_element(*self.ADD_TO_CART).click()

    def click_vezi_detalii_cos(self):
        self.chrome.find_element(*self.VEZI_DETALII_COS_BTN).click()

    def verify_results_contain_text(self, text):
        title_list = self.chrome.find_elements(*self.RESULTS_TITLE)
        for i in range(5):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')


