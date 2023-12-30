from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#delays element interaction until everything is loaded - explicit wait
wait = WebDriverWait(driver, 10)
upload = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='inline-flex dist_button__IZCSb Header_uploadButton__d600D']")))
upload.click()

#create new gallery
new_gallery = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='uploadoptions_newgallery_button']")))
new_gallery.click()

#[needs fixing]
title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='yui_3_8_0_1_1703913908150_1694']")))
title.send_keys("12.30.2023 Test Gallery")
















    


