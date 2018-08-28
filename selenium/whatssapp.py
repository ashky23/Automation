from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
browser=webdriver.Firefox(executable_path=r"/home/freakash/python/selenium/geckodriver")
browser.get("https://web.whatsapp.com")
wait=WebDriverWait(browser,600)
target='"Pk"'
x_arg='//span[contains(@title,' + target + ')]'
group_title=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
group_title.click()
text='/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]'
group_title=wait.until(EC.presence_of_element_located((By.XPATH,text)))
group_title.click()
string="Write the message to send to your friend:"
for i in range(100):
    group_title.send_keys(string+Keys.ENTER)
    time.sleep(1)

