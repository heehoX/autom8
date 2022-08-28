from selenium.webdriver.common.by import By
import pytest


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_click_element(driver, driver_type):
    driver.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    add_element_button = driver.find_element(selector="button[onclick='addElement()']", by=By.CSS_SELECTOR)
    add_element_button.click()

    delete_element_button = driver.find_element(selector="button[onclick='deleteElement()']", by=By.CSS_SELECTOR)
    assert delete_element_button.is_displayed()


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_textbox_element_interaction(driver, driver_type):
    driver.goto("https://the-internet.herokuapp.com/forgot_password")

    email_textbox = driver.find_element(selector="#email", by=By.CSS_SELECTOR)
    email_textbox.type_text(email := "myemail@emailprovider.com")
    assert email_textbox.get_property('value') == email

    email_textbox.clear()
    assert email_textbox.get_property('value') == ""


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_dropdown_element_interactions(driver, driver_type):
    driver.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(selector="#dropdown", by=By.CSS_SELECTOR)

    dropdown.select_from_dropdown_by_index(1)
    assert dropdown.get_selected_item_from_dropdown() == "Option 1"

    dropdown.select_from_dropdown_by_text("Option 2")
    assert dropdown.get_selected_item_from_dropdown() == "Option 2"

    dropdown.select_from_dropdown_by_value("1")
    assert dropdown.get_selected_item_from_dropdown() == "Option 1"


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_get_an_elements_text(driver, driver_type):
    driver.goto(url := "https://the-internet.herokuapp.com/")

    heading = driver.find_element(selector=".heading", by=By.CSS_SELECTOR)
    assert heading.get_text() == "Welcome to the-internet"


@pytest.mark.unit
@pytest.mark.parametrize("driver_type", ["chrome", "firefox", "edge"])
def test_get_attribute_and_get_property(driver, driver_type):
    driver.goto(url := "https://the-internet.herokuapp.com/login")

    username_field = driver.find_element(selector="#username", by=By.CSS_SELECTOR)
    assert username_field.get_attribute('type') == "text"

    username_field.type_text(uname := "heehoX")
    assert username_field.get_property('value') == uname
