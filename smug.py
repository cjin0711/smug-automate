from selenium import webdriver
#from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

#uses Brave browser as alternative chromium platform
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"

#detaches browser tab from program to prevent premature tab closure
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = options)


#user and pass
user = input("Username: ")
password = input("Password: ")


#retrieve login screen
driver.get("https://secure.smugmug.com/login")

#login
driver.find_element(By.NAME, 'username').send_keys(user)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'sm-login-buttons-container').click()

driver.maximize_window()

#delays element interaction (up to 10s -> timeout) until everything is loaded - explicit wait
wait = WebDriverWait(driver, 10)
upload = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='inline-flex dist_button__IZCSb Header_uploadButton__d600D']")))
upload.click()

#create new gallery
new_gallery = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='uploadoptions_newgallery_button']")))
new_gallery.click()


#gallery name (find by ID doesn't work -> find by NAME)
title = wait.until(EC.presence_of_element_located((By.NAME, "Name")))
title.send_keys("12.30.2023 Test Gallery")

'''
#gallery description
desc = wait.until(EC.presence_of_element_located((By.NAME, "Description")))
desc.send_keys("Test description for Gallery")
'''

time.sleep(2)

#gallery creation [needs fixing]
create = wait.until(EC.presence_of_element_located((By.ID, "yui_3_8_0_1_1703959192564_1699")))
create.click()


















    


