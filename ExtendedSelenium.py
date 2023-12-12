from RPA.Browser.Selenium import Selenium, keyword
from selenium.webdriver import ChromeOptions

# Configure custom preferences for the browser here.
CUSTOM_PREFS = {
    "plugins.plugins_disabled": ["Chrome PDF Viewer"],
    "plugins.always_open_pdf_externally": True,
    "download.prompt_for_download": False,
    "plugins.disable_popup_blocking": False,
    "profile.password_manager_enabled": False,
    "credentials_enable_service": False,
}
DEFAULT_ALIAS = "CUSTOM_BROWSER"


class ExtendedSelenium(Selenium):
    """Extends selenium to open a browser with a custom configuration."""

    @keyword
    def open_configured_available_browser(self, alias: str = DEFAULT_ALIAS):
        """Opens the browser with custom configuration."""
        # Using Robocorp's "Open Available Browser" keyword will download
        # the webdriver automatically and still set the custom preferences.
        return self.open_available_browser(
            maximized=True,
            browser_selection="Chrome",
            alias=alias,
            preferences=CUSTOM_PREFS,
        )

    @keyword
    def open_custom_webdriver(self, alias: str = DEFAULT_ALIAS):
        """Does not use the RPA Framework "Open Available Browser" keyword.
        to generate a custom webdriver.
        """
        # Configure ChromeOptions directly
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", CUSTOM_PREFS)
        # This will only work if the webdriver is already installed.
        return self.create_webdriver("Chrome", options=options, alias=alias)
