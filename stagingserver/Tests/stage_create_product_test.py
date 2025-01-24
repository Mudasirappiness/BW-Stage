import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException , N
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
import logging
import os
from PIL import Image
from send_mail import send_email
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config")
class Test_create_product:

    def test_create_product(self,caplog):
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

        """"Clicking on the my product button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the my product")
                my_product = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='My Products'])[1]")))
                my_product.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the My project button- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the create product button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the create product ")
                create_product = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Add Product']")))
                create_product.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the create product button- Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the OS dialog box")
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(r"C:\Users\muduu\Downloads\product.jpg")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(3)
                logging.info("Successfully entered value - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the done button - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Entering value in the product name field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                product_name = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@id='Product Name*']")))
                product_name.send_keys("Bullet Solar Power 4G Network Camera")
                time.sleep(3)

                logging.info("Successfully entered value in the field - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll down till the page visible"""
        element = WebDriverWait(self.driver, 10).until(
            BD.element_to_be_clickable((By.XPATH, "//p[text()='Photos and Document of Product*']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)

        """"Entering value in the product category field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                product_category = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.CSS_SELECTOR, ".absolute.w-full.h-full.z-10.cursor-pointer")))
                product_category.click()
                time.sleep(3)

                logging.info("Successfully clicked in the field - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

            """"Selecting value in the product category l1 field"""
            with caplog.at_level(logging.INFO):
                try:
                    logging.info("Entering value in the field ")
                    l1 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//p[text()='Access & Security']")))
                    l1.click()
                    time.sleep(3)

                    logging.info("Successfully selected the L1 value- Testcase 1.9 is passed")

                except (NoSuchElementException, ElementNotInteractableException) as e:

                    logging.error("Element not found:{e}")

            """"Selecting value in the product category l2 field"""
            with caplog.at_level(logging.INFO):
                try:
                    logging.info("Entering value in the field ")
                    l2 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//p[text()='CCTV Camera']")))
                    l2.click()
                    time.sleep(3)

                    logging.info("Successfully selected the L2 value- Testcase 1.10 is passed")

                except (NoSuchElementException, ElementNotInteractableException) as e:

                    logging.error("Element not found:{e}")

            """"Selecting value in the product category l3 field"""
            with caplog.at_level(logging.INFO):
                try:
                    logging.info("Entering value in the field ")
                    l3_field = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//body[1]/main[1]/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")))
                    l3_field.click()

                    l3 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//p[text()='Bullet Solar Power 4G Network Camera Kit']")))
                    l3.click()
                    time.sleep(3)

                    logging.info("Successfully selected the L2 value- Testcase 1.7 is passed")

                except (NoSuchElementException, ElementNotInteractableException) as e:

                    logging.error("Element not found:{e}")

        """"Entering value in the price field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the price field ")
                price_filter = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@id='price']")))
                price_filter.send_keys("25000")
                time.sleep(2)

                logging.info("Successfully entered value in the field - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Submit']")))
                submit_button.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(5)

        """"Clicking on the got it  button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                got_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Got it!']")))
                got_button.click()
                time.sleep(2)
                self.driver.refresh()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(5)

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "create_product.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.15 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")

