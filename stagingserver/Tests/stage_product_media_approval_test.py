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
class Test_media_approval:

    def test_media_approval(self, caplog):

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

        """"Clicking on the my product button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the my product")
                my_product = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//p[text()='My Products'])[1]")))
                my_product.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the My project button- Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the create product button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the create product ")
                create_product = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Add Product']")))
                create_product.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the create product button- Testcase 1.3 is passed")

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

                logging.info("Successfully Clicked on the upload button - Testcase 1.4 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the OS dialog box")
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(r"C:\Users\muduu\Downloads\ladder1.jpg")
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
                    (By.XPATH, "//button[text()='Done']")))
                done_button.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the done button - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Entering value in the product name field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                product_name = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@id='Product Name*']")))
                product_name.send_keys("Aluminium ladder for house")
                time.sleep(3)

                logging.info("Successfully entered value in the field - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Scroll down till the page visible"""
        element = WebDriverWait(self.driver, 10).until(
            BD.element_to_be_clickable((By.XPATH, "//p[text()='Photos and Document of Product*']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)

        """"Entering value in the product category field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the field ")
                product_category = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.CSS_SELECTOR, ".absolute.w-full.h-full.z-10.cursor-pointer")))
                product_category.click()
                time.sleep(3)

                logging.info("Successfully clicked in the field - Testcase 1.8 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

            """"Selecting value in the product category l1 field"""
            with caplog.at_level(logging.INFO):
                try:
                    logging.info("Entering value in the field ")
                    l1 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//p[text()='Access & Security']")))
                    l1.click()
                    time.sleep(3)

                    logging.info("Successfully selected the L1 value- Testcase 1.9 is passed")

                except (NoSuchElementException, ElementNotInteractableException) as e:

                    logging.error("Element not found:{e}")

            """"Selecting value in the product category l2 field"""
            with caplog.at_level(logging.INFO):
                try:
                    logging.info("Entering value in the field ")
                    l2 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//p[text()='Access Ladders']")))
                    l2.click()
                    time.sleep(3)

                    logging.info("Successfully selected the L2 value- Testcase 1.10 is passed")

                except (NoSuchElementException, ElementNotInteractableException) as e:

                    logging.error("Element not found:{e}")

            """"Selecting value in the product category l3 field"""
            with caplog.at_level(logging.INFO):
                try:
                    logging.info("Entering value in the field ")
                    l3_field = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//body[1]/main[1]/div[1]/div[6]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")))
                    l3_field.click()

                    l3 = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                        (By.XPATH, "//p[text()='Electrical Loft Ladders']")))
                    l3.click()
                    time.sleep(3)

                    logging.info("Successfully selected the L2 value- Testcase 1.7 is passed")

                except (NoSuchElementException, ElementNotInteractableException) as e:

                    logging.error("Element not found:{e}")

        """"Entering value in the price field"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering value in the price field ")
                price_filter = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@id='price']")))
                price_filter.send_keys("25000")
                time.sleep(2)

                logging.info("Successfully entered value in the field - Testcase 1.8 is passed")

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
                logging.info("Successfully clicked - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(5)

        """"Clicking on the got it  button"""
        with caplog.at_level(logging.INFO):
            try:

                logging.info("Clicking on the submit button ")
                got_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Got it!']")))
                got_button.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.14 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(5)

        """Navigating to the admin side"""

        with caplog.at_level(logging.INFO):
            try:
                logging.info("Opening a new tab and navigating to the admin panel")
                self.driver.execute_script("window.open('about:blank', '_blank');")
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(5)
                self.driver.get("https://fedstage.buildingworld.com/admin/login")
                time.sleep(3)

                admin_username = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@name='email']")))
                admin_username.send_keys("mudasiradmin@yopmail.com")

                admin_password = WebDriverWait(self.driver, 10).until(BD.presence_of_element_located(
                    (By.XPATH, "//input[@id='password']")))
                admin_password.send_keys("Mud@123")

                admin_login = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Login']")))
                admin_login.click()

                time.sleep(5)
                logging.info("Successfully logged in to the admin panel - Testcase 1.15 is passed")

            except (NoSuchElementException, ElementNotInteractableException):
                logging.error("Element not found:{e}")

        """"Clicking on the products link"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the products link ")
                products_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[normalize-space()='Products']")))
                products_button.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.16 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """"Clicking on the products to approve"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the projects to approve ")
                specific_products = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[@title='Aluminium ladder for house']")))
                specific_products.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.17 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """"Clicking on the approve button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the approve button ")
                approve_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Approve']")))
                self.driver.execute_script("arguments[0].click();", approve_button)
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.18 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """"Entering values in the ID field """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the ID field")
                id_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//input[@name='id']")))
                id_button.send_keys("Ladder-001")
                time.sleep(5)
                logging.info("Successfully clicked - Testcase 1.19 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """"Clicking on the approve button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the approve button ")
                approve_button_2 = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//button[text()='Approve'])[2]")))
                self.driver.execute_script("arguments[0].click();", approve_button_2)
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.20 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """Get back to the user side"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Getting back to the previous tab")

                if len(self.driver.window_handles) > 1:
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    logging.info("Switched back to the original tab. - Testcase 1.21 is passed")
                    time.sleep(10)
                    self.driver.refresh()

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found: {e}")

        """"Clicking on the approve tab"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the approve button ")
                approve_tab = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Approved']")))
                self.driver.execute_script("arguments[0].click();", approve_tab)
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.22 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """"Clicking on the details page"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the details button")
                details_page = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Aluminium ladder for house']")))
                self.driver.execute_script("arguments[0].click();", details_page)
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.23 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """"Navigating to the new page for details"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the new page ")
                self.driver.switch_to.window(self.driver.window_handles[2])
                logging.info("Successfully navigated - Testcase 1.24 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(6)

        """"Clicking on the edit button"""
        with caplog.at_level(logging.INFO):
            try:
                self.driver.refresh()
                logging.info("Clicking on the edit tab")
                edit_tab = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Edit'])[1]")))
                self.driver.execute_script("arguments[0].click();", edit_tab)
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.25 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """"Clicking on the browse button"""
        with caplog.at_level(logging.INFO):
            try:
                time.sleep(3)
                logging.info("Clicking on the browse button")
                browse_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//img[@src='/images/icons/uploadImg.svg']")))
                browse_button.click()
                time.sleep(3)
                logging.info("Successfully clicked on the browse button- Testcase 1.26 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")

        """selecting a document from a file"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Entering values in the OS dialog box")
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(r"C:\Users\muduu\Downloads\ladder2.jpg")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(5)
                logging.info("Successfully entered value - Testcase 1.27 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the done button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the done button ")
                done_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Done']")))
                done_button.click()
                time.sleep(3)

                logging.info("Successfully Clicked on the done button - Testcase 1.28 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the submit button"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the browse button")
                submit_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Submit']")))
                self.driver.execute_script("arguments[0].click();", submit_button)
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.29 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found:{e}")
                time.sleep(3)

        """Again navigating to the admin panel to approve the uploaded media"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the admin panel for approve the media")
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.refresh()
                time.sleep(3)
                logging.info("Successfully navigated to the admin panel - Testcase 1.30 is passed ")

            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error("Element not found : {e}")

        """"Clicking on the project for details page"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the specific project")
                specific_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//p[text()='Aluminium ladder for house']")))
                specific_button.click()
                time.sleep(3)

                logging.info("Successfully navigated to the details page - Testcase 1.31 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the approved icon"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the approve button")
                approved_button = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.CSS_SELECTOR, "img[class='h-5 w-5 p-0.5']")))
                approved_button.click()
                time.sleep(3)

                logging.info("Successfully clicked on the approved button - Testcase 1.32 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """"Clicking on the approved popup"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the approve popup")
                approved_popup = WebDriverWait(self.driver, 10).until(BD.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Approve']")))
                approved_popup.click()
                time.sleep(3)

                logging.info("Successfully clicked on the approved popup - Testcase 1.33 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "product_media_approval.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.34 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")




