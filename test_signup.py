from base_test import BaseTestCase
from homepage import HomePage
from subscriptionpage import SubscriptionPage
import unittest


class TestSignUp(BaseTestCase):
    def test_signup_flow(self):
        # Step 1A: Go to the ABCmouse website
        home_page = HomePage(self.driver, self.url)
        home_page.open()
        #
        # # Step 1B: Bypass the human check
        # captcha = self.driver.find_element_by_id("captcha")
        # if captcha.is_displayed():
        #     # Handle captcha (long press 'PRESS & HOLD')
        #     home_page.test_press_and_hold_captcha()
        #
        # Step 2: Click the "Sign Up" button
        home_page.click_sign_up()

        # Step 3: Verify the registration page
        home_page.verify_registration_page()

        # Step 4: Enter email address and submit
        home_page.enter_email_and_submit(self.email)

        # Step 5: Verify the subscription page
        subscription_page = SubscriptionPage(self.driver)
        subscription_page.verify_subscription_page()

        # Step 6: Verify "Become a Member!" text
        subscription_page.verify_become_member_text()


if __name__ == "__main__":
    unittest.main()
