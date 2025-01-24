import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import logging
from send_mail import send_email
from PIL import Image


@pytest.mark.usefixtures("setup")
class TestTypeSearch:

    def test_type_search(self, caplog):
        """Searching with specific keywords."""
        with caplog.at_level(logging.INFO):
            try:
                # Wait for the search input field to be present and clickable
                search_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search for Products']"))
                )

                # Search for "jaquar tap"
                logging.info("Searching with the word Jaquar tap")
                search_input.send_keys("jaquar tap")
                click_suggestion = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@title='jaquar tap']")))
                click_suggestion.click()
                time.sleep(10)
                logging.info("We can see the results for jaquar tap - Test case for 1.1 is passed")

                """"Clicking on the products tab"""
                logging.info("Clicking on the products tab ")
                products_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, "//button[text()='Products']")))
                products_tab.click()
                time.sleep(3)
                logging.info("Successfully clicked - Testcase 1.2 is passed")

                # Scroll down 5 times
                logging.info("Scrolling down for 5 times")
                execution = 7
                for i in range(execution):
                    self.driver.execute_script("window.scrollBy(0, 150);")
                    time.sleep(3)  # Adding a short delay to observe the scroll effect

                logging.info("Scrolling down the page successfully executed - Testcase 1.8 is passed")

                """Scroll down till the page visible"""
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//h1[text()='FILTERS']")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)

                # Re-locate the search input field to handle possible stale element reference
                search_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "(//input[@value='jaquar tap'])[2]"))
                )
                search_input.clear()

                # Search for "marble floors"
                logging.info("Searching with the word marble floors ")
                search_input.send_keys("marble floors")
                time.sleep(5)
                marble_click = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "(//span[@title='marble floors'])[2]")))
                marble_click.click()
                time.sleep(5)
                logging.info("We can see the results for basin mixer  - Test case for 1.2 is passed")

                # Scroll down 5 times
                logging.info("Scrolling down for 5 times")
                execution = 7
                for i in range(execution):
                    self.driver.execute_script("window.scrollBy(0, 150);")
                    time.sleep(3)  # Adding a short delay to observe the scroll effect

                logging.info("Scrolling down the page successfully executed - Testcase 1.8 is passed")

                """Scroll down till the page visible"""
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//h1[text()='FILTERS']")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)

                # Re-locate the search input field to handle possible stale element reference
                search_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "(//input[@value='marble floors'])[2]"))
                )
                search_input.clear()

                # Search for "sofa"
                logging.info("Searching with the word 'taps'")
                search_input.send_keys("basin mixer")
                time.sleep(5)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='html']/body/div[5]/div[6]/div/div/ul/li[1]"))
                ).click()
                time.sleep(5)
                logging.info("We can see the results sofa set - Test case for 1.3 is passed")

                logging.info("Navigating to the products tab")
                product_tab = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[text()='Products']")))
                product_tab.click()
                time.sleep(5)
                logging.info("Successfully navigated to the products tab - Testcase 1.4 is passed")

                logging.info("Clicking on the price filter")
                price_filter = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='1000.0-9000.0']")))
                price_filter.click()
                time.sleep(5)
                logging.info("Successfully clicked on the price filter - Testcase 1.5 is passed")

                logging.info("Scrolling down till the sort by filter")
                scroll_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[text()='Sort by']"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
                time.sleep(5)

                logging.info("Scrolled to the element successfully - Testcase 1.6 is passed")

                logging.info("Clicking on the sorting filter")
                sorting_filter = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='asc']")))
                sorting_filter.click()
                time.sleep(5)
                logging.info("Successfully clicked on the sorting filter - Low to High - Testcase 1.7 is passed")

                # Scroll down 5 times
                logging.info("Scrolling down for 5 times")
                execution = 7
                for i in range(execution):
                    self.driver.execute_script("window.scrollBy(0, 150);")
                    time.sleep(3)  # Adding a short delay to observe the scroll effect

                logging.info("Scrolling down the page successfully executed - Testcase 1.8 is passed")

                """Scroll down till the page visible"""
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//h1[text()='FILTERS']")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(3)

                logger.info("Taking screenshot")
                folder_path = r"C:\Users\muduu\Downloads\stagingserver\Tests\screenshots"
                screenshot_path = os.path.join(folder_path, "type_search.png")
                self.driver.save_screenshot(screenshot_path)
                showing = Image.open(screenshot_path)
                showing.show()
                send_email()
                logger.info("Screenshot done - Testcase 1.2 is passed")

            except (TimeoutException, StaleElementReferenceException) as e:
                logging.error(f"Exception occurred: {e}")
                raise
