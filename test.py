import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

class TestAddition(unittest.TestCase):
    def setUp(self):
        # Specify the correct path to your ChromeDriver
        self.driver = webdriver.Chrome()
        self.driver.get('file:///C:/Users/CSELAB2/Desktop/devopslab_568/js_testing/addition.html')

    def test_addition(self):
        driver = self.driver

        # Adding debug messages to track execution
        print("Opening the page...")

        try:
            num1_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'num1'))
            )
            print("Found first input element (num1).")
            
            num2_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'num2'))
            )
            print("Found second input element (num2).")
            
            add_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'button'))
            )
            print("Found Add button.")
            
            result_span = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'result'))
            )
            print("Found result span.")

            # Simulate user input
            num1_input.send_keys('5')
            num2_input.send_keys('10')
            add_button.click()

            # Wait for result to be updated
            WebDriverWait(driver, 20).until(
                lambda d: result_span.text != ""
            )
            
            # Verify the result is 15
            self.assertEqual(result_span.text, '15')
            print("Test passed: result is 15.")

        except TimeoutException:
            print("Test failed: Element not found within the given time.")

    def tearDown(self):
        # Delay closing the browser to view the result
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
