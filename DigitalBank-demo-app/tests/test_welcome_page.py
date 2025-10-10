import pytest
from pages.welcome_page import WelcomePage

@pytest.mark.usefixtures("driver_setup")
class TestWelcomePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.page = WelcomePage(self.driver)

    # ---------- Field Presence Tests ----------
    def test_field_presence_android(self):
        assert self.page.is_element_displayed("android", "welcome_text"), "Welcome text not visible"
        assert self.page.is_element_displayed("android", "account_selection"), "Account selection text missing"
        assert self.page.is_element_displayed("android", "balance_label"), "Balance label not found"

    def test_field_presence_ios(self):
        assert self.page.is_element_displayed("ios", "welcome_label"), "Welcome label missing"
        assert self.page.is_element_displayed("ios", "chart_icon"), "Chart icon not visible"
        assert self.page.is_element_displayed("ios", "atm_button"), "ATM button missing"

    # ---------- Valid Input/Click Tests ----------
    def test_valid_clicks_android(self):
        self.page.click_element("android", "welcome_text")
        self.page.click_element("android", "my_dashboard")
        self.page.click_element("android", "atms")
        self.page.click_element("android", "my_accounts")

    def test_valid_clicks_ios(self):
        self.page.click_element("ios", "welcome_button")
        self.page.click_element("ios", "transfer_button")
        self.page.click_element("ios", "tray_icon")

    # ---------- Negative Test Cases ----------
    def test_invalid_element_android(self):
        with pytest.raises(KeyError):
            self.page.click_element("android", "non_existent_button")

    def test_invalid_element_ios(self):
        with pytest.raises(KeyError):
            self.page.click_element("ios", "wrong_locator")

    def test_hidden_element_check_android(self):
        assert not self.page.is_element_displayed("android", "fake_field"), "Fake field should not exist"
