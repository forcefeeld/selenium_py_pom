import time
#import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def test_press_and_hold_captcha(self):
        self.driver.get(self.url)

        el = self.driver.find_element(By.ID, 'px-captcha')
        print("location:", el.location)

        # Locate the captcha element's screen coordinates (adjust as needed)
        #captcha_x, captcha_y = 180, 120

        # Move the mouse to the captcha element and press the mouse button
        #pyautogui.moveTo(captcha_x, captcha_y)
        #pyautogui.mouseDown()

        # Locate and interact with the captcha element (assuming it's an image or button)
        captcha_element = self.driver.find_element(By.ID, '#px-captcha')

        # Perform a press and hold action
        actions = ActionChains(self.driver)
        actions.click_and_hold(captcha_element).perform()

        # Hold for a few seconds (adjust the duration as needed)
        time.sleep(10)  # Hold for 5 seconds

        # Release the mouse button
        #pyautogui.mouseUp()

        # Release the mouse click
        actions.release().perform()

    def click_sign_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signup-button"))
        ).click()

    def verify_registration_page(self):
        registration_url = "https://www.abcmouse.com/abt/register"
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(registration_url)
        )

    def enter_email_and_submit(self, email):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)
        submit_button = self.driver.find_element(By.ID, "submit-button")
        submit_button.click()
