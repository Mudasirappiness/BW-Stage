import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
import logging
import os
from PIL import Image
from send_mail import send_email
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from helper_methods import click_action , java_click , send_keys, enter_text_in_os_dialog , move_element
from Locators import class_Locators
from selenium.webdriver.common.action_chains import ActionChains

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config_for_service")
class Test_create_project:

    def test_clicking_on_hamburger_menu(self,caplog,setup):
        self.driver = setup
        """Clicking on the hamburger menu"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the hamburger menu")
                click_action(self.driver,class_Locators.hamburger_menu)
                logging.info("Successfully clicked on the hamburger menu Testcase 1.1 is passed ")

                logging.info("Clicking on the My projects")
                click_action(self.driver, class_Locators.my_project_button)
                logging.info("Successfully clicked on the my project button Testcase 1.2 is passed ")

                logging.info("Clicking on the add projects")
                click_action(self.driver, class_Locators.add_project)
                logging.info("Successfully clicked on the add project button Testcase 1.3 is passed ")

                logging.info("Clicking on the upload button")
                click_action(self.driver, class_Locators.project_upload_button)
                logging.info("Successfully clicked on the upload button Testcase 1.4 is passed ")

                logging.info("Clicking on the upload button")
                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\project.jpg"
                enter_text_in_os_dialog(file_path)
                logging.info("Successfully uploaded a image - Testcase 1.5 is passed")

                logging.info("Clicking on the upload button")
                click_action(self.driver,class_Locators.project_done)
                logging.info("Successfully clicked on done - Testcase 1.6 is passed")

                logging.info("Sending values to the name field")
                send_keys(self.driver, class_Locators.project_name, "Sample project")
                logging.info("Successfully sent values to the field - Testcase 1.7 is passed")

                logging.info("Clicking on the types of building")
                click_action(self.driver, class_Locators.types_of_building_click)
                click_action(self.driver, class_Locators.types_of_buildings_suggestion)
                logging.info("Successfully clicked on the types of building - Testcase 1.8 is passed")

                logging.info("Sending values to the location field ")
                send_keys(self.driver, class_Locators.project_location, "salem")
                click_action(self.driver, class_Locators.project_location_suggestion)
                logging.info("Successfully clicked on the location field - Testcase 1.9 is passed")

                logging.info("Clicking on the submit button")
                click_action(self.driver, class_Locators.project_submit_button)
                logging.info("Successfully clicked on the location field - Testcase 1.10 is passed")

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "create_project.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()

            except (NoSuchElementException,ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")




