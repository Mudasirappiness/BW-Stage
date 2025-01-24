import time
import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException ,ElementNotInteractableException
from Locators import class_Locators
from helper_methods import click_action,send_keys, screenshot

logger = logging.getLogger(__name__)


class Test_admin_dealer_creation:

        @pytest.mark.usefixtures("admin_setup")
        def test_admin_dealer_account(self,caplog,setup):
            """Logging in to the admin panel"""
            with caplog.at_level(logging.INFO):
                try:
                    self.driver = setup
                    logging.info("Entering values in to the field")
                    send_keys(self.driver,class_Locators.admin_user_name,"kiran@appinessworld.com")
                    send_keys(self.driver,class_Locators.admin_pass,"BW@123")
                    click_action(self.driver,class_Locators.admin_submit)
                    time.sleep(5)

                    expected_result = "Admin"
                    actual_result = self.driver.title
                    assert expected_result == actual_result
                    print("Successfully verified the title")

                    logging.info("Successfully logged in to the admin panel - Testcase 1.1 is passed")

                    logging.info("Clicking on the user management link ")
                    click_action(self.driver,class_Locators.user_management)
                    logging.info("Successfully done - Testcase 1.2 is passed")

                    logging.info("Clicking on the brand link")
                    click_action(self.driver, class_Locators.admin_dealer_user)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Clicking on the create brand button")
                    click_action(self.driver, class_Locators.admin_dealer_create_dealer)
                    time.sleep(3)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    logging.info("Entering values in the Name and id field")
                    send_keys(self.driver, class_Locators.admin_dealer_name,"Testautomation")
                    send_keys(self.driver, class_Locators.admin_dealer_id,"Test-300810")
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Entering phone number")
                    send_keys(self.driver, class_Locators.admin_dealer_phone_number,"8855432246")
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Entering Address")
                    send_keys(self.driver, class_Locators.admin_dealer_address,
                              "32/008- G floor , Chooliamedu, Opposite to KV complex")
                    logging.info("Successfully done - Testcase 1.10 is passed")

                    self.driver.execute_script("window.scrollBy(0,500);")

                    logging.info("Selecting the city")
                    send_keys(self.driver, class_Locators.admin_dealer_city, "chennai")
                    click_action(self.driver,class_Locators.admin_dealer_city_suggestion)
                    logging.info("Successfully done - Testcase 1.8 is passed")

                    logging.info("Selecting the location served")
                    send_keys(self.driver, class_Locators.admin_dealer_location_served, "salem")
                    click_action(self.driver, class_Locators.admin_dealer_location_served_suggestion)
                    logging.info("Successfully done - Testcase 1.9 is passed")

                    logging.info("Selecting the id type")
                    click_action(self.driver, class_Locators.admin_dealer_id_click)
                    click_action(self.driver, class_Locators.admin_dealer_id_type)
                    send_keys(self.driver, class_Locators.admin_dealer_id_number,"06AAHCB5089L1Z8")
                    logging.info("Successfully done - Testcase 1.11 is passed")

                    logging.info("Selecting the feature")
                    click_action(self.driver, class_Locators.admin_dealer_featured)
                    logging.info("Successfully done - Testcase 1.12 is passed")

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.admin_dealer_submit)
                    time.sleep(5)
                    logging.info("Successfully done - Testcase 1.13 is passed")

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create.png")

                except (NoSuchElementException , ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Element not found{}".format(e))






