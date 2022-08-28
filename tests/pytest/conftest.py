import pytest

from autom8.core.ui.selenium.selenium_webdriver_factory import SeleniumDriverFactory
from autom8.core.ui.selenium.selenium_webdriver_wrapper import SeleniumWebdriverWrapper


@pytest.fixture
def driver(request):
    driver_type = request.node.callspec.params['driver_type']
    driver = SeleniumWebdriverWrapper(SeleniumDriverFactory.create_new_driver(driver_type))
    yield driver
    driver.close()
