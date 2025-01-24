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


@pytest.mark.usefixtures("setup","user_account","otp_config")
class Test_idea_cropping:

    def test_idea_crop(self, caplog):

        """"Clicking on the hamburger menu"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the hamburger menu")
                hamburger_menu = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable((By.XPATH,"//*[@id='html']/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")))
                hamburger_menu.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the hamburger menu- Testcase 1.1 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the my ideas button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the my ideas")
                my_ideas = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='My Ideas'])[1]")))
                my_ideas.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the My ideas button- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the create idea button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the create idea")
                create_ideas = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Add New Idea'])[2]")))
                create_ideas.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the create ideas button- Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Upload Image']")))
                upload_image.click()
                time.sleep(5)

                logging.info("Successfully Clicked on the upload button - Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the OS dialog box")
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(r"C:\Users\muduu\Downloads\testingidea.jpg")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(3)
                logging.info("Successfully entered value - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the select crop button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                crop_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.CSS_SELECTOR, "svg[aria-label='Select crop']")))
                crop_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the select crop button - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the select ratio icon"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the select ratio icon")
                image_ratio = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='4:5']")))
                image_ratio.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the select ratio button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Done']")))
                done_button.click()
                time.sleep(5)

                logging.info("Successfully Clicked on the done button - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll in to view"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Scrolling down ")
                self.driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(5)
                logging.info("Successfully done - Testcase 1.9 is passed")
            except(NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found : {e}")

        """"Entering value in the idea name field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                idea_name = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "(//input[@id='IdeaTitle*'])[2]")))
                idea_name.send_keys("Idea cropping for test")
                time.sleep(3)

                logging.info("Successfully entered value in the field - Testcase 1.10 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the location field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                idea_location = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.CSS_SELECTOR, "div[class=' w-full'] section[class='md:w-full my-5'] div input[type='text']")))
                idea_location.send_keys("salem")
                time.sleep(2)
                logging.info("Successfully entered value in the field - Testcase 1.11 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Selecting value from the location dropdown"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Selecting value from the dropdown")
                idea_suggestion = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Salem, Tamil Nadu']")))
                idea_suggestion.click()
                time.sleep(3)
                logging.info("Successfully selected value from the dropdown - Testcase 1.12 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll in to view"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Scrolling down ")
                self.driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(5)
                logging.info("Successfully done - Testcase 1.13 is passed")
            except(NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found : {e}")

        """"Clicking on the Classification field"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the classification field")
                idea_classification = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[@class='absolute w-full h-full z-10 cursor-pointer'])[2]")))
                idea_classification.click()
                time.sleep(3)
                logging.info("Successfully clicked on the field - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Selecting value from the classification dropdown"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Selecting value from the dropdown")
                classification_suggestion_l1 = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Commercial']")))
                classification_suggestion_l1.click()

                time.sleep(2)

                classification_suggestion_l2 = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Commercial Building']")))
                classification_suggestion_l2.click()
                time.sleep(3)
                logging.info("Successfully selected value from the dropdown - Testcase 1.15 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the idea description field"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the description field")
                idea_description = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//textarea[@placeholder=' '])[2]")))
                idea_description.click()
                time.sleep(2)
                idea_description.send_keys("Hello this is for testing")
                logging.info("Successfully entered value - Testcase 1.16 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//button[text()='Submit'])[2]")))
                submit_button.click()
                time.sleep(5)
                logging.info("Successfully clicked - Testcase 1.17 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "idea_cropping.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.18 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")

