"""
Page object for registration success confirmation page.
This page displays the success message after successful user registration.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class RegistrationSuccessPage(BasePageObject):
    """Page object for the registration success confirmation page."""

    def __init__(self, page: Page):
        super().__init__(page)
        
        # Success message elements
        self.elements.success_message = ".success-message, #successMsg, [class*='success']:has-text('Registration'), h1:has-text('Success'), h2:has-text('Success')"
        self.elements.success_page_heading = "h1, h2, .page-title, .heading"
        self.elements.success_icon = ".success-icon, .checkmark, [class*='icon-success']"
