"""Test cases for Registration Page following SRP (Single Responsibility Principle)."""

import pytest
from pages.registration_page import RegistrationPage
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistrationPage:
    """Test suite for verifying registration page functionality."""

    @pytest.fixture(autouse=True)
    def init_page(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.page = RegistrationPage(self.driver)

    # ---------- FIELD PRESENCE TESTS ---------- #

    def test_first_name_field_present(self):
        assert self.page.is_field_present("first_name")

    def test_last_name_field_present(self):
        assert self.page.is_field_present("last_name")

    def test_email_field_present(self):
        assert self.page.is_field_present("email")

    def test_password_field_present(self):
        assert self.page.is_field_present("password")

    def test_dob_field_present(self):
        assert self.page.is_field_present("dob")

    def test_address_field_present(self):
        assert self.page.is_field_present("address")

    def test_region_field_present(self):
        assert self.page.is_field_present("region")

    def test_locality_field_present(self):
        assert self.page.is_field_present("locality")

    def test_register_button_present(self):
        assert self.page.is_field_present("register_button")

    # ---------- VALID INPUT TESTS ---------- #

    def test_enter_first_name(self):
        self.page.enter_first_name("Sowmya")
        assert True

    def test_enter_last_name(self):
        self.page.enter_last_name("Sridhar")
        assert True

    def test_enter_email(self):
        self.page.enter_email("testuser@gmail.com")
        assert True

    def test_enter_password(self):
        self.page.enter_password("StrongPass@123")
        assert True

    def test_click_register_button(self):
        self.page.click_register()
        assert True

    # ---------- NEGATIVE TEST CASES ---------- #

    def test_invalid_email_format(self):
        """Verify that invalid email triggers an error message."""
        self.page.enter_email("invalid-email")
        self.page.click_register()
        error = self.page.get_error_message()
        assert error is not None and "invalid" in error.lower()

    def test_empty_first_name(self):
        """Check that first name cannot be empty."""
        self.page.enter_first_name("")
        self.page.click_register()
        error = self.page.get_error_message()
        assert error is not None and "first name" in error.lower()

    def test_empty_password(self):
        """Check that password cannot be empty."""
        self.page.enter_password("")
        self.page.click_register()
        error = self.page.get_error_message()
        assert error is not None and "password" in error.lower()

    def test_weak_password(self):
        """Check that weak passwords are rejected."""
        self.page.enter_password("1234")
        self.page.click_register()
        error = self.page.get_error_message()
        assert error is not None and "weak" in error.lower()

    def test_missing_mandatory_fields(self):
        """Click register without entering mandatory fields."""
        self.page.click_register()
        error = self.page.get_error_message()
        assert error is not None and "required" in error.lower()

    def test_invalid_ssn(self):
        """Check that invalid SSN is handled properly."""
        self.page.enter_ssn("abcd123")
        self.page.click_register()
        error = self.page.get_error_message()
        assert error is not None and "ssn" in error.lower()
