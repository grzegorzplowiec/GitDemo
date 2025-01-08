from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    cards_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a.btn-primary")

    def __init__(self, driver):
        self.driver = driver

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.cards_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def check_out_items(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
