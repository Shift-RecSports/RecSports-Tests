import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#chromediver download from selenium-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

import os
from dotenv import load_dotenv

load_dotenv()
PAGE_ADDRESS = os.getenv('PAGE_ADDRESS')

#HU603
#Comprobar que los usuarios de tipo Administrador
#  puedan agregar anuncios a la plataforma, y que estas 
# puedan ser visibles para los alumnos.

class agregarAnuncios(unittest.TestCase):
    
    ADMIN_LOG = os.getenv('ADMIN_LOG')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    ADMIN_NAME = os.getenv('ADMIN_NAME')

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
 
    def test_agregarAnuncios(self):
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
        #============================LOGIN COMPLETE============================

        time.sleep(2)
        driver.get(PAGE_ADDRESS + "/noticias")
        time.sleep(2)

        botonAgregarAnuncio = driver.find_element(By.XPATH, "/html/body/app-root/div/app-noticias/div/div/div/button/span[2]/div")
        botonAgregarAnuncio.click()
        time.sleep(1)

        #Llenar forms
        tituloNoticia = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[1]/mat-form-field/div[1]/div/div[2]/input")
        tituloNoticia.send_keys("Noticia de prueba")
        time.sleep(1)
        print("🟢 Se ha agregado el Titulo")

        fechaNoticia = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[2]/nz-date-picker/div/input")
        fechaNoticia.click()
        today = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/date-range-popup/div/div/calendar-footer/div/a")
        today.click()
        time.sleep(1)
        print("🟢 Se ha agregado la Fecha")

        horaNoticia = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[3]/nz-time-picker/div/input")
        horaNoticia.send_keys("12:00")
        time.sleep(1)
        print("🟢 Se ha agregado la Hora")

        lugarNoticia = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[4]/mat-form-field/div[1]/div/div[2]/input")
        lugarNoticia.send_keys("Lugar de prueba")
        time.sleep(1)
        print("🟢 Se ha agregado Lugar")

        urlNoticia = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[5]/mat-form-field/div[1]/div/div[2]/input")
        urlNoticia.send_keys("https://www.google.com")
        time.sleep(1)
        print("🟢 Se ha agregado URL")

        imagenNoticia = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[6]/mat-form-field/div[1]/div/div[2]/mat-toolbar/div/input[2]")
        imagenNoticia.send_keys("/Users/aleksandrmorozov/Desktop/RecSports-Tests/tests/recsports_logo.png")
        print("🟢 Se ha agregado la foto")

        tituloNoticia.send_keys(Keys.ESCAPE)
        time.sleep(1)

        #Guardar Noticia
        botonGuardar = driver.find_element(By.XPATH, "/html/body/app-root/div/app-nueva-noticia/div/div/div/form/div/div[8]/div/button[2]/span[2]/div")
        botonGuardar.click()
        time.sleep(2)
        print("🟢 Se ha agregado la Noticia")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 



