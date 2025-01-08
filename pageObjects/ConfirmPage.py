from selenium.webdriver.common.by import By


class ConfirmPage:
    checkout = (By.CSS_SELECTOR, "button.btn-success.btn")
    country = (By.ID, "country")
    country_selected = (By.LINK_TEXT, "Poland")
    agreements = (By.CSS_SELECTOR, "div.checkbox.checkbox-primary")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    confirmation_text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def check_out_items(self):
        return self.driver.find_element(*ConfirmPage.checkout)

    def country_input(self):
        return self.driver.find_element(*ConfirmPage.country)

    def country_select(self):
        return self.driver.find_element(*ConfirmPage.country_selected)

    def agreements_select(self):
        return self.driver.find_element(*ConfirmPage.agreements)

    def purchase_items(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def get_confirmation_text(self):
        return self.driver.find_element(*ConfirmPage.confirmation_text)
