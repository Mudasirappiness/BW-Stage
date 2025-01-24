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
from helper_methods import click_action , java_click , send_keys, enter_text_in_os_dialog , move_element
from Locators import class_Locators
from selenium.webdriver.common.action_chains import ActionChains


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup", "user_account", "otp_config")
class Test_create_wishlist:

    def test_navigating_to_the_product(self,setup,caplog):
        self.driver = setup
        """Clicking on the products"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the products page")
                click_action(self.driver,class_Locators.product_tab)
                logging.info("Successfully clicked on the products tab - Testcase 1.1 is passed")
                time.sleep(3)
            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.error(f"Element not found{str(e)}")

    def test_create_folder(self,caplog,setup):
        """Creating a folder"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Creating a folder")
                element = WebDriverWait(self.driver,10).until(BD.element_to_be_clickable((By.CSS_SELECTOR,r"#JhroKbCdCvyYFmyNLe\/e6A\=\= > div > div.relative.aspect-\[4\/3\].rounded-md.border.border-bw-typo-50.shadow-400.imageHolder.bottom-0.transition-all > div > div > div.cursor-pointer.z-30 > svg > path")))
                action_chains = ActionChains(self.driver)
                action_chains.move_to_element(element)
                action_chains.perform()
                time.sleep(2)
                click_action(self.driver,class_Locators.new_folder)
                send_keys(self.driver,class_Locators.folder_name,"Construction designs")
                time.sleep(2)
                click_action(self.driver, class_Locators.folder_submit_button)
                time.sleep(2)
                logging.info("Successfully created a folder - Testcase 1.2 is passed")
            except (NoSuchElementException,ElementNotInteractableException) as e:
                logging.error(f"Element not found{str(e)}")

    def test_next_wishlist(self,caplog,setup):
        """Moving to the other element"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the other element")
                move_element(self.driver, class_Locators.wish_list)
                time.sleep(2)
                click_action(self.driver,class_Locators.created_list)
                time.sleep(3)
                logging.info("Successfully wishlisted the product - Testcase 1.3 is passed ")
            except (NoSuchElementException,ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_navigating_to_the_idea(self,caplog,setup):
        """Navigating to the idea"""
        with caplog .at_level(logging.INFO):
            try:
                logging.info("Navigating to the idea section")
                click_action(self.driver,class_Locators.building_world)
                time.sleep(3)
                self.driver.execute_script("window.scrollBy(0,500)")
                time.sleep(2)
                click_action(self.driver,class_Locators.idea_section)
                time.sleep(2)
                click_action(self.driver,class_Locators.sort_by)
                time.sleep(2)
                move_element(self.driver,class_Locators.idea_wishlist1)
                time.sleep(2)
                click_action(self.driver,class_Locators.created_list)
                time.sleep(2)
                logging.info("Successfully navigated to the idea section - Testcase 1.4 is passed ")
            except (NoSuchElementException, ElementNotInteractableException)as e:
                logging.error(f"Element not found {str(e)}")

    def test_navigating_to_the_service(self,caplog,setup):
        """Navigating to the services"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the service section")
                click_action(self.driver,class_Locators.building_world)
                time.sleep(2)
                click_action(self.driver,class_Locators.navigating_service)
                time.sleep(2)
                move_element(self.driver,class_Locators.service_wishlist)
                time.sleep(2)
                click_action(self.driver,class_Locators.created_list)
                time.sleep(5)
                logging.info("Successfully navigated to the service section- Testcase 1.5 is passed ")
            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.info(f"Element not found {str(e)}")

    def test_navigating_my_list(self,caplog,setup):
        """Navigating to the my wish list"""
        with caplog.at_level(logging.INFO):
            try:
                logging.info("Navigating to the mywishlist page")
                click_action(self.driver,class_Locators.hamburger_menu)
                time.sleep(3)
                click_action(self.driver,class_Locators.my_wish_list_page)
                time.sleep(2)
                click_action(self.driver,class_Locators.created_folder)
                time.sleep(2)
                logging.info("Successfully navigated to the my wishlist page - Testcase 1.6 is passed ")
            except (NoSuchElementException, ElementNotInteractableException) as e:
                logging.info(f"Element not found {str(e)}")








