import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

load_dotenv()
PATH = os.getenv('PATH')
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')

#HU102
# Verificar que cada usuario pueda 
# verificar que puedan acceder a sus componentes 
# en la página principal 

class MenuPrincipalTest(unittest.TestCase):

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
        self.driver = webdriver.Chrome(PATH)
    
    def test_menuAdmin(self):
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
        loginField.send_keys(self.ADMIN_LOG)

        passField.click()
        passField.send_keys(self.ADMIN_PASS)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav/div")) #This is a dummy element
            )
        finally:
            self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div/div").text, self.ADMIN_NAME)

        assert driver.find_element(By.XPATH, "//*[@id='bar-card']/div")
        print("🟢 ADMIN Stats OK")
        assert driver.find_element(By.XPATH, "//*[@id='donut-card']")
        print("🟢 ADMIN Aforo OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/div[2]/div[1]/div/app-news/nz-carousel")
        print("🟢 ADMIN Anuncios OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/div[2]/div[2]/div")
        print("🟢 ADMIN Deportes OK")


    def test_menuUser(self):
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
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav/div")) #This is a dummy element
            )
        finally:
            self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div/div").text, self.USER_NAME)  

        assert driver.find_element(By.XPATH, "//*[@id='bar-card']/div")    
        print("🟢 USER Stats OK")
        assert driver.find_element(By.XPATH, "//*[@id='donut-card']")
        print("🟢 USER Aforo OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/div[2]/div[1]/div/app-news/nz-carousel")
        print("🟢 USER Anuncios OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/div[2]/div[2]/div")
        print("🟢 USER Deportes OK")
    

    def test_menuTrainer(self):
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
        loginField.send_keys(self.TRAINER_LOG)

        passField.click()
        passField.send_keys(self.TRAINER_PASS)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav/div")) #This is a dummy element
            )
        finally:
            self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/div[2]/button/span[2]/div/div").text, self.TRAINER_NAME)

        assert driver.find_element(By.XPATH, "//*[@id='bar-card']/div")
        print("🟢 TRAINER Stats OK")
        assert driver.find_element(By.XPATH, "//*[@id='donut-card']")
        print("🟢 TRAINER Aforo OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home-entrenador/div/div/div[2]/div[1]/div/div/button")
        print("🟢 TRAINER IN OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home-entrenador/div/div/div[2]/div[2]/div/div/button")
        print("🟢 TRAINER OUT OK")



        

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 