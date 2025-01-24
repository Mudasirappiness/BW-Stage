import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
import logging
import os
from PIL import Image
from send_mail import send_email
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup","user_account","otp_config_for_service")
class Test_coa_filed:


    def test_coa(self,caplog):

        """"Clicking on the hamburger menu"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the hamburger menu")
                hamburger_menu = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//*[@id='html']/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")))
                hamburger_menu.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the hamburger menu- Testcase 1.1 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the my account page"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the my account page")
                my_account = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()=' My Account'])[1]")))
                my_account.click()
                time.sleep(3)
                logging.info("Successfully Clicked on the my account page- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll down till the page visible"""
        with caplog.at_level(logging.INFO):
            try:

                element = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "//div[text()='Firm Details']")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)
                logging.info("Successfully scrolls down - Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the edit profile button"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the edit profile button")
                edit_profile = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//button[text()='Edit Profile'])[1]")))
                edit_profile.click()
                time.sleep(3)
                logging.info("Successfully Clicked on the edit profile button- Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll down till the page visible"""
        with caplog.at_level(logging.INFO):
            try:

                element = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "//h1[text()='ID Details']")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)
                logging.info("Successfully scrolls down - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the continue button"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the continue button")
                continue_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Continue']")))
                continue_button.click()
                time.sleep(3)
                logging.info("Successfully Clicked on the continue button- Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll up till the page visible"""
        with caplog.at_level(logging.INFO):
            try:

                element = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//label[text()='Website'])[1]")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)
                logging.info("Successfully scrolls down - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clearing the coa field"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clearing the coa field")
                coa_field = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input[id='CA Reg. No.']")))
                coa_field.click()
                time.sleep(3)
                self.driver.execute_script("arguments[0].value = '';", coa_field)
                coa_field.send_keys("8333")
                time.sleep(3)
                coa_field.send_keys("888969")
                logging.info("Successfully cleared - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the submit button")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Submit']")))
                submit_button.click()
                time.sleep(3)
                logging.info("Successfully Clicked on the continue button- Testcase 1.9 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll up till the page visible"""
        with caplog.at_level(logging.INFO):
            try:

                element = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "//div[text()='Firm Details']")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)
                logging.info("Successfully scrolls down - Testcase 1.10 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "coa_field.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.11 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")















