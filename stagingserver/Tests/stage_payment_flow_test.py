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
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import NoSuchFrameException

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup","user_account", "otp_config")
class Test_payment_logged_in:

    def test_payment_for_logged_in_user(self,caplog):
        """"Clicking on the advertise with us button """
        with caplog.at_level(logging.INFO):

            try:

                logging.info("clicking on the advertise with us button")
                advertise_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Advertise with Us']")))
                advertise_button.click()
                time.sleep(3)

                logging.info("Successfully Clicked - Testcase 1.1 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Choosing the plan """
        with caplog.at_level(logging.INFO):

            try:

                """Scroll in to view"""
                self.driver.execute_script("window.scrollBy(0, 900);")
                time.sleep(5)

                logging.info("Choosing the plan")
                advertise_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Invest Now'])[3]")))
                self.driver.execute_script("arguments[0].click();", advertise_button)
                time.sleep(5)

                logging.info("Successfully choosed a plan - Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        # """"Entering values in the GST field """
        # with caplog.at_level(logging.INFO):
        #
        #     try:
        #         logging.info("Entering value in the GST field")
        #         gst_field = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
        #             (By.XPATH, "//input[@id='account**']")))
        #         gst_field.send_keys("")
        #         gst_field.send_keys("33AAPCM6442A1ZO")
        #         time.sleep(2)
        #         logging.info("Successfully entered value - Testcase 1.3 is passed")
        #
        #     except (NoSuchElementException, ElementNotInteractableException) as e:
        #
        #         logging.error("Element not found:{e}")
        #
        # """"Clicking on verify button"""
        # with caplog.at_level(logging.INFO):
        #
        #     try:
        #         logging.info("Clicking on the verify button")
        #         verify_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
        #             (By.XPATH, "//p[text()='Verify']")))
        #         verify_button.click()
        #         time.sleep(6)
        #         logging.info("Successfully entered value - Testcase 1.4 is passed")
        #
        #     except (NoSuchElementException, ElementNotInteractableException) as e:
        #
        #         logging.error("Element not found:{e}")
        #
        # """"Clicking on submit button"""
        # with caplog.at_level(logging.INFO):
        #
        #     try:
        #         logging.info("Clicking on the submit button")
        #         submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
        #             (By.XPATH, "//span[text()='Submit']")))
        #         submit_button.click()
        #         time.sleep(6)
        #         logging.info("Successfully clicked the submit button - Testcase 1.5 is passed")
        #
        #     except (NoSuchElementException, ElementNotInteractableException) as e:
        #
        #         logging.error("Element not found:{e}")

        """"Clicking on next button"""
        with caplog.at_level(logging.INFO):

            try:
                logging.info("Clicking on the submit button")
                next_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Next']")))
                next_button.click()
                time.sleep(6)
                logging.info("Successfully clicked the next button - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Switching to the frame"""
        with caplog.at_level(logging.INFO):

            try:
                logging.info("switching to the frame")
                switch_frame = WebDriverWait(self.driver,10).until(BD.presence_of_element_located((By.XPATH,"//iframe[@class='razorpay-checkout-frame']")))
                self.driver.switch_to.frame(switch_frame)

                logging.info("Successfully switched to the frame - Testcase 1.7 is passed")

            except (ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on UPI payment option"""
        with caplog.at_level(logging.INFO):

            try:
                logging.info("Clicking on UPI payment option")
                upi_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='UPI']")))
                upi_button.click()
                time.sleep(5)
                logging.info("Successfully clicked the next button - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the field"""
        with caplog.at_level(logging.INFO):

            try:
                logging.info("Clicking on UPI payment option")
                upi_field = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@name='vpa']")))
                upi_field.send_keys("hdfc@icicipay")
                time.sleep(5)
                logging.info("Successfully clicked the next button - Testcase 1.9 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the verify button"""
        with caplog.at_level(logging.INFO):

            try:
                logging.info("Clicking on UPI payment verify button")
                upi_field_verify = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[@data-testid='vpa-submit']")))
                upi_field_verify.click()
                time.sleep(5)
                logging.info("Successfully clicked the verify button - Testcase 1.10 is passed")
                time.sleep(10)

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"/Users/mac/Desktop/new repo/Staging-automation/stagingserver/Tests/screenshots"
                screenshot_path = os.path.join(folder_path, "payment.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.11 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")




