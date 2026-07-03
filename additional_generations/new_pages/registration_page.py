"""
Page object for user registration form.
This page handles the complete registration form with all input fields and validation.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class RegistrationPage(BasePageObject):
    """Page object for the user registration page."""

    def __init__(self, page: Page):
        super().__init__(page)
        
        # Form container
        self.elements.registration_form = "form[id*='registration'], form[class*='registration'], form"
        
        # Input fields
        self.elements.first_name_input = "input[id='firstName'], input[name='firstName'], input[placeholder*='First Name']"
        self.elements.last_name_input = "input[id='lastName'], input[name='lastName'], input[placeholder*='Last Name']"
        self.elements.email_input = "input[id='email'], input[name='email'], input[type='email']"
        self.elements.password_input = "input[id='password'], input[name='password'], input[type='password']:not([id*='confirm'])"
        self.elements.confirm_password_input = "input[id*='confirm'], input[name*='confirm'], input[placeholder*='Confirm']"
        self.elements.phone_number_input = "input[id='phone'], input[name='phone'], input[type='tel']"
        self.elements.date_of_birth_input = "input[id='dob'], input[name='dob'], input[type='date']"
        
        # Buttons
        self.elements.register_button = "button[type='submit'], button:has-text('Register'), button:has-text('Sign Up'), button:has-text('Create Account')"
        
        # Validation error messages
        self.elements.first_name_validation_error = "#firstName-error, .error-message:near(input[id='firstName'])"
        self.elements.last_name_validation_error = "#lastName-error, .error-message:near(input[id='lastName'])"
        self.elements.email_validation_error = "#email-error, .error-message:near(input[id='email'])"
        self.elements.password_validation_error = "#password-error, .error-message:near(input[id='password'])"
        self.elements.confirm_password_validation_error = "#confirmPassword-error, .error-message:near(input[id*='confirm'])"
        self.elements.phone_validation_error = "#phone-error, .error-message:near(input[id='phone'])"
        self.elements.dob_validation_error = "#dob-error, .error-message:near(input[id='dob'])"
        self.elements.form_submission_error = ".form-error, .submission-error, #formError, .alert-danger"
        
        # Loading and status indicators
        self.elements.loading_indicator = ".spinner, .loading, #loadingIndicator, .progress"
        self.elements.password_strength_indicator = ".password-strength, #passwordStrength"
        self.elements.password_match_indicator = ".password-match-icon, .match-indicator"
        
        # Date picker widget (if present)
        self.elements.date_picker_widget = ".date-picker, .calendar-widget, .datepicker"

    def select_date_of_birth(self, date_string):
        """
        Selects or enters the date of birth.
        Handles both direct input and date picker widgets.
        
        Args:
            date_string: Date in format MM/DD/YYYY or DD/MM/YYYY
        """
        try:
            # Try direct input first
            self.date_of_birth_input.fill(date_string)
        except Exception:
            # If direct input fails, try clicking to open date picker
            self.date_of_birth_input.click()
            # Wait for date picker to appear
            self.page.wait_for_timeout(1000)
            # Try filling again
            self.date_of_birth_input.fill(date_string)
