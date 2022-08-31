from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_navigating_to_url(driver, driver_type):
    driver.goto(url := "https://the-internet.herokuapp.com/")
    assert driver.get_driver().current_url == url


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_finding_element(driver, driver_type):
    driver.goto("https://the-internet.herokuapp.com/login")

    username_field = driver.find_element(selector="username", by=By.ID)
    username_field.clear()
    username_field.type_text(value := "id")
    assert username_field.get_property("value") == value

    username_field = driver.find_element(selector="username", by=By.NAME)
    username_field.clear()
    username_field.type_text(value := "name")
    assert username_field.get_property("value") == value

    username_field = driver.find_element(selector="#username", by=By.CSS_SELECTOR)
    username_field.clear()
    username_field.type_text(value := "css")
    assert username_field.get_property("value") == value

    username_field = driver.find_element(selector="//input[@id='username']", by=By.XPATH)
    username_field.clear()
    username_field.type_text(value := "xpath")
    assert username_field.get_property("value") == value


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_back_and_forward_navigation(driver, driver_type):
    driver.goto("https://the-internet.herokuapp.com")
    driver\
        .find_element('Form Authentication', by=By.LINK_TEXT)\
        .click()

    driver.back()
    assert driver.get_driver().current_url == "https://the-internet.herokuapp.com/"

    driver.forward()
    assert driver.get_driver().current_url == "https://the-internet.herokuapp.com/login"


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_tab_switching(driver, driver_type):
    driver.goto("https://google.com")
    assert driver.get_driver().title == "Google"

    # open new tab, navigate to a page then check if the new page is opened in the new tab and not the old one
    driver.open_new_tab(url="https://duckduckgo.com")
    assert driver.get_driver().current_window_handle == driver.get_driver().window_handles[-1]
    assert driver.get_driver().title == "DuckDuckGo — Privacy, simplified."

    driver.open_new_tab(url="https://the-internet.herokuapp.com/")
    assert driver.get_driver().current_window_handle == driver.get_driver().window_handles[-1]
    assert driver.get_driver().title == "The Internet"

    driver.open_new_tab(url="https://the-internet.herokuapp.com/iframe")
    assert driver.get_driver().current_window_handle == driver.get_driver().window_handles[-1]
    assert driver.get_driver().title == "The Internet"

    # should be able to switch to other tabs
    driver.switch_to_tab('Google')
    assert driver.get_driver().title == "Google"

    driver.switch_to_tab('DuckDuckGo — Privacy, simplified.')
    assert driver.get_driver().title == "DuckDuckGo — Privacy, simplified."

    # and can handle tabs with same names using index
    driver.switch_to_tab('The Internet', index=1)
    assert driver.get_driver().current_url == "https://the-internet.herokuapp.com/iframe"

    driver.switch_to_tab('The Internet', index=0)
    assert driver.get_driver().current_url == "https://the-internet.herokuapp.com/"


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_iframe_switching(driver, driver_type):
    driver.goto("https://the-internet.herokuapp.com/iframe")

    driver.switch_to_frame("mce_0_ifr")
    editor = driver.find_element("body#tinymce", By.CSS_SELECTOR)
    assert editor.is_displayed()

    editor.clear()
    editor.type_text("Hello")
    assert editor.get_text() == "Hello"

    driver.exit_frame()
    with pytest.raises(NoSuchElementException) as e_info:
        driver.find_element("body#tinymce", By.CSS_SELECTOR).is_displayed()


