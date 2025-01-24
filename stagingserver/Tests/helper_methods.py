
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
from selenium.common.exceptions import NoSuchElementException , ElementNotInteractableException
import logging
import os
from selenium.webdriver.chrome.options import Options
from PIL import Image
from send_mail import send_email
from pynput.keyboard import Key, Controller
import pytest
from Locators import class_Locators
from selenium.webdriver.remote.webelement import WebElement


def enter_text_in_os_dialog(file_path):
    keyboard = Controller()
    time.sleep(1)
    keyboard.type(file_path)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)


def click_action(driver, Locator):

    element = WebDriverWait(driver,10).until(BD.element_to_be_clickable(Locator))
    element.click()


def java_click(driver, Locator):
    element = WebDriverWait(driver,10).until(BD.element_to_be_clickable(Locator))
    driver.execute_script("arguments[0].click();", element)


def java_send_keys(driver, Locator, text):
    element = WebDriverWait(driver,10).until(BD.element_to_be_clickable(Locator))
    driver.execute_script("arguments[0].value = arguments[1];",element,text)


def send_keys(driver, Locator,text):
    element = WebDriverWait(driver,10).until(BD.presence_of_element_located(Locator))
    element.send_keys(text)


def move_element(driver, locator):
    element = WebDriverWait(driver,10).until(BD.presence_of_element_located(locator))
    action_chain = ActionChains(driver)
    action_chain.move_to_element(element)
    action_chain.perform()


def screenshot(driver, file_path, file_name):
    screenshot_path = os.path.join(file_path, file_name)
    driver.save_screenshot(screenshot_path)
    showing = Image.open(screenshot_path)
    showing.show()
    send_email()


def is_element_displayed(driver, locator):

    element = WebDriverWait(driver,10).until((BD.presence_of_element_located(locator)))
    return element.is_displayed()









