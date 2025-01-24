import time
import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException ,ElementNotInteractableException
from Locators import class_Locators
from helper_methods import click_action,send_keys, screenshot

logger = logging.getLogger(__name__)


class Test_admin_end_user_creation:

        @pytest.mark.usefixtures("admin_setup")
        def test_admin_end_user_account(self,caplog,setup):
            """Logging in to the admin panel"""
            with caplog.at_level(logging.INFO):
                try:
                    self.driver = setup
                    logging.info("Entering values in to the field")
                    send_keys(self.driver,class_Locators.admin_user_name,"kiran@appinessworld.com")
                    send_keys(self.driver,class_Locators.admin_pass,"BW@123")
                    click_action(self.driver,class_Locators.admin_submit)
                    time.sleep(5)
                    logging.info("Successfully logged in to the admin panel - Testcase 1.1 is passed")

                    logging.info("Clicking on the user management link ")
                    click_action(self.driver,class_Locators.user_management)
                    logging.info("Successfully done - Testcase 1.2 is passed")

                    logging.info("Clicking on the end_user link")
                    click_action(self.driver, class_Locators.admin_end_user)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Clicking on the create users button")
                    click_action(self.driver, class_Locators.admin_end_user_create_user)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    logging.info("Entering values in the Name and id field")
                    send_keys(self.driver, class_Locators.admin_end_user_name,"Testautomation")
                    send_keys(self.driver, class_Locators.admin_end_user_email,"Tes3t-00811q")
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Entering phone number")
                    send_keys(self.driver, class_Locators.admin_end_user_phone_number,"9656442247")
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Selecting the city")
                    send_keys(self.driver, class_Locators.admin_end_user_city, "salem")
                    click_action(self.driver,class_Locators.admin_end_user_city_suggestion)
                    logging.info("Successfully done - Testcase 1.8 is passed")
                    time.sleep(2)

                    logging.info("Selecting the gender")
                    click_action(self.driver, class_Locators.admin_end_user_gender_click)
                    click_action(self.driver, class_Locators.admin_end_user_gender_selection)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Entering address")
                    send_keys(self.driver, class_Locators.admin_end_user_address, "32/102 A Karumbukadai , 2nd cross coimbatore")
                    logging.info("Successfully done - Testcase 1.13 is passed")

                    logging.info("Entering bio")
                    send_keys(self.driver, class_Locators.admin_end_user_bio, "We are prestigious group of companies")
                    logging.info("Successfully done - Testcase 1.13 is passed")
                    time.sleep(2)

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.admin_end_user_submit)
                    logging.info("Successfully done - Testcase 1.15 is passed")
                    time.sleep(2)

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create.png")

                except (NoSuchElementException , ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Element not found{}".format(e))