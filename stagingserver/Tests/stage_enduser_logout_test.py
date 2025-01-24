import time
import pytest
from PIL import Image
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException ,ElementNotInteractableException
from send_mail import send_email
import os
from Locators import class_Locators
from helper_methods import click_action, java_click, java_send_keys, send_keys, enter_text_in_os_dialog

logger = logging.getLogger(__name__)


class Test_logout:

    @pytest.mark.usefixtures("setup")
    def test_login(self, setup, caplog):
        self.driver = setup
        """Creating a service account"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the profile icon")
                click_action(self.driver, class_Locators.profile_icon)
                logging.info("Successfully done - Test case 1.1 is passed ")

                logging.info("Clicking on the login link")
                click_action(self.driver, class_Locators.login_link)
                logging.info("Successfully done - Test case 1.2 is passed ")

                logging.info("Clicking on the login with OTP button")
                click_action(self.driver, class_Locators.login_with_otp)
                logging.info("Successfully done - Test case 1.3 is passed ")

                logging.info("Entering value email or number in the field")
                send_keys(self.driver, class_Locators.login_email_or_phone_number, "testingenduser@yopmail.com")
                logging.info("Successfully done - Test case 1.4 is passed ")

                logging.info("Clicking on the login with OTP button")
                click_action(self.driver, class_Locators.get_otp)
                logging.info("Successfully done - Test case 1.5 is passed ")

                logging.info("Entering OTP in to the fields")
                send_keys(self.driver, class_Locators.otp_1, "1")
                send_keys(self.driver, class_Locators.otp_2, "2")
                send_keys(self.driver, class_Locators.otp_3, "3")
                send_keys(self.driver, class_Locators.otp_4, "4")
                logging.info("Successfully entered otp- Testcase 1.6 is passed")

                logging.info("Clicking on the verify button")
                click_action(self.driver, class_Locators.verify_button)
                logging.info("Successfully done - Test case 1.7 is passed ")
                time.sleep(5)

                logging.info("Clicking on the logo menu")
                click_action(self.driver,class_Locators.end_user_logo)
                time.sleep(3)
                logging.info("Successfully clicked on the logo - Testcase 1.8 is passed")

                logging.info("Clicking on the logout button")
                click_action(self.driver,class_Locators.service_logout)
                logging.info("Successfully clicked on the logout button -Testcase 1.9 is passed")
                time.sleep(5)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "end_user_logout.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.10 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.info("Element not found {}".format(e))



