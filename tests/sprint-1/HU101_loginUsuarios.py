import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#chromediver download from selenium-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
from dotenv import load_dotenv
import time

load_dotenv()
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')


#HU101
# Ingresar con los datos de tres tipos de 
# usuario y verificar que puedan acceder a sus componentes


class LoginPageTest(unittest.TestCase):

    USER_LOG = os.getenv('USER_LOG')
    USER_PASS = os.getenv('USER_PASS')
    USER_NAME = os.getenv('USER_NAME')

    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    TRAINER_LOG = os.getenv('TRAINER_LOG')
    TRAINER_PASS = os.getenv('TRAINER_PASS')
    TRAINER_NAME = os.getenv('TRAINER_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_adminLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(PAGE_ADDRESS + "/login")
        self.assertIn("Athletic", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.ADMIN_LOG)

        passField.click()
        passField.send_keys(self.ADMIN_PASS)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        # try:
        #     elem = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div")) #This is a dummy element
        #     )
        # finally:
        #     self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div").text, self.ADMIN_NAME)

        time.sleep(2)
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div/div").text, self.ADMIN_NAME)

        


    def test_userLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(PAGE_ADDRESS + "/login")
        self.assertIn("Athletics", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.USER_LOG)

        passField.click()
        passField.send_keys(self.USER_PASS)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        # try:
        #     elem = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div")) #This is a dummy element
        #     )
        # finally:
        #     self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div").text, self.USER_NAME)      

        time.sleep(2)
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div/div").text, self.USER_NAME)      


    def test_trainerLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(PAGE_ADDRESS + "/login")
        self.assertIn("Athletic", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.TRAINER_LOG)

        passField.click()
        passField.send_keys(self.TRAINER_PASS)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        # try:
        #     elem = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div")) #This is a dummy element
        #     )
        # finally:
        #     self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div").text, self.TRAINER_NAME)

        time.sleep(2)
        self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div/div").text, self.TRAINER_NAME)


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 