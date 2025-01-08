import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from test_data.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        log = self.get_logger()
        # ID, Xpath, CSSSelector, Classname, name, linkText

        homepage = HomePage(self.driver)
        log.info("first name is "+get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["lastname"])
        homepage.get_password().send_keys("123456")

        homepage.get_checkbox().click()

        # Xpath - //tagname[@attribute='value']
        # CSSSelector - tagname[attribute='value']   , #id , .classname

        # driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

        # Static Dropdown
        self.select_option_by_text(homepage.get_gender_form(), get_data["gender"])

        # dropdown.select_by_index(0)
        # dropdown.select_by_value()

        homepage.get_submit_button().click()

        alert_text = homepage.get_message().text
        assert "Success" in alert_text

        self.driver.refresh()
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
