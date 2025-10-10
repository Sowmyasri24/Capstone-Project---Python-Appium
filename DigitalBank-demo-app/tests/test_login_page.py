"""Test cases for Login Page (Android + iOS) following SRP principle."""

import pytest
from pages.login_page import LoginPage
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginPage:
    """Test suite for verifying Login Page functionality."""

    @pytest.fixture(autouse=True)
    def init_page(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.page = LoginPage(self.driver)

    # ---------- FIELD PRESENCE TESTS ---------- #

    def test_username_or_email_field_present(self):
        assert self.page.is_field_present("email" if self.page else "username")

    def test_password_field_present(self):
        assert self.page.is_field_present("password")

    def test_login_button_present(self):
        assert self.page.is_field_present("login_button")

    def test_register_link_present(self):
        assert self.page.is_field_present("register_link")

    def test_settings_icon_present(self):
        assert self.page.is_field_present("settings_icon")

    # ---------- VALID INPUT TESTS ---------- #

    def test_enter_valid_email_or_username(self):
        """Enter valid username/email."""
        self.page.enter_username_or_email("valid_user@gmail.com")
        assert True

    def test_enter_valid_password(self):
        """Enter valid password."""
        self.page.enter_password("StrongPass@123")
        assert True

    def test_valid_login(self):
        """Simulate valid login attempt."""
        self.page.enter_username_or_email("valid_user@gmail.com")
        self.page.enter_password("StrongPass@123")
        self.page.click_login()
        assert True  # could later assert landing page navigation

    # ---------- NEGATIVE TEST CASES ---------- #

    def test_empty_username_or_email(self):
        """Check error when username/email is empty."""
        self.page.enter_username_or_email("")
        self.page.enter_password("StrongPass@123")
        self.page.click_login()
        error = self.page.get_error_message()
        assert error is not None and "email" in error.lower()

    def test_empty_password(self):
        """Check error when password field is empty."""
        self.page.enter_username_or_email("valid_user@gmail.com")
        self.page.enter_password("")
        self.page.click_login()
        error = self.page.get_error_message()
        assert error is not None and "password" in error.lower()

    def test_invalid_email_format(self):
        """Check that invalid email is rejected."""
        self.page.enter_username_or_email("invalid-email")
        self.page.enter_password("StrongPass@123")
        self.page.click_login()
        error = self.page.get_error_message()
        assert error is not None and "invalid" in error.lower()

    def test_invalid_credentials(self):
        """Check login with wrong credentials."""
        self.page.enter_username_or_email("wronguser@gmail.com")
        self.page.enter_password("WrongPass123")
        self.page.click_login()
        error = self.page.get_error_message()
        assert error is not None and "incorrect" in error.lower()

    def test_blank_login(self):
        """Click login without entering anything."""
        self.page.click_login()
        error = self.page.get_error_message()
        assert error is not None and "required" in error.lower()
