import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from main_class import MainClass
from pages.login import Login

@pytest.mark.usefixtures("browser_invocation")

@allure.feature("user login test")
class TestMainScript(MainClass):
    @allure.story("user logging in")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logging(self, browser_invocation):
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless--")a
        # driver = webdriver.Chrome(options=options)
        # driver.implicitly_wait(5)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        login = Login(self.driver, browser_invocation)

        with allure.step("input user name"):
            login.input_name()
            allure.attach("user name input", attachment_type=allure.attachment_type.TEXT)
        login.input_email()
        login.input_password()
        login.click_button()
        login.click_submit()

        wait = WebDriverWait(self.driver,6)
        wait.until(expected_conditions.presence_of_element_located(()))

        # self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(browser_invocation[0])
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(browser_invocation[1])
        # self.driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys(browser_invocation[2])
        # self.driver.find_element(By.ID, 'exampleCheck1').click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        assert self.driver.find_element(By.CSS_SELECTOR, '.alert-success').is_displayed()
        logger = TestMainScript.get_logger(self)
        logger.info("test is successfull")

        time.sleep(5)



