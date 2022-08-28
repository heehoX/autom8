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
