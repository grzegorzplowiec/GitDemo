from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        # xPath:  //a[contains(@href,'shop')]    CSSSelector:  a[href*='shop']
        checkout_page = home_page.shop_items()
        log.info("getting all the card titles")
        cards = checkout_page.get_card_titles()

        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkout_page.get_card_footer()[i].click()

        # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirm_page = checkout_page.check_out_items()

        confirm_page.check_out_items().click()
        confirm_page.country_input().send_keys("Po")
        log.info("Entering country name as Po")
        self.verify_link_presence("Poland")
        confirm_page.country_select().click()
        confirm_page.agreements_select().click()
        confirm_page.purchase_items().click()
        confirmation_text = confirm_page.get_confirmation_text().text
        log.info("Text received from application is "+confirmation_text)
        assert "Success! Tyyhank you! Your order will be delivered in next few weeks :-)." in confirmation_text, "Wrong confirmation text on the screen"
