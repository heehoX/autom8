from abc import ABCMeta, abstractmethod
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver


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

