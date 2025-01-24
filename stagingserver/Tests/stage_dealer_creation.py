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


class Test_dealer_creation:

    @pytest.mark.usefixtures("setup")
    def test_dealer_account(self,caplog,setup):
        self.driver = setup
        """Creating a dealer account"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the profile icon")
                click_action(self.driver,class_Locators.profile_icon)
                logging.info("Successfully done - Test case 1.1 is passed ")

                logging.info("Clicking on the signup link")
                click_action(self.driver,class_Locators.sign_up)
                time.sleep(2)
                logging.info("Successfully done - Test case 1.2 is passed ")

                logging.info("Entering value in the email field button")
                send_keys(self.driver, class_Locators.sign_up_email_field, "dummyenduser37@yopmail.com")
                time.sleep(2)
                logging.info("Successfully entered value in the field- Testcase 1.3 is passed")

                logging.info("Clicking on the getotp button")
                click_action(self.driver, class_Locators.get_otp)
                time.sleep(2)
                logging.info("Successfully clicked the button- Testcase 1.4 is passed")

                logging.info("Entering OTP in to the fields")
                send_keys(self.driver, class_Locators.otp_1, "1")
                send_keys(self.driver, class_Locators.otp_2, "2")
                send_keys(self.driver, class_Locators.otp_3, "3")
                send_keys(self.driver, class_Locators.otp_4, "4")
                logging.info("Successfully entered otp- Testcase 1.5 is passed")

                logging.info("Clicking on the verify button")
                click_action(self.driver, class_Locators.verify_button)
                time.sleep(2)
                logging.info("Successfully clicked the button- Testcase 1.6 is passed")

                logging.info("Entering passwords in to the field")
                send_keys(self.driver, class_Locators.password_1, "Mudasir@123")
                send_keys(self.driver, class_Locators.password_2, "Mudasir@123")
                click_action(self.driver, class_Locators.continue_button)
                time.sleep(2)
                logging.info("Successfully clicked the button- Testcase 1.7 is passed")

                logging.info("Selecting an user role")
                click_action(self.driver, class_Locators.user_selection2)
                click_action(self.driver, class_Locators.continue_button)
                time.sleep(2)
                logging.info("Successfully selected an user - Testcase 1.8 is passed")

                logging.info("Filling an form ")
                send_keys(self.driver, class_Locators.user_name, "Mudasir")
                time.sleep(1)
                logging.info("Successfully name entered in the filed - Testcase 1.9 is passed")

                logging.info("Entering phone number ")
                send_keys(self.driver, class_Locators.user_phone_number, "9916366305")
                logging.info("Successfully entered phone number - Testcase 1.10 is passed ")

                logging.info("Clicking on verify button")
                click_action(self.driver, class_Locators.phone_number_verify)
                send_keys(self.driver, class_Locators.otp_1, "1")
                send_keys(self.driver, class_Locators.otp_2, "2")
                send_keys(self.driver, class_Locators.otp_3, "3")
                send_keys(self.driver, class_Locators.otp_4, "4")
                click_action(self.driver, class_Locators.password_verify_submit)
                time.sleep(5)
                logging.info("Successfully verified - Testcase 1.11 is passed ")

                logging.info("Entering address in to the field ")
                send_keys(self.driver, class_Locators.dealer_address,"32/1023 A Kilpauk stadium")
                time.sleep(3)
                logging.info("Successfully entered  - Testcase 1.12 is passed ")

                self.driver.execute_script("window.scrollBy(0,200)")

                logging.info("Selecting a city ")
                send_keys(self.driver, class_Locators.user_location, "salem")
                time.sleep(1)
                click_action(self.driver, class_Locators.user_location_dropdown)
                time.sleep(1)
                logging.info("Successfully selected - Testcase 1.13 is passed ")

                logging.info("Selecting a location served")
                send_keys(self.driver,class_Locators.dealer_location_served,"salem")
                click_action(self.driver,class_Locators.dealer_location_served_suggestion)
                logging.info("Successfully selected - Testcase 1.14 is passed ")

                self.driver.execute_script("window.scrollBy(0,500)")

                logging.info("Selecting a document type")
                click_action(self.driver, class_Locators.document_type_dropdown)
                click_action(self.driver,class_Locators.document_type_select)
                logging.info("Successfully selected - Testcase 1.15 is passed ")

                logging.info("Verifying the document")
                send_keys(self.driver,class_Locators.dealer_id_number,"06AAHCB5089L1Z8")
                click_action(self.driver,class_Locators.phone_number_verify)
                time.sleep(5)
                click_action(self.driver,class_Locators.document_verify_submit)
                logging.info("Successfully Verified - Testcase 1.16 is passed ")

                logging.info("Clicking on the browse button")
                click_action(self.driver, class_Locators.dealer_browse)
                logging.info("Successfully clicked on the browse button - Testcase 1.17 is passed")

                logging.info("Uploading a file")
                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\buildingworld.png"
                enter_text_in_os_dialog(file_path)
                time.sleep(2)
                logging.info("Successfully uploaded -Testcase 1.17 is passed")

                logging.info("Clicking on the done button")
                click_action(self.driver, class_Locators.project_done)
                time.sleep(2)
                logging.info("Successfully done - Testcase 1.18 is passed")

                self.driver.execute_script("window.scrollBy(0,200)")

                logging.info("Clicking on the checkbox")
                click_action(self.driver, class_Locators.check_box)
                time.sleep(3)
                logging.info("Successfully done - Testcase 1.19 is passed")

                logging.info("Clicking on the submit button")
                click_action(self.driver,class_Locators.dealer_submit)
                logging.info("Successfully done - Testcase 1.20 is passed")
                time.sleep(2)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "create_dealer_user.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()

            except (NoSuchElementException,ElementNotInteractableException)as e:
                logging.info("Element not found{}".format(e))

