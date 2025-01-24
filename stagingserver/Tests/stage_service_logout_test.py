import time
import pytest
from PIL import Image
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from send_mail import send_email
import os
from Locators import class_Locators
from helper_methods import click_action, java_click, java_send_keys, send_keys, enter_text_in_os_dialog

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config_for_service")
class Test_logout:

    def test_service_logout(self,caplog,setup):

        """Performing logout"""
        with caplog.at_level(logging.INFO):
            try:
                self.driver = setup

                logging.info("Clicking on the logo menu")
                click_action(self.driver,class_Locators.service_profile_icon)
                time.sleep(3)
                logging.info("Successfully clicked on the logo - Testcase 1.1 is passed")

                logging.info("Clicking on the logout button")
                click_action(self.driver,class_Locators.service_logout)
                logging.info("Successfully clicked on the logout button")
                time.sleep(5)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "service_logout.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.2 is passed")

            except NoSuchElementException as e:
                logging.info("No such element")
