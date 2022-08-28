from typing import Optional

from autom8.core.interfaces.ui_driver_interface import UiDriverInterface
from selenium.webdriver.remote.webdriver import WebDriver

from autom8.core.ui.selenium.selenium_webelement_wrapper import SeleniumWebElementWrapper


class SeleniumWebdriverWrapper(UiDriverInterface):
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def get_driver(self) -> WebDriver:
        return self.__driver

    def goto(self, url: str):
        self.__driver.get(url)

    def find_element(self, selector: str, by: str):
        return SeleniumWebElementWrapper(self.__driver.find_element(by=by, value=selector))

    def close(self):
        self.__driver.close()
        self.__driver.quit()

    def back(self):
        self.__driver.back()

    def forward(self):
        self.__driver.forward()

    def switch_to_tab(self, tab_name: str, index: int = 0):
        """Switch to tab by looking at the tab name
        if there is an expected duplicate, pass in the
        index."""
        tabs = self.__driver.window_handles
        for tab in tabs:
            counter = 0
            self.__driver.switch_to.window(tab)
            if self.__driver.title == tab_name:
                if counter == index:
                    return
                counter += 1

    def open_new_tab(self, url: str = ""):
        self.__driver.switch_to.new_window()

        if url:
            self.goto(url)

    def switch_to_frame(self, iframe_selector: str):
        self.__driver.switch_to.frame(iframe_selector)

    def exit_frame(self):
        self.__driver.switch_to.default_content()
