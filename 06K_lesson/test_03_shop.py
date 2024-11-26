from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_03_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standart_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-card-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-card-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-card-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shoping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Kate")
    driver.find_element(By.ID, "last-name").send_keys("Alekseeva")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_value = total_element.text
    assert total_value == "Total: $58.29"

    driver.quit()