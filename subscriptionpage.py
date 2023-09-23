from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_subscription_page(self):
        subscription_url = "https://www.abcmouse.com/abt/subscription"
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(subscription_url)
        )

    def verify_become_member_text(self):
        membership_text = self.driver.find_element(By.XPATH, "//h1[text()='Become a Member!']")
        assert membership_text.is_displayed()
