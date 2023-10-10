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

    driver.find_element(By.XPATH,"//span[contains(text(),'Zaloguj')]//parent::*[@class='button']").click()
    time.sleep(2)

    login_title = driver.find_element(By.XPATH, "//h1[@class='title']").text
    assert login_title == "Zacznijmy od Twojego konta e-mail"
    driver.find_element(By.ID, "email").send_keys("example@mail.com")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    driver.close()
    driver.quit()
    print("Test completed")
