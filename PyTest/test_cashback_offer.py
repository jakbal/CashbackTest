from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_page():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://cashback.opera.com/pl/")
    time.sleep(2)

    title = driver.title
    assert title == "Opera Cashback | Kupuj i zyskuj pieniądze z powrotem"

    element = driver.find_element(By.XPATH,"//a[@data-test-handle='offer-tile-button'][4]")
    element.location_once_scrolled_into_view
    time.sleep(2)

    element.click()
    time.sleep(2)

    driver.find_element(By.XPATH,"//span[contains(text(),'Zacznij zakupy')]//parent::*[@class='button']").click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID,"popup-sign-in-link").click()
    login_title = driver.find_element(By.XPATH, "//h1[@class='title']").text
    assert login_title == "Zacznijmy od Twojego konta e-mail"

    driver.close()
    driver.quit()
    print("Test completed")
