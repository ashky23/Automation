from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path=r"/home/freakash/python/selenium/geckodriver")
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")
#Username Insertion
user=driver.find_element_by_id("identifierId")
user.send_keys("iamakashkumar1999@gmail.com")

driver.find_element_by_css_selector("#identifierNext > content:nth-child(3) > span:nth-child(1)").click()
#waiting for clicking part
time.sleep(2)
#Password Insertion
password=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input")
password.send_keys("12345678xxx")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span").click()
