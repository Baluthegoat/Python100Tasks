#https://www.geeksforgeeks.org/gmail-login-using-python-selenium/
#https://www.testim.io/blog/selenium-click-button/
#https://www.google.com/search?q=selenioum+clicking+a+button&oq=selenioum+clicking+a+button&aqs=chrome..69i57j0i13i512j0i22i30l8.4055j0j7&sourceid=chrome&ie=UTF-8

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def system():
     driver = webdriver.Chrome()
     driver.get("https://www.classroom.google.com/")
     driver.maximize_window()
     try:
     
          sign_in_button = driver.find_element(By.XPATH,'//*[@id="gfe-main-content"]/section[1]/div/div/div[1]/div/div/div/ul/li[2]/a')
          time.sleep(2)
          sign_in_button.click()
          time.sleep(2)
          p = driver.current_window_handle

     
          chwd = driver.window_handles

          for w in chwd:
               if(w!=p):
                    driver.switch_to.window(w)
          username = "02230306.cst@rub.edu.bt"
          password = "Ds(53)22-32190"

          loginBox = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
          time.sleep(2)
          loginBox.send_keys(username)
          time.sleep(2)
          b = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
          time.sleep(2)
          b.click()
          time.sleep(2)
          pwBow = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
          time.sleep(2)
          pwBow.send_keys(password)
          time.sleep(2)
          pwb = driver.find_element(By.ID,'passwordNext')
          pwb.click()
          time.sleep(300)

     except Exception as e:
          print(f"An error occurred: {str(e)}")

system()


