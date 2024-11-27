
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_01_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    alert_danger_color = "rgba(248, 215, 218, 1)"
    zip_code = driver.find_element(By.ID, "zip-code")
    color_zip = zip_code.value_of_css_property("background-color")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    alert_success_color = "rgba(209, 231, 221, 1)"
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_name in fields:
        field = driver.find_element(By.CSS_SELECTOR, f"[id='{field_name}']")
        field_color = field.value_of_css_property("background-color")
        assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"

    driver.quit()