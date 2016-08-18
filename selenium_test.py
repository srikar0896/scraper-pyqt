from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#import unittest

# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

driver = webdriver.PhantomJS()
try:
    driver.get("https://www.facebook.com/")
    fbUsername = ""
    fbPassword = ""
    emailFieldID = ".//*[@id='email']"
    passFieldID = ".//*[@id='pass']"
    loginButtonXPath = ".//input[@value='Log In']"
    flLogoXpath = "(//a[contains(@href, 'logo')])[1]"
    emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
    passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldID))
    loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))
    emailFieldElement.click()
    emailFieldElement.clear()
    emailFieldElement.send_keys(fbUsername)
    passFieldElement.click()
    passFieldElement.clear()
    passFieldElement.send_keys(fbPassword)
    loginButtonElement.click()
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(flLogoXpath))
    print(str(driver.current_url))
    driver.save_screenshot('Home.png')
except:
    driver.save_screenshot('error.png')
    print("saved screen shot")

driver.quit()
# display.stop()
