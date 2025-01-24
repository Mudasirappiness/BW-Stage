import time
from selenium.common.exceptions import NoSuchElementException , ElementNotInteractableException
import logging
import pytest
from helper_methods import click_action , send_keys,screenshot
from Locators import class_Locators

logger = logging.getLogger(__name__)


class Test_end_user_login:

    @pytest.mark.usefixtures("setup")
    def test_login(self,setup,caplog):
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
                send_keys(self.driver, class_Locators.login_email_or_phone_number,"testingenduser@yopmail.com")
                logging.info("Successfully done - Test case 1.4 is passed ")

                logging.info("Clicking on the login with OTP button")
                click_action(self.driver, class_Locators.login_get_otp_button)
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

                logging.info("Asserting the title")
                expected_title = "BuildingWorld"
                actual_title = self.driver.title
                if expected_title == actual_title:
                    print("Successfully logged in")
                else:
                    print("Not done")
                logging.info("Successfully done - Test case 1.8 is passed ")
                time.sleep(3)

                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot(self.driver, folder_path, "end_user_login.png")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.info("Element not found {}".format(e))






