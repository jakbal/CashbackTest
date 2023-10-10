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

    driver.find_element(By.XPATH,"//h2[contains(text(),'Wszystkie sklepy')]")

    action = webdriver.ActionChains(driver)
    element = driver.find_element(By.XPATH,"//header/div/div/div[5]")
    action.move_to_element(element)
    action.perform()
    time.sleep(2)

    driver.find_element(By.XPATH,"//header/div/div/div[5]/div/div[2]/div[3]").click()
    driver.find_element(By.XPATH,"//h2[contains(text(),'All shops')]")
    driver.find_element(By.XPATH,"//a[@data-test-handle='offer-tile-button'][1]")
    driver.find_element(By.XPATH,"//a[@data-test-handle='offer-tile-button'][6]")
    driver.find_element(By.XPATH,"//a[@data-test-handle='offer-tile-button'][12]")

    driver.close()
    driver.quit()
    print("Test completed")
