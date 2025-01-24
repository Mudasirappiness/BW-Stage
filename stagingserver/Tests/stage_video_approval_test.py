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
                time.sleep(3)
            except (NoSuchElementException,ElementNotInteractableException) as e:

                logging.error(f"Element not found {str(e)}")

    def test_click_on_my_videos(self,caplog):
        """Clicking on the videos button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the my videos button")
                java_click(self.driver,class_Locators.my_videos)
                logging.info("Successfully clicked on the my video button - Testcase 1.2 is passed")
                time.sleep(3)
            except (NoSuchElementException,ElementNotInteractableException) as e:
                logging.error(f"Element not found {str(e)}")

    def test_click_create_video(self,caplog):
        """Clicking on the create video button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the create video button")
                click_action(self.driver,class_Locators.create_video)
                logging.info("Successfully clicked on the create video button - Testcase 1.3 is passed")
                time.sleep(3)
            except (NoSuchElementException , ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_click_on_the_browse_button(self,caplog):
        """Clicking on the browse button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the browse button")
                click_action(self.driver,class_Locators.browse_button)
                logging.info("Successfully clicked on the browse button - Testcase 1.4 is passed")
                time.sleep(3)
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_upload_video(self,caplog):
        """Uploading video"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Uploading video from the dailog box")
                file_path = r"C:\Users\muduu\OneDrive\Desktop\Videos\fencing.mp4"
                enter_text_in_os_dialog(file_path)
                time.sleep(5)
                logging.info("Successfully uploaded a video - Testcase 1.5 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_entering_value_in_the_field(self,caplog):
        """Sending value to the field """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Sending value to the field")
                send_keys(self.driver, class_Locators.video_name,"remove")
                logging.info("Successfully sent a value to the field - Testcase 1.5 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_entering_values_in_the_description(self,caplog):
        """Sending value to the description field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Sending value to the description field")
                send_keys(self.driver,class_Locators.description_field,"This is just sample video")
                logging.info("Successfully sent a value to the description field - Testcase 1.6 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_sending_value_for_location_field(self,caplog):
        """Sending value to the location field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Sending value to the location field")
                send_keys(self.driver,class_Locators.location_field,"salem")
                logging.info("Successfully sent a value to the location field - Testcase 1.7 is passed")
            except (NoSuchElementException , ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_select_value_for_location(self,caplog):
        """Selecting value from the suggestion"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Selecting value from the location suggestion")
                click_action(self.driver,class_Locators.location_dropdown)
                logging.info("Successfully entered value from the suggestion - Testcase 1.8 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_enter_value_in_tags_field(self,caplog):
        """Sending value to the tags field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Sending value to the tags field")
                send_keys(self.driver,class_Locators.tags_field,"fencing")
                click_action(self.driver,class_Locators.tags_suggestion)
                logging.info("Successfully entered value in the tag field - Testcase 1.9 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e :
                logging.error(f"Element not found {str(e)}")

    def test_submit_button(self,caplog):
        """Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the submit button")
                click_action(self.driver,class_Locators.submit_button)
                logging.info("Successfully clicked the button - Testcase 1.10 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error(f"Element not found {str(e)}")

    def test_navigating_to_admin(self,caplog):
        """"Opening a new tab for the admin panel"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the new tab for admin panel")
                action_chains = ActionChains(self.driver)
                self.driver.execute_script("window.open('');")
                action_chains.perform()
                time.sleep(5)
                all_windows = self.driver.window_handles
                self.driver.switch_to.window(all_windows[1])
                self.driver.get("https://fedstage.buildingworld.com/admin/login")
                logging.info("Successfully navigated to the admin panel - Testcase 1.11 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_entering_credentials(self,caplog):
        """Entering credentials and navigating to the home page"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering credentials for the fields")
                send_keys(self.driver, class_Locators.admin_user_name,"kiran@appinessworld.com")
                send_keys(self.driver, class_Locators.admin_pass ,"BW@123")
                java_click(self.driver, class_Locators.admin_submit)
                time.sleep(3)
                click_action(self.driver,class_Locators.videos_tab)
                logging.info("Successfully navigated to the admin panel - Testcase 1.12 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    # def test_clicking_on_entity(self,caplog):
    #     """Clicking on the specific video"""
    #     with caplog.at_level(logging.INFO):
    #         try:
    #             logging.info("Selecting a specific entity")
    #             click_action(self.driver, class_Locators.specific_video)
    #             logging.info("Successfully clicked on the specific video - Testcase 1.13 is passed")
    #         except (NoSuchElementException, ElementNotInteractableException)as e:
    #             logging.error(f"Element not found {str(e)}")

    def test_approve_a_video(self,caplog):
        """Approving a video"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Approving the video")
                click_action(self.driver,class_Locators.created_video)
                java_click(self.driver,class_Locators.approve_button)
                time.sleep(7)
                logging.info("Successfully approved a video - Testcase 1.14 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    # @pytest.mark.usefixtures("screen_shot")
    # def test_screen_shot_and_mail(self,caplog):
    #     """Capturing screen_shot and logs sending to email"""
    #     with caplog.at_level(logging.INFO):
    #         try:
    #             logging.info("Capturing screenshot")
    #             send_email()
    #             logging.info("Successfully captured- Testcase 1.15 is passed ")
    #         except (NoSuchElementException, ElementNotInteractableException)as e:
    #             logging.error(f"Capturing failed {str(e)}")




















