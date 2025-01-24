import time
import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException ,ElementNotInteractableException
from Locators import class_Locators
from helper_methods import click_action,send_keys, screenshot

logger = logging.getLogger(__name__)


class Test_admin_service_creation:

        @pytest.mark.usefixtures("admin_setup")
        def test_admin_service_account(self,caplog,setup):
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

                    logging.info("Clicking on the service link")
                    click_action(self.driver, class_Locators.admin_service_user)
                    logging.info("Successfully done - Testcase 1.3 is passed")


                    logging.info("Clicking on the create service button")
                    click_action(self.driver, class_Locators.admin_service_create_service)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    logging.info("Entering values in the Name and id field")
                    send_keys(self.driver, class_Locators.admin_service_user_name,"Testautomation")
                    send_keys(self.driver, class_Locators.admin_service_user_id,"Tes3t-00811")
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Entering phone number")
                    send_keys(self.driver, class_Locators.admin_service_phone_number,"9655442247")
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Entering address")
                    send_keys(self.driver, class_Locators.admin_service_address, "Test-bigdata")
                    logging.info("Successfully done - Testcase 1.7 is passed")

                    self.driver.execute_script("window.scrollBy(0,500);")

                    logging.info("Selecting the city")
                    send_keys(self.driver, class_Locators.admin_service_city, "salem")
                    click_action(self.driver,class_Locators.service_city_suggestion)
                    logging.info("Successfully done - Testcase 1.8 is passed")
                    time.sleep(2)

                    logging.info("Selecting the id type")
                    click_action(self.driver, class_Locators.admin_service_id_select)
                    click_action(self.driver, class_Locators.admin_service_id_suggestion)
                    send_keys(self.driver, class_Locators.admin_service_id_number,"06AAHCB5089L1Z8")
                    logging.info("Successfully done - Testcase 1.9 is passed")
                    time.sleep(2)

                    logging.info("Selecting the types of service provided")
                    click_action(self.driver, class_Locators.admin_service_types_of_services)
                    click_action(self.driver, class_Locators.admin_service_types_of_services_suggestion)
                    time.sleep(2)
                    click_action(self.driver, class_Locators.admin_service_types_of_service_arrow)
                    logging.info("Successfully done - Testcase 1.10 is passed")

                    logging.info("Selecting the specialization")
                    click_action(self.driver, class_Locators.admin_service_specialization_click)
                    click_action(self.driver, class_Locators.admin_service_specialization_suggestion)
                    time.sleep(2)
                    click_action(self.driver, class_Locators.admin_service_specialization_arrow)
                    logging.info("Successfully done - Testcase 1.11 is passed")

                    logging.info("Selecting the location served")
                    send_keys(self.driver, class_Locators.admin_service_location_served, "bengaluru")
                    click_action(self.driver, class_Locators.admin_service_location_served_suggestion)
                    logging.info("Successfully done - Testcase 1.12 is passed")

                    logging.info("Entering about us")
                    send_keys(self.driver, class_Locators.admin_service_about_us, "Test-bigdata")
                    logging.info("Successfully done - Testcase 1.13 is passed")

                    logging.info("Selecting the feature")
                    click_action(self.driver, class_Locators.admin_service_featured)
                    logging.info("Successfully done - Testcase 1.14 is passed")

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.admin_service_submit)
                    time.sleep(5)
                    logging.info("Successfully done - Testcase 1.15 is passed")

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create.png")

                except (NoSuchElementException , ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Element not found{}".format(e))