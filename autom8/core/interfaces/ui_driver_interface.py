from abc import ABCMeta, abstractmethod
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

from autom8.core.interfaces.ui_element_interface import UiElementInterface


class UiDriverInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_driver(self) -> WebDriver: ...

    @abstractmethod
    def goto(self, url: str): ...

    @abstractmethod
    def find_element(self, selector: str, by: Optional[int]): ...

    @abstractmethod
    def close(self): ...

    @abstractmethod
    def back(self): ...

    @abstractmethod
    def forward(self): ...

    @abstractmethod
    def switch_to_tab(self, tab_name: str, index: int): ...

    @abstractmethod
    def switch_to_frame(self, iframe): ...

    @abstractmethod
    def exit_frame(self): ...

    @abstractmethod
    def execute_script(self, script): ...

    @abstractmethod
    def screenshot_page(self, filepath: str): ...

    @abstractmethod
    def highlight_element_and_screenshot_page(self, filepath: str, element_to_highlight: UiElementInterface): ...
