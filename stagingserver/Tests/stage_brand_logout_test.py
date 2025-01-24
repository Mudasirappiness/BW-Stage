import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
from PIL import Image
from pynput.keyboard import Key, Controller
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from send_mail import send_email
import os

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup","user_account","otp_config")
class Test_logout:
    pass

    def test_logout(self, user_account,caplog,setup):
        """Performing logout"""
        with caplog.at_level(logging.INFO):
            try:
                self.driver = setup

                logging.info("Clicking on the logo menu")
                profile_icon = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='B'])[2]")))
                profile_icon.click()
                time.sleep(3)
                logging.info("Successfully clicked on the logo - Testcase 1.1 is passed")

                logging.info("Clicking on the logout button")
                log_out = WebDriverWait(self.driver,10).until(BD.element_to_be_clickable((By.XPATH,"(//div[text()='Logout'])[1]")))
                log_out.click()
                logging.info("Successfully clicked on the logout button")
                time.sleep(5)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "profile_logout.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.2 is passed")

            except NoSuchElementException as e:
                logging.info("No such element")



