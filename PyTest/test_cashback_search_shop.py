from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_page():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://cashback.opera.com/pl/")
    time.sleep(2)

    driver.find_element(By.XPATH,"//input[@placeholder='Szukaj sklepu...']").send_keys("Allegro")
    time.sleep(2)

    driver.find_element(By.XPATH,"//header/div/div/div[4]/div[@data-test-handle='search-autocomplete-list']/a").click()
    time.sleep(2)

    title = driver.title
    assert title == "Allegro - Cashback - Polska | Opera Cashback"

    driver.close()
    driver.quit()
    print("Test completed")
