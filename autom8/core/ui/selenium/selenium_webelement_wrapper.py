from selenium.webdriver.support.select import Select

from autom8.core.interfaces.ui_element_interface import UiElementInterface
from selenium.webdriver.remote.webdriver import WebElement


class SeleniumWebElementWrapper(UiElementInterface):
    def __init__(self, element: WebElement):
        self.__element = element

    def click(self):
        self.__element.click()

    def type_text(self, text: str):
        self.__element.send_keys(text)

    def clear(self):
        self.__element.clear()

    def select_from_dropdown_by_value(self, value: str):
        Select(self.__element).select_by_value(value)

    def select_from_dropdown_by_index(self, index: int):
        Select(self.__element).select_by_index(index)

    def select_from_dropdown_by_text(self, text: str):
        Select(self.__element).select_by_visible_text(text)

    def get_selected_item_from_dropdown(self):
        return Select(self.__element).first_selected_option.text

    def get_text(self):
        return self.__element.text

    def get_property(self, property_name: str):
        return self.__element.get_property(property_name)

    def get_attribute(self, attribute_name: str):
        return self.__element.get_attribute(attribute_name)

    def is_displayed(self):
        return self.__element.is_displayed()
