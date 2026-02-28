import pytest
from src.config import BASE_URL, VALID_USER, VALID_PASS
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load(BASE_URL)
    login_page.login(VALID_USER, VALID_PASS)

    assert inventory_page.get_title() == "Products"


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.load(BASE_URL)
    login_page.login("invalid_user", "wrong_pass")

    assert "Epic sadface" in login_page.get_error_message()
