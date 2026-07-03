"""
Test Case ID: C44873515
Title: Verify User Registration Flow
Description: This test case verifies the complete user registration process including form validation, submission, and confirmation
"""

import traceback
import pytest
from core.playwright_manager import PlaywrightManager
from core.settings import framework_logger
from helper.registration_helper import RegistrationHelper
from pages.registration_page import RegistrationPage
from pages.registration_success_page import RegistrationSuccessPage
from playwright.sync_api import expect
import test_flows_common.test_flows_common as common
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.usefixtures("main_execution")
def test_c44873515_verify_user_registration_flow(stage_callback, tc_tracer, reporter):
    tcid = "C44873515"
    current_step = "Step 0"
    current_validation = "Initialization"

    try:
        common.setup()
        
        # Generate unique email for this test run
        timestamp = common.generate_tenant_email().split("@")[0].split("_")[-1]
        unique_email = f"john.doe_{timestamp}@example.com"
        
        # Test data
        FIRST_NAME = "John"
        LAST_NAME = "Doe"
        PASSWORD = "Test@1234"
        PHONE_NUMBER = "1234567890"
        DATE_OF_BIRTH = "01/01/1990"
        EXPECTED_SUCCESS_MESSAGE = "Registration Successful"
        
        framework_logger.info(f"[{tcid}] Test data prepared: email={unique_email}")

        # ── Step 1: Navigate to the registration page ──
        current_step = "Step 1"
        current_validation = "Registration page should be displayed"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            expect(registration_page.registration_form).to_be_visible(timeout=30000)
            stage_callback("step1_registration_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 1: Navigated to registration page successfully")
            reporter.validate(True, f"[{tcid}] Step 1: Navigated to registration page successfully")

        # ── Step 2: Enter valid data in First Name field ──
        current_step = "Step 2"
        current_validation = "First Name should be accepted"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            expect(registration_page.first_name_input).to_have_value(FIRST_NAME, timeout=10000)
            expect(registration_page.first_name_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step2_first_name", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 2: First name '{FIRST_NAME}' accepted")
            reporter.validate(True, f"[{tcid}] Step 2: First name '{FIRST_NAME}' accepted")

        # ── Step 3: Enter valid data in Last Name field ──
        current_step = "Step 3"
        current_validation = "Last Name should be accepted"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            expect(registration_page.last_name_input).to_have_value(LAST_NAME, timeout=10000)
            expect(registration_page.last_name_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step3_last_name", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 3: Last name '{LAST_NAME}' accepted")
            reporter.validate(True, f"[{tcid}] Step 3: Last name '{LAST_NAME}' accepted")

        # ── Step 4: Enter valid email address ──
        current_step = "Step 4"
        current_validation = "Email should be accepted"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            registration_page.email_input.fill(unique_email)
            expect(registration_page.email_input).to_have_value(unique_email, timeout=10000)
            expect(registration_page.email_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step4_email", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 4: Email '{unique_email}' accepted")
            reporter.validate(True, f"[{tcid}] Step 4: Email '{unique_email}' accepted")

        # ── Step 5: Enter valid password ──
        current_step = "Step 5"
        current_validation = "Password should be accepted"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            registration_page.email_input.fill(unique_email)
            registration_page.password_input.fill(PASSWORD)
            expect(registration_page.password_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step5_password", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 5: Password accepted")
            reporter.validate(True, f"[{tcid}] Step 5: Password accepted")

        # ── Step 6: Enter password in Confirm Password field ──
        current_step = "Step 6"
        current_validation = "Confirm Password should match with Password"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            registration_page.email_input.fill(unique_email)
            registration_page.password_input.fill(PASSWORD)
            registration_page.confirm_password_input.fill(PASSWORD)
            expect(registration_page.confirm_password_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step6_confirm_password", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 6: Confirm password matches password")
            reporter.validate(True, f"[{tcid}] Step 6: Confirm password matches password")

        # ── Step 7: Enter valid phone number ──
        current_step = "Step 7"
        current_validation = "Phone number should be accepted"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            registration_page.email_input.fill(unique_email)
            registration_page.password_input.fill(PASSWORD)
            registration_page.confirm_password_input.fill(PASSWORD)
            registration_page.phone_number_input.fill(PHONE_NUMBER)
            expect(registration_page.phone_number_input).to_have_value(PHONE_NUMBER, timeout=10000)
            expect(registration_page.phone_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step7_phone_number", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 7: Phone number '{PHONE_NUMBER}' accepted")
            reporter.validate(True, f"[{tcid}] Step 7: Phone number '{PHONE_NUMBER}' accepted")

        # ── Step 8: Select Date of Birth ──
        current_step = "Step 8"
        current_validation = "Date should be selected"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            registration_page.email_input.fill(unique_email)
            registration_page.password_input.fill(PASSWORD)
            registration_page.confirm_password_input.fill(PASSWORD)
            registration_page.phone_number_input.fill(PHONE_NUMBER)
            registration_page.select_date_of_birth(DATE_OF_BIRTH)
            expect(registration_page.dob_validation_error).not_to_be_visible(timeout=10000)
            stage_callback("step8_date_of_birth", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 8: Date of birth '{DATE_OF_BIRTH}' selected")
            reporter.validate(True, f"[{tcid}] Step 8: Date of birth '{DATE_OF_BIRTH}' selected")

        # ── Step 9: Click on Register button ──
        current_step = "Step 9"
        current_validation = "Registration should be successful and user should be redirected to success page"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            registration_page.first_name_input.fill(FIRST_NAME)
            registration_page.last_name_input.fill(LAST_NAME)
            registration_page.email_input.fill(unique_email)
            registration_page.password_input.fill(PASSWORD)
            registration_page.confirm_password_input.fill(PASSWORD)
            registration_page.phone_number_input.fill(PHONE_NUMBER)
            registration_page.select_date_of_birth(DATE_OF_BIRTH)
            registration_page.register_button.click()
            page.wait_for_load_state("networkidle", timeout=30000)
            expect(registration_page.form_submission_error).not_to_be_visible(timeout=10000)
            stage_callback("step9_form_submitted", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 9: Registration form submitted successfully")
            reporter.validate(True, f"[{tcid}] Step 9: Registration form submitted successfully")

        # ── Step 10: Verify success message ──
        current_step = "Step 10"
        current_validation = "Success message 'Registration Successful' should be displayed"

        with PlaywrightManager() as page:
            RegistrationHelper.navigate_to_registration_page(page)
            registration_page = RegistrationPage(page)
            RegistrationHelper.fill_registration_form(
                page,
                first_name=FIRST_NAME,
                last_name=LAST_NAME,
                email=unique_email,
                password=PASSWORD,
                phone_number=PHONE_NUMBER,
                date_of_birth=DATE_OF_BIRTH
            )
            RegistrationHelper.submit_registration(page)
            
            success_page = RegistrationSuccessPage(page)
            expect(success_page.success_message).to_be_visible(timeout=30000)
            expect(success_page.success_message).to_contain_text(EXPECTED_SUCCESS_MESSAGE, timeout=30000)
            stage_callback("step10_success_message", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 10: Success message '{EXPECTED_SUCCESS_MESSAGE}' displayed")
            reporter.validate(True, f"[{tcid}] Step 10: Success message '{EXPECTED_SUCCESS_MESSAGE}' displayed")

    except Exception as e:
        framework_logger.error(
            f"[{tcid}] Test failed at {current_step} — {current_validation}: "
            f"{e}\n{traceback.format_exc()}"
        )
        reporter.validate(False, f"[{tcid}] FAIL at {current_step} — {current_validation}: {str(e)}")
        raise
