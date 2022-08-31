import os

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_screenshot_page(driver, driver_type):
    driver.goto(url := "https://google.com/")
    driver.screenshot_page(fp := f"./screenshot-{driver_type}.png")
    assert os.path.exists(fp)


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_screenshot_page_highlight_element(driver, driver_type):
    driver.goto(url := "https://google.com/")
    element = driver.find_element("img[alt='Google']", By.CSS_SELECTOR)
    driver.highlight_element_and_screenshot_page(fp := f"./highlighted-screenshot-{driver_type}.png", element)
    assert os.path.exists(fp)