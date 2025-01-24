import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
from PIL import Image
from pynput.keyboard import Key, Controller
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from send_mail import send_email


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup","user_account","otp_config_for_service")
class Test_stage_Login:

    def test_screenshot(self,caplog):

        """Again clicking on the logo"""
        with caplog.at_level(logging.INFO):

            logging.info("Clicking on the logo menu")
            profile_icon = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                (By.XPATH, "(//p[text()='TA'])[2]")))
            profile_icon.click()
            time.sleep(3)
            logging.info("Successfully again clicked on the logo - Testcase 1.6 is passed")

            logger.info("Taking screenshot")
            folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
            screenshot_path = os.path.join(folder_path, "profile_logout.png")
            self.driver.save_screenshot(screenshot_path)
            showing = Image.open(screenshot_path)
            showing.show()
            send_email()
            logger.info("Screenshot done - Testcase 1.7 is passed")











