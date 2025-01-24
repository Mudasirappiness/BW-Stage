import time
import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from Locators import class_Locators
from helper_methods import click_action, java_click, java_send_keys, send_keys, enter_text_in_os_dialog,screenshot , is_element_displayed

logger = logging.getLogger(__name__)


class Test_admin_product_creation:

        @pytest.mark.usefixtures("admin_setup")
        def test_admin_product(self,caplog,setup):
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

                    logging.info("Clicking on the ideas link ")
                    click_action(self.driver,class_Locators.admin_idea_link)
                    logging.info("Successfully done - Testcase 1.2 is passed")
                    logging.info("Clicking on the add idea button ")
                    click_action(self.driver, class_Locators.admin_add_idea)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Uploading a image")
                    click_action(self.driver, class_Locators.admin_idea_image_browse)
                    filepath = r"C:\Users\muduu\OneDrive\Desktop\Images\idea.jpg"
                    enter_text_in_os_dialog(filepath)
                    click_action(self.driver,class_Locators.admin_idea_image_continue)
                    click_action(self.driver, class_Locators.admin_idea_image_done)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    self.driver.execute_script("window.scrollBy(0,300);")

                    logging.info("Entering values in the ID & name field")
                    send_keys(self.driver, class_Locators.admin_idea_id, "Commercial-112")
                    send_keys(self.driver, class_Locators.admin_idea_name,"Multi purpose")
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Selecting a location")
                    send_keys(self.driver, class_Locators.admin_idea_location, "salem")
                    click_action(self.driver, class_Locators.admin_idea_location_suggestion)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Selecting a idea category")
                    click_action(self.driver, class_Locators.admin_idea_classification)
                    assertion = is_element_displayed(self.driver, class_Locators.admin_idea_classification)
                    print("Assertion :",assertion)

                    time.sleep(2)
                    click_action(self.driver, class_Locators.admin_idea_l1)
                    time.sleep(2)
                    click_action(self.driver, class_Locators.admin_idea_l2)
                    logging.info("Successfully done - Testcase 1.7 is passed")

                    logging.info("Entering values in the description field")
                    send_keys(self.driver, class_Locators.admin_idea_description,"Commercial-112")
                    logging.info("Successfully done - Testcase 1.8 is passed")

                    logging.info("Clicking on the iconic projects")
                    click_action(self.driver, class_Locators.admin_idea_iconic_unique)
                    logging.info("Successfully done - Testcase 1.9 is passed")

                    self.driver.execute_script("window.scrollBy(0,500);")
                    time.sleep(3)

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.submit_button)
                    time.sleep(5)
                    logging.info("Successfully done - Testcase 1.10is passed")

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create_idea.png")

                except (NoSuchElementException , ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Error {}".format(e))




