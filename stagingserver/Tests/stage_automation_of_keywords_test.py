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


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config")
class Test_automate_of_kwords_idea:

    def test_automation(self, caplog):
        time.sleep(5)

        """"Searching the idea"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching the idea")
                search_query = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search for Products'])[1]")))
                search_query.send_keys("Bathroom in Krishnan House")
                time.sleep(3)
                logging.info("Successfully entered value ion the search field - Testcase 1.1 is passed")
                search_query.send_keys(Keys.ENTER)
                time.sleep(3)

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                product_tab = WebDriverWait(self.driver ,10).until(
                    BD.element_to_be_clickable((By.XPATH,"(//button[@role='tab'])[4]"))
                )
                product_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.2 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Clicking on the idea to the navigation"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Clicking on the idea card")
                details_page = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(17) > div:nth-child(9) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(7)"))
                )
                details_page.click()

                time.sleep(10)
                logging.info("Successfully clicked in the idea - Testcase 1.3 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Switching in to the new tab"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the new tab")
                new_tab = self.driver.window_handles[-1]
                self.driver.switch_to.window(new_tab)
                logging.info("Successfully moved in top the new tab - Testcase 1.4 is passed")
            except(NoSuchElementException,ElementNotInteractableException)as e:
                logging.error("Window not found: {e}")

        """Searching a tagged product with title """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with title")
                search_tagged_product = WebDriverWait(self.driver ,10).until(BD.presence_of_element_located((By.XPATH,"(//input[@placeholder='Search for Products'])[1]")))
                search_tagged_product.send_keys("RK Marble India Bengal Black Granite")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the term - Testcase 1.5 is passed")
            except (NoSuchElementException, ElementNotInteractableException)as e :

                logging.error("Element not found:{e}")

        """Changing to the idea tab"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.6 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with keyword """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with keyword")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@value='rk marble india bengal black granite'])[2]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "Bengal Black Granite")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.6 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.7 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with L1 -Category title"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with L1- Category title")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@value='bengal black granite'])[2]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "Floors & Walls")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.8 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.9 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with L1 - Keyword"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with L1- Keyword")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search for Products'])[1]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "Floorings")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.10 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.11 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with L2 - Title """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with L2- Title")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search for Products'])[1]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "Natural Stone Floors and Walls")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.12 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.13 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with L2 - Keyword """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with L2- Keyword")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search for Products'])[1]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "Natural Stone Floors")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.14 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.15 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with L3 - Title"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with L3- Title")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search for Products'])[1]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "Granite")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.16 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.17 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Searching a tagged product with L3 - Keyword"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Searching a tagged product with L3- Keyword")
                search_tagged_product = WebDriverWait(self.driver, 10).until(
                    BD.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search for Products'])[1]")))
                search_tagged_product.clear()
                time.sleep(2)
                search_tagged_product.send_keys(
                    "granite flooring ideas")
                search_tagged_product.send_keys(Keys.ENTER)
                time.sleep(5)
                logging.info("Successfully searched the keyword - Testcase 1.18 is passed")
            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")
        """Changing to the idea tab """
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea tab")
                idea_tab = WebDriverWait(self.driver, 10).until(
                    BD.element_to_be_clickable((By.XPATH, "(//button[@role='tab'])[4]"))
                )
                idea_tab.click()
                time.sleep(2)
                logging.info("Successfully moved in to the idea tab - Testcase 1.17 is passed")

            except (NoSuchElementException, ElementNotInteractableException) as e:

                logging.error("Element not found:{e}")

        """Taking screenshot"""
        with caplog.at_level(logging.INFO):
            try:
                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "automation_of_keywords.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.18 is passed")

            except NoSuchElementException as e:
                logger.error(f"Element not found: {e.msg}")