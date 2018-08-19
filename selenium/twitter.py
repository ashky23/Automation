from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user="********"#use your username ^_^
pwd="*********"#use your password too ^_^ 
browser=webdriver.Firefox(executable_path=r'/home/freakash/python/selenium/geckodriver')
browser.get('https://www.twitter.com')
assert "Twitter" in browser.title
elem=browser.find_element_by_name("session[username_or_email]")
elem.send_keys(user)
elem=browser.find_element_by_name("session[password]")
elem.send_keys(pwd)
browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[1]/form/input[1]').click()

