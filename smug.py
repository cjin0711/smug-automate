from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.service import Service
#from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()

#uses Brave browser as alternative chromium
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"

#detaches browser tab from program to prevent premature closure
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = options)


#user and pass
user = input("Username: ")
password = input("Password: ")

#loads login screen
driver.get("https://secure.smugmug.com/login")

driver.find_element(By.NAME, 'username').send_keys(user)
driver.find_element(By.NAME, 'password').send_keys(password)

#driver.find_element(By.CLASS_NAME, 'sm-login-buttons-container').click()





    


