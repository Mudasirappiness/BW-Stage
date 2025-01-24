import time
from selenium.common.exceptions import NoSuchElementException , ElementNotInteractableException
import logging
import os
from PIL import Image
from send_mail import send_email
import pytest
from helper_methods import click_action , java_click , send_keys, enter_text_in_os_dialog , java_send_keys
from Locators import class_Locators

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class Test_account_creation:

    def test_end_user_account(self,caplog,setup):
        self.driver = setup
        """Creating an account """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the profile menu")
                click_action(self.driver,class_Locators.profile_icon)
                time.sleep(2)
                logging.info("Successfully clicked on the profile menu - Testcase 1.1 is passed")

                logging.info("Clicking on the sign up button")
                click_action(self.driver, class_Locators.sign_up)
                time.sleep(2)
                logging.info("Successfully clicked on the signup menu - Testcase 1.2 is passed")

                logging.info("Entering value in the email field button")
                send_keys(self.driver, class_Locators.sign_up_email_field,"dummyenduser07@yopmail.com")
                time.sleep(2)
                logging.info("Successfully entered value in the field- Testcase 1.3 is passed")

                logging.info("Clicking on the getotp button")
                click_action(self.driver, class_Locators.get_otp)
                time.sleep(2)
                logging.info("Successfully clicked the button- Testcase 1.4 is passed")

                logging.info("Entering OTP in to the fields")
                send_keys(self.driver,class_Locators.otp_1,"1")
                send_keys(self.driver, class_Locators.otp_2, "2")
                send_keys(self.driver, class_Locators.otp_3, "3")
                send_keys(self.driver, class_Locators.otp_4, "4")
                logging.info("Successfully entered otp- Testcase 1.5 is passed")

                logging.info("Clicking on the verify button")
                click_action(self.driver, class_Locators.verify_button)
                time.sleep(2)
                logging.info("Successfully clicked the button- Testcase 1.6 is passed")

                logging.info("Entering passwords in to the field")
                send_keys(self.driver, class_Locators.password_1,"Mudasir@123")
                send_keys(self.driver, class_Locators.password_2,"Mudasir@123")
                click_action(self.driver, class_Locators.continue_button)
                time.sleep(2)
                logging.info("Successfully clicked the button- Testcase 1.7 is passed")

                logging.info("Selecting an user role")
                click_action(self.driver, class_Locators.user_selection)
                click_action(self.driver,class_Locators.continue_button)
                time.sleep(2)
                logging.info("Successfully selected an user - Testcase 1.8 is passed")

                logging.info("Filling an form ")
                send_keys(self.driver, class_Locators.user_name,"Mudasir")
                time.sleep(3)

                send_keys(self.driver, class_Locators.user_phone_number,"9786202847")
                time.sleep(5)

                click_action(self.driver, class_Locators.phone_number_verify)
                send_keys(self.driver,class_Locators.otp_1,"1")
                send_keys(self.driver,class_Locators.otp_2,"2")
                send_keys(self.driver, class_Locators.otp_3, "3")
                send_keys(self.driver, class_Locators.otp_4, "4")

                click_action(self.driver,class_Locators.password_verify_submit)
                time.sleep(2)

                send_keys(self.driver,class_Locators.user_location,"salem")
                time.sleep(1)

                click_action(self.driver,class_Locators.user_location_dropdown)
                time.sleep(1)

                click_action(self.driver,class_Locators.check_box)
                time.sleep(1)

                click_action(self.driver,class_Locators.user_submit)
                time.sleep(5)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "create_end_user.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()

                logging.info("Successfully filled a form - Testcase 1.9 is passed")

            except (NoSuchElementException,ElementNotInteractableException) as e:
                logging.error(f"Element not found {str(e)}")

