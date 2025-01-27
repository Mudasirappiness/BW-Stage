import time
import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException ,ElementNotInteractableException
from Locators import class_Locators
from helper_methods import click_action,send_keys, screenshot

logger = logging.getLogger(__name__)


class Test_admin_brand_creation:

        @pytest.mark.usefixtures("admin_setup")
        def test_admin_brand_account(self,caplog,setup):
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

                    logging.info("Clicking on the admin link")
                    click_action(self.driver, class_Locators.admin_sub_admin_user_link)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Clicking on the create admin button")
                    click_action(self.driver, class_Locators.admin_sub_admin_create_admin)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    logging.info("Entering values in the Name and id field")
                    send_keys(self.driver, class_Locators.sub_admin_dealer_name, "Testautomation")
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Entering values in the email field ")
                    # reset = class_Locators.sub_admin_dealer_email_reset
                    # reset.clear()
                    send_keys(self.driver, class_Locators.sub_admin_dealer_new_email, "dealersubadmin@yopmail.com")
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("selecting a sub_admin_role ")
                    click_action(self.driver, class_Locators.sub_admin_dealer_user_open_click)
                    click_action(self.driver, class_Locators.sub_admin_dealer_user_selection)
                    click_action(self.driver, class_Locators.sub_admin_dealer_user_close_click)
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Checking the password")
                    send_keys(self.driver, class_Locators.sub_admin_dealer_password,"Mud@123")
                    logging.info("Successfully done - Testcase 1.7 is passed")

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.sub_admin_dealer_submit)
                    time.sleep(5)
                    logging.info("Successfully done - Testcase 1.13 is passed")

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create.png")

                except (NoSuchElementException, ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Element not found{}".format(e))






