import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as BD
import logging
import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from PIL import Image
import os
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')
def setup(request):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://fedstage.buildingworld.com/tempLogin")
    time.sleep(3)

    try:
        logger.info("Entering email.")
        email_field = WebDriverWait(driver, 10).until(
            BD.presence_of_element_located((By.XPATH, "//input[@id='Username']"))
        )
        email_field.send_keys("BuildingWorld")

        logger.info("Entering password.")
        password_field = WebDriverWait(driver, 10).until(
            BD.presence_of_element_located((By.XPATH, "//input[@id='Password']"))
        )
        password_field.send_keys("1234")

        logger.info("Clicking the submit button.")
        submit_button = WebDriverWait(driver, 10).until(
            BD.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
        )
        submit_button.click()

        # Wait for the login to complete, increase sleep duration if needed
        time.sleep(3)
    except Exception as e:
        logger.error(f"An error occurred during login: {e}")
        driver.quit()
        raise

    request.cls.driver = driver
    yield driver

    logger.info("Tearing down the WebDriver.")
    driver.quit()


@pytest.fixture(scope='class')
def user_account(request, setup):
    driver = setup
    profile_icon = WebDriverWait(driver, 10).until(BD.element_to_be_clickable(
        (By.XPATH, "(//img[@class='rounded-[100px] max-w-none w-[36px] h-[36px] object-cover'])[1]")))
    profile_icon.click()
    time.sleep(3)
    login_button = WebDriverWait(driver, 10).until(BD.element_to_be_clickable((By.XPATH, "(//p[text()='Login'])[2]")))
    login_button.click()
    time.sleep(3)


@pytest.fixture(scope="class")
def users(setup):
    driver = setup
    profile_logos = WebDriverWait(driver, 10).until(BD.presence_of_element_located((By.XPATH,
                                                                                    "//div[@id='wishlist']//div//div[contains(@class,'lg:mb-0 flex justify-center lg:flex-none lg:cursor-pointer')]//img[contains(@alt,'profile pic')]")))
    profile_logos.click()
    time.sleep(3)
    logo_login = WebDriverWait(driver, 10).until(BD.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 "#wishlist > div > div > div:nth-child(2) > div.block > div > div > div.flex.flex-col.justify-between.text-bw-disabled-600 > div > div.flex.items-start.justify-center.col-span-5.flex-col.my-auto > div > div > p:nth-child(2)")))
    logo_login.click()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def otp_config(setup):
    driver = setup
    time.sleep(3)
    log_with_otp_btn = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//a[text()='Login with OTP']")))
    log_with_otp_btn.click()
    email_field = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.CSS_SELECTOR, "input[id='Phone Number or Email']")))
    email_field.send_keys("testingbuildingworld@gmail.com")
    get_otp = WebDriverWait(driver, 10).until(
        BD.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Get OTP']")))
    get_otp.click()

    logging.info("Entering OTP into the boxes")
    otp1 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 1']")))
    otp1.send_keys("8")
    otp2 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 2']")))
    otp2.send_keys("7")
    otp3 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 3']")))
    otp3.send_keys("6")
    otp4 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 4']")))
    otp4.send_keys("5")
    time.sleep(2)
    logging.info("Entered OTP successfully - Testcase 1.5 is passed")

    Verify_btn = WebDriverWait(driver, 10).until(BD.element_to_be_clickable((By.XPATH,
                                                                             "//button[normalize-space()='Verify']")))
    Verify_btn.click()
    time.sleep(5)


@pytest.fixture(scope="function")
def otp_config_for_service(setup, caplog):
    driver = setup
    time.sleep(3)
    log_with_otp_btn = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//a[text()='Login with OTP']")))
    log_with_otp_btn.click()
    email_field = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.CSS_SELECTOR, "input[id='Phone Number or Email']")))
    email_field.send_keys("testingserviceprovider@yopmail.com")
    get_otp = WebDriverWait(driver, 10).until(
        BD.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Get OTP']")))
    get_otp.click()

    logging.info("Entering OTP into the boxes")
    otp1 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 1']")))
    otp1.send_keys("8")
    otp2 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 2']")))
    otp2.send_keys("7")
    otp3 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 3']")))
    otp3.send_keys("6")
    otp4 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 4']")))
    otp4.send_keys("5")
    time.sleep(2)
    logging.info("Entered OTP successfully - Testcase 1.5 is passed")

    verify_btn = WebDriverWait(driver, 10).until(BD.element_to_be_clickable((By.XPATH,
                                                                             "//button[normalize-space()='Verify']")))
    verify_btn.click()
    time.sleep(5)


@pytest.fixture(scope="function")
def otp_config_for_dealer(setup, caplog):
    driver = setup
    time.sleep(3)
    log_with_otp_btn = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//a[text()='Login with OTP']")))
    log_with_otp_btn.click()
    email_field = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.CSS_SELECTOR, "input[id='Phone Number or Email']")))
    email_field.send_keys("testingdealer@yopmail.com")
    get_otp = WebDriverWait(driver, 10).until(
        BD.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Get OTP']")))
    get_otp.click()

    logging.info("Entering OTP into the boxes")
    otp1 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 1']")))
    otp1.send_keys("8")
    otp2 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 2']")))
    otp2.send_keys("7")
    otp3 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 3']")))
    otp3.send_keys("6")
    otp4 = WebDriverWait(driver, 10).until(
        BD.presence_of_element_located((By.XPATH, "//input[@aria-label='Please enter OTP character 4']")))
    otp4.send_keys("5")
    time.sleep(2)
    logging.info("Entered OTP successfully - Testcase 1.5 is passed")

    verify_btn = WebDriverWait(driver, 10).until(BD.element_to_be_clickable((By.XPATH,
                                                                             "//button[normalize-space()='Verify']")))
    verify_btn.click()
    time.sleep(5)


@pytest.fixture(scope='function')
def admin_setup(setup, caplog):
    driver = setup
    driver.execute_script("window.open('https://fedstage.buildingworld.com/admin/login','_blank');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
