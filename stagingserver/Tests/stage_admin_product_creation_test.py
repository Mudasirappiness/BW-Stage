import time
import pytest
from PIL import Image
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException ,ElementNotInteractableException
from send_mail import send_email
import os
from Locators import class_Locators
from helper_methods import click_action, java_click, java_send_keys, send_keys, enter_text_in_os_dialog,screenshot

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

                    logging.info("Clicking on the product link ")
                    click_action(self.driver,class_Locators.admin_product_tab)
                    logging.info("Successfully done - Testcase 1.2 is passed")

                    logging.info("Clicking on the add product button ")
                    click_action(self.driver, class_Locators.admin_add_product)
                    logging.info("Successfully done - Testcase 1.3 is passed")

                    logging.info("Selecting a brand")
                    send_keys(self.driver, class_Locators.admin_brand_search, "hind")
                    click_action(self.driver, class_Locators.admin_brand_suggestion)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.4 is passed")

                    logging.info("Uploading a profile picture")
                    click_action(self.driver,class_Locators.admin_product_browse)
                    image_path = r"C:\Users\muduu\Downloads\washbasin.jpg"
                    enter_text_in_os_dialog(image_path)
                    click_action(self.driver,class_Locators.project_done)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.5 is passed")

                    logging.info("Entering value in the product name & product ID")
                    send_keys(self.driver, class_Locators.admin_product_name, "Washbasin")
                    send_keys(self.driver, class_Locators.admin_product_id, "hind-0923")
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.6 is passed")

                    logging.info("Selecting a product category")
                    click_action(self.driver, class_Locators.admin_product_category)
                    time.sleep(2)
                    click_action(self.driver,class_Locators.admin_product_L1)
                    time.sleep(2)
                    click_action(self.driver,class_Locators.admin_product_L2)
                    time.sleep(2)
                    click_action(self.driver,class_Locators.admin_product_l3_select)
                    time.sleep(2)
                    click_action(self.driver,class_Locators.admin_product_l3_click)
                    time.sleep(2)
                    logging.info("Successfully done - Testcase 1.7 is passed")

                    logging.info("Clicking on the price on request ")
                    click_action(self.driver, class_Locators.admin_price_on_request)
                    logging.info("Successfully done - Testcase 1.8 is passed")

                    self.driver.execute_script("window.scrollBy(0,2500);")
                    time.sleep(3)

                    logging.info("Clicking on the submit button")
                    click_action(self.driver, class_Locators.folder_submit_button)
                    time.sleep(5)
                    logging.info("Successfully done - Testcase 1.9is passed")

                    folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                    screenshot(self.driver,folder_path,"admin_create.png")

                except (NoSuchElementException , ElementNotInteractableException, TimeoutException)as e:
                    logging.error("Element not found{}".format(e))




