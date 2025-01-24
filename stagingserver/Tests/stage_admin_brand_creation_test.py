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

                    logging.info("Clicking on the brand link")
                    click_action(self.driver, class_Locators.admin_brand_user)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Clicking on the create brand button")
                    click_action(self.driver, class_Locators.admin_create_brand_button)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    logging.info("Entering values in the Name and id field")
                    send_keys(self.driver, class_Locators.admin_brand_name,"Testautomation")
                    send_keys(self.driver, class_Locators.admin_brand_id,"Test-0081")
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Entering phone number")
                    send_keys(self.driver, class_Locators.admin_brand_phone_number,"9655432246")
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Entering parent company")
                    send_keys(self.driver, class_Locators.admin_brand_parent_company, "Test-bigdata")
                    logging.info("Successfully done - Testcase 1.7 is passed")

                    self.driver.execute_script("window.scrollBy(0,500);")

                    logging.info("Selecting the city")
                    send_keys(self.driver, class_Locators.admin_brand_city, "salem")
                    click_action(self.driver,class_Locators.admin_brand_city_suggestion)
                    logging.info("Successfully done - Testcase 1.8 is passed")

                    logging.info("Selecting the location served")
                    send_keys(self.driver, class_Locators.admin_brand_location_served, "chennai")
                    click_action(self.driver, class_Locators.admin_brand_location_served_suggestion)
                    logging.info("Successfully done - Testcase 1.9 is passed")

                    logging.info("Entering Address")
                    send_keys(self.driver, class_Locators.admin_brand_address, "32/008- G floor , Chooliamedu, Opposite to KV complex")
                    logging.info("Successfully done - Testcase 1.10 is passed")

                    logging.info("Selecting the id type")
                    click_action(self.driver, class_Locators.admin_brand_id_select)
                    click_action(self.driver, class_Locators.admin_brand_id_type_select)
                    send_keys(self.driver, class_Locators.admin_brand_id_number,"06AAHCB5089L1Z8")
                    logging.info("Successfully done - Testcase 1.11 is passed")

                    logging.info("Selecting the feature")
                    click_action(self.driver, class_Locators.admin_brand_featured)
                    logging.info("Successfully done - Testcase 1.12 is passed")

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.admin_brand_submit)
                    time.sleep(5)
                    logging.info("Successfully done - Testcase 1.13 is passed")

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create.png")

                except (NoSuchElementException , ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Element not found{}".format(e))






