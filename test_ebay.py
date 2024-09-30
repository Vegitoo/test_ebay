import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    yield driver
    driver.quit()

def test_ebay_search(setup):
    driver = setup
    search_box = driver.find_element(By.NAME, "_nkw")
    search_box.send_keys("Laptop")
    search_box.send_keys(Keys.RETURN)
    assert "Laptops & Netbooks" in driver.page_source, "Nie znaleziono sekcji 'Laptops & Netbooks'."

