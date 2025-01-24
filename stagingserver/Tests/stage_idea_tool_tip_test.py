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
class Test_create_idea:

    def test_create_idea(self, caplog):

        """"Clicking on the hamburger menu"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the hamburger menu")
                hamburger_menu = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//*[@id='html']/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")))
                hamburger_menu.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the hamburger menu- Testcase 1.1 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the my ideas button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the my ideas")
                my_idea = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='My Ideas'])[1]")))
                my_idea.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the My ideas button- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the create idea button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the idea product ")
                create_idea = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[2]//span[2]")))
                create_idea.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the create idea button- Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Upload Image']")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the OS dialog box")
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(r"C:\Users\muduu\OneDrive\Desktop\Images\walllight.jpg")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(3)
                logging.info("Successfully entered value - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(2)
                logging.info("Successfully Clicked on the done button - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")
        """Scroll in to view"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Scrolling down ")
                self.driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(5)
                logging.info("Successfully done - Testcase 1.7 is passed")
            except(NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found : {e}")

        """"Entering value in the idea name field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                idea_name = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "(//input[@id='IdeaTitle*'])[2]")))
                idea_name.send_keys("Idea tool tip")
                time.sleep(3)

                logging.info("Successfully entered value in the field - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the location field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                idea_location = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.CSS_SELECTOR, "div[class=' w-full'] section[class='md:w-full my-5'] div input[type='text']")))
                idea_location.send_keys("salem")
                time.sleep(3)

                idea_suggestion = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Salem, Tamil Nadu']")))
                idea_suggestion.click()

                logging.info("Successfully entered value in the field - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll in to view"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Scrolling down ")
                self.driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(2)
                logging.info("Successfully done - Testcase 1.7 is passed")
            except(NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found : {e}")

        """"Clicking on the Classification field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the classification field")
                idea_classification_1 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "(//span[@class='absolute w-full h-full z-10 cursor-pointer'])[2]")))
                self.driver.execute_script("arguments[0].click();",idea_classification_1)
                time.sleep(2)
                logging.info("Successfully clicked on the field - Testcase 1.11 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Selecting value in the product category l1 field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                l1 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//p[text()='Commercial']")))
                l1.click()
                time.sleep(2)

                logging.info("Successfully selected the L1 value- Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Selecting value in the product category l2 field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                l2 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//p[text()='Commercial Building']")))
                l2.click()
                time.sleep(2)

                logging.info("Successfully selected the L2 value- Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the description field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the description field ")
                idea_description = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "(//textarea[@placeholder=' '])[2]")))
                idea_description.send_keys("This is the best commercial alarm the building")
                time.sleep(2)

                logging.info("Successfully entered value in the field - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Submit'])[2]")))
                submit_button.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the got it  button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                got_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Got it!']")))
                got_button.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the title card"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                title_card = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[@title='Idea tool tip']")))
                title_card.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.15 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the edit button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                edit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Edit']")))
                edit_button.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.17 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the add brand button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the add product button")
                add_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='Add Brand'])[2]")))
                add_brand.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.18 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Searching the brand"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Searching the brand in the field")
                add_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@placeholder='Search brand']")))
                add_brand.send_keys("mudasir")

                add_entered_data = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Mudasir & Co private limited']")))
                add_entered_data.click()

                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.19 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(2)

        """"Clicking on the save button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the save button")
                save_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Save']")))
                save_button.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.20 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(2)

        """"Choosing the second value for brand"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the add product button")
                add_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='Add Brand'])[2]")))
                add_brand.click()

                search_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@placeholder='Search brand']")))
                search_brand.send_keys("hindware")

                add_entered_data = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Hindware Limited']")))
                add_entered_data.click()

                logging.info("Successfully clicked - Testcase 1.21 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the save button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the save button")
                save_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Save']")))
                save_button.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.22 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Choosing the third value for brand"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the add product button")
                add_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='Add Brand'])[2]")))
                add_brand.click()

                search_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@placeholder='Search brand']")))
                search_brand.send_keys("jaquar")

                add_entered_data = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Jaquar_Light']")))
                add_entered_data.click()

                logging.info("Successfully clicked - Testcase 1.23 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the save button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the save button")
                save_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Save']")))
                save_button.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.24 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the add service button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the add service button")
                add_service = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='Add Service'])[4]")))
                add_service.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.25 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(2)

        """"Searching the service"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Searching the brand in the field")
                add_service = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@placeholder='Search services']")))
                add_service.send_keys("mudasir")

                add_entered_data = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Mudasir']")))
                add_entered_data.click()

                check_box = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@id='6']")))
                check_box.click()

                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Submit'])[3]")))
                submit_button.click()

                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.26 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the save button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the save button")
                save_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Save']")))
                save_button.click()
                time.sleep(2)
                logging.info("Successfully clicked - Testcase 1.27 is passed")

                self.driver.execute_script("window.scrollBy(0, 600);")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the save button")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Submit'])[2]")))
                submit_button.click()
                self.driver.refresh()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.28 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Clicking on the tagged brand """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the save button")
                tagged_brand = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Mudasir & Co private limited']")))
                tagged_brand.click()
                logging.info("Successfully clicked on the tagged brand - Testcase 1.29 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Navigating to the new-tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating & switch bag to the same tab")

                self.driver.execute_script("window.open('about:blank', '_blank');")
                self.driver.switch_to.window(self.driver.window_handles[1])

                if len(self.driver.window_handles) > 1:
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    time.sleep(2)

                logging.info("Successfully navigated back to the same tab - Testcase 1.29 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "tool_tip.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.30 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")