import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
from selenium.common.exceptions import NoSuchElementException , ElementNotInteractableException
import logging
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image
from send_mail import send_email
from pynput.keyboard import Key, Controller
import pytest
from helper_methods import click_action , java_click , send_keys, enter_text_in_os_dialog
from Locators import class_Locators
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config")
class Test_media_approval:

    def test_video_approval(self,setup,caplog):
        self.driver = setup
        """"Clicking on the hamburger menu"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the hamburger menu")
                click_action(self.driver , class_Locators.hamburger_menu)
                logging.info("Successfully clicked on the hamburger menu - Testcase 1.1 is passed")

                logging.info("Clicking on the my videos button")
                java_click(self.driver, class_Locators.my_videos)
                logging.info("Successfully clicked on the my video button - Testcase 1.2 is passed")

                logging.info("Clicking on the create video button")
                click_action(self.driver, class_Locators.create_video)
                logging.info("Successfully clicked on the create video button - Testcase 1.3 is passed")

                logging.info("Clicking on the browse button")
                click_action(self.driver, class_Locators.browse_button)
                logging.info("Successfully clicked on the browse button - Testcase 1.4 is passed")

                logging.info("Uploading video from the dailog box")
                file_path = r"C:\Users\muduu\OneDrive\Desktop\Videos\fencing.mp4"
                enter_text_in_os_dialog(file_path)
                time.sleep(5)

                logging.info("Sending value to the field")
                send_keys(self.driver, class_Locators.video_name, "Sample video")
                logging.info("Successfully sent a value to the field - Testcase 1.5 is passed")

                logging.info("Sending value to the description field")
                send_keys(self.driver, class_Locators.description_field, "This is just sample video")
                logging.info("Successfully sent a value to the description field - Testcase 1.6 is passed")

                logging.info("Sending value to the location field")
                send_keys(self.driver, class_Locators.location_field, "salem")
                logging.info("Successfully sent a value to the location field - Testcase 1.7 is passed")

                logging.info("Selecting value from the location suggestion")
                click_action(self.driver, class_Locators.location_dropdown)
                logging.info("Successfully entered value from the suggestion - Testcase 1.8 is passed")

                logging.info("Sending value to the tags field")
                send_keys(self.driver, class_Locators.tags_field, "fencing")
                click_action(self.driver, class_Locators.tags_suggestion)
                logging.info("Successfully entered value in the tag field - Testcase 1.9 is passed")

                logging.info("Clicking on the submit button")
                click_action(self.driver, class_Locators.submit_button)
                logging.info("Successfully clicked the button - Testcase 1.10 is passed")
                time.sleep(3)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "create_video.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error(f"Element not found {str(e)}")