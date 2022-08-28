from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from autom8.core.enums.browser import Browser


class SeleniumDriverFactory:
    @staticmethod
    def create_new_driver(browser: str):
        match browser:
            case Browser.CHROME.value:
                options = ChromeOptions()
                options.headless = True
                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            case Browser.FIREFOX.value:
                options = FirefoxOptions()
                options.headless = True
                return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            case Browser.EDGE.value:
                options = EdgeOptions()
                options.headless = True
                return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            case _:
                raise Exception(f"Unsupported selenium web driver type: {browser}")
