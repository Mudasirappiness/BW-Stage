import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
import logging
import os
from PIL import Image
from send_mail import send_email
from pynput.keyboard import Key, Controller
from helper_methods import enter_text_in_os_dialog


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config_for_service")
class Test_media_approval:

    def test_ten_media(self, caplog):

        """"Clicking on the hamburger menu"""
        with caplog.at_level(logging.INFO):

            try:

                logging.info("Clicking on the hamburger menu")
                hamburger_menu = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//*[@id='html']/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")))
                hamburger_menu.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the hamburger menu- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the my project button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the my project")
                my_project = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()=' My Projects'])[1]")))
                my_project.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the My project button- Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the create project button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the create project")
                create_project = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Add Project']")))
                create_project.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the create project button- Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 1 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")
        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 2 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")
        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 3 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")
        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 4 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")
        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked  5 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 6 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 7 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()

                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 8  on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked 9 on the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the upload image button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the upload image")
                upload_image = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Browse'])[1]")))
                upload_image.click()
                logging.info("Successfully Clicked on the upload button - Testcase 1.5 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:

                file_path = r"C:\Users\muduu\OneDrive\Desktop\Images\testingidea.jpg"

                enter_text_in_os_dialog(file_path)

                logging.info("Successfully entered value - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Done']")))
                done_button.click()
                time.sleep(6)

                logging.info("Successfully Clicked on 10 the done button - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the project name field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                project_name = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@id='ProjectName*']")))
                project_name.send_keys("Aims hospital")
                time.sleep(2)

                logging.info("Successfully entered value in the field - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll down till the page visible"""
        element = WebDriverWait(self.driver, 10).until(
            BD.element_to_be_clickable((By.XPATH, "(//label[text()='Project Name*'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)

        """"Selecting value from the type of building dropdown"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Selecting value in the type of building field ")
                type_of_building = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "(//div[@class=' css-1wy0on6'])[1]")))
                type_of_building.click()
                time.sleep(2)

                type_of_building_sug = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//p[text()='Commercial']")))
                type_of_building_sug.click()
                time.sleep(2)

                logging.info("Successfully entered value in the field - Testcase 1.9 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the location field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                idea_location = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//*[@id='html']/body/main/div/div[5]/div[2]/div/div[6]/div[1]/div/div/div/input")))
                idea_location.send_keys("salem")
                time.sleep(2)
                logging.info("Successfully entered value in the field - Testcase 1.10 is passed")

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
                logging.info("Successfully selected value from the dropdown - Testcase 1.11 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Submit']")))
                submit_button.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.12 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(5)

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "project_iamges.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.30 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")