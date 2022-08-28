from abc import ABCMeta, abstractmethod
from typing import Optional

from selenium.webdriver.remote.webdriver import WebElement


class UiElementInterface(metaclass=ABCMeta):
    @abstractmethod
    def click(self): ...

    @abstractmethod
    def type_text(self, text: str): ...

    @abstractmethod
    def clear(self): ...

    @abstractmethod
    def select_from_dropdown_by_value(self, value: str): ...

    @abstractmethod
    def select_from_dropdown_by_index(self, index: int): ...

    @abstractmethod
    def select_from_dropdown_by_text(self, text: str): ...

    @abstractmethod
    def get_selected_item_from_dropdown(self): ...

    @abstractmethod
    def get_text(self): ...

    @abstractmethod
    def get_property(self, property_name: str): ...

    @abstractmethod
    def get_attribute(self, attribute_name: str): ...

    @abstractmethod
    def is_displayed(self): ...
