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

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config")
class Test_create_post_requirement:

    def test_post_requirement(self,caplog):
        """"Clicking on the dropdown"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the Announce New Project / Post your requirement dropdown ")
                announce_project = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//button[@class='p-1 outline-none'])[1]")))
                announce_project.click()
                time.sleep(3)

                logging.info("Successfully Clicked - Testcase 1.1 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the post your requirement"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the post your requirement")
                post_requirement = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Post Your Requirement']")))
                post_requirement.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the Announce New Project Button- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the location"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Entering value in the location")
                announce_project_location = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH,
                     "//div[contains(@class,'relative')]//div[contains(@class,'w-full relative')]//input[contains(@type,'text')]")))
                announce_project_location.send_keys("Chennai")
                time.sleep(2)

                location_suggestion = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Chennai, Tamil Nadu']")))
                location_suggestion.click()

                logging.info("Successfully entered value in the location field- Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the Types of construction dropdown"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the Types of construction dropdown")
                types_of_construction = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//div[text()='--Select--'])[1]")))
                types_of_construction.click()
                time.sleep(3)

                types_of_construction_suggestion = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Educational']")))
                types_of_construction_suggestion.click()

                logging.info("Successfully entered value in the Types of construction dropdown- Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the product required field """
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Entering value in the product required field")
                product_required = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//*[@id='html']/body/main/div/div[5]/div/div[3]/div/div/div[3]/div[1]/div/div[1]/div/input")))
                product_required.send_keys("bricks")
                time.sleep(3)

                product_required_suggestion = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH,"//li[text()='Cement concrete bricks']")))
                product_required_suggestion.click()

                logging.info("Successfully entered value in the product required field - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the quantity required field"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Entering value in the quantity required field")
                quantity_required = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//*[@id='html']/body/main/div/div[5]/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div/div/div/input")))
                quantity_required.send_keys("8500")
                time.sleep(2)

                logging.info("Successfully Entered value in the quantity required- Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the timeline dropdown"""
        with caplog.at_level(logging.INFO):

            try:
                logging.info("Clicking on the project timeline dropdown")
                time_line = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//*[@id='html']/body/main/div/div[5]/div/div[3]/div/div/div[3]/div[2]/div/div/div/div")))
                time_line.click()
                time.sleep(3)

                time_line_suggestion = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Three Months']")))
                time_line_suggestion.click()
                logging.info("Successfully entered value in the project timeline button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the OS dialog box")
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(r"C:\Users\muduu\Downloads\project.jpg")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(3)
                logging.info("Successfully entered value - Testcase 1.9 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll in to view"""
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(5)

        """"Entering values in the description field """
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Entering values in the description field")
                description_field = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//textarea[@placeholder=' ']")))
                description_field.send_keys("This is my own project")
                time.sleep(3)

                logging.info("Successfully Entered values in the description field - Testcase 1.10 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the submit button")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Submit']")))
                submit_button.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the submit Button- Testcase 1.11 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path,"post_requirement.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.12 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")
