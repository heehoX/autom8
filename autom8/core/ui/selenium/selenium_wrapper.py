from autom8.core.interfaces.ui_driver_interface import UiDriverInterface
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumWrapper(UiDriverInterface):
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def get_driver(self) -> WebDriver:
        return self.__driver

    def goto(self, url: str):
        self.__driver.get(url)

    def find_element(self, selector: str, by: str):
        return self.__driver.find_element(by=by, value=selector)

    def close(self):
        self.__driver.close()
        self.__driver.quit()

    def back(self):
        self.__driver.back()

    def forward(self):
        self.__driver.forward()
