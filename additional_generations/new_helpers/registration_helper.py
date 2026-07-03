"""
Helper for user registration related flows.
Orchestrates the complete registration process including navigation, form filling, and submission.
"""

from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from pages.registration_success_page import RegistrationSuccessPage
from core.settings import framework_logger


class RegistrationHelper:
    """Helper for orchestrating user registration flows."""

    @staticmethod
    def navigate_to_registration_page(page: Page):
        """
        Navigates to the registration page.
        
        Args:
            page: Playwright Page object
        """
        # This should be configured based on the actual application URL
        # For now, using a placeholder that should be replaced with actual URL
        registration_url = "https://example.com/register"
        page.goto(registration_url)
        page.wait_for_load_state("networkidle", timeout=30000)
        framework_logger.info("Navigated to registration page")

    @staticmethod
    def fill_registration_form(page: Page, first_name: str, last_name: str, email: str, 
                               password: str, phone_number: str, date_of_birth: str):
        """
        Fills all fields in the registration form.
        
        Args:
            page: Playwright Page object
            first_name: User's first name
            last_name: User's last name
            email: User's email address
            password: User's password
            phone_number: User's phone number
            date_of_birth: User's date of birth (MM/DD/YYYY)
        """
        registration_page = RegistrationPage(page)
        
        registration_page.first_name_input.fill(first_name)
        framework_logger.info(f"Entered first name: {first_name}")
        
        registration_page.last_name_input.fill(last_name)
        framework_logger.info(f"Entered last name: {last_name}")
        
        registration_page.email_input.fill(email)
        framework_logger.info(f"Entered email: {email}")
        
        registration_page.password_input.fill(password)
        framework_logger.info("Entered password")
        
        registration_page.confirm_password_input.fill(password)
        framework_logger.info("Entered confirm password")
        
        registration_page.phone_number_input.fill(phone_number)
        framework_logger.info(f"Entered phone number: {phone_number}")
        
        registration_page.select_date_of_birth(date_of_birth)
        framework_logger.info(f"Selected date of birth: {date_of_birth}")

    @staticmethod
    def submit_registration(page: Page):
        """
        Submits the registration form and waits for submission to complete.
        
        Args:
            page: Playwright Page object
        """
        registration_page = RegistrationPage(page)
        registration_page.register_button.click()
        framework_logger.info("Clicked register button")
        
        # Wait for form submission to complete
        page.wait_for_load_state("networkidle", timeout=30000)
        framework_logger.info("Registration form submitted")

    @staticmethod
    def verify_registration_success(page: Page, expected_message: str):
        """
        Verifies that registration was successful by checking the success message.
        
        Args:
            page: Playwright Page object
            expected_message: Expected success message text
        """
        success_page = RegistrationSuccessPage(page)
        expect(success_page.success_message).to_be_visible(timeout=30000)
        expect(success_page.success_message).to_contain_text(expected_message, timeout=30000)
        framework_logger.info(f"Verified success message: {expected_message}")

    @staticmethod
    def complete_registration(page: Page, first_name: str, last_name: str, email: str,
                             password: str, phone_number: str, date_of_birth: str,
                             expected_success_message: str = "Registration Successful"):
        """
        Completes the entire registration flow from navigation to success verification.
        
        Args:
            page: Playwright Page object
            first_name: User's first name
            last_name: User's last name
            email: User's email address
            password: User's password
            phone_number: User's phone number
            date_of_birth: User's date of birth (MM/DD/YYYY)
            expected_success_message: Expected success message text
        """
        RegistrationHelper.navigate_to_registration_page(page)
        RegistrationHelper.fill_registration_form(
            page, first_name, last_name, email, password, phone_number, date_of_birth
        )
        RegistrationHelper.submit_registration(page)
        RegistrationHelper.verify_registration_success(page, expected_success_message)
        framework_logger.info("Complete registration flow executed successfully")
