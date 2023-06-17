# RecSports Tests
 
 ## Plan de Calidad con Diseño de Pruebas: 

https://docs.google.com/document/d/1-amnV6iuXhx_A3xUtCt1cPubFINTjR3GcDD8J0FHs4c/edit?usp=sharing 
 
 ## Tests de Software RecSports

 Repositorio de Pruebas aplicación web con Angular con conexión a baso de datos en MySQL y API de Javascript.


## Guia de Instalación macOS

Tabla de versiones y software requerido
| Software/Framework  | Version | Link de Descarga  | 
| ------------- | ------------- | ------------- |
| Python  | 3.10 | |
| Python Selenium Library | 4.9.1 | |
| Chrome | 113.0.5672.126 | |
| Chrome Driver | 113.0.5672.63 | https://chromedriver.chromium.org/downloads |
| WebDriver Manager | | https://github.com/SergeyPirogov/webdriver_manager |
| Python dotenv Library | | pip install python-dotenv |
 
1. Verificar que el sistema cumple con los requisitos de las versiones.
2. Clonar repositorio.
3. Crear archivo .env

```
PATH = " "   #Proporcionar el path hacia el chromedriver, ej. /Users/*user*/Desktop/RecSports-Tests/chromedriver"
PAGE_ADDRESS = " "  #Proporcionar URL de front-end, ej. "http://localhost:4200"

#Llenar los credenciales de los usuarios acorde al back-end.

#Admin Credentials
ADMIN_LOG =  " " 
ADMIN_PASS = " "
ADMIN_NAME = " "

#User Credentials
USER_LOG = " "
USER_PASS = " "
USER_NAME = " "

#Trainer Credentials
TRAINER_LOG = " "
TRAINER_PASS = " "
TRAINER_NAME = " "
```

4. Para correr la prueba deciada a seguir siguentes pasos: <br /> 
 a. cd RecSports-Tests <br /> 
   b. cd tests <br /> 
   c. cd sprint-[1,2, .. ] <br /> 
   d. python [102, 103...]_nombreDeLaPrueba.py

 ## Video de demostración de fincionamiento de las pruebas:
 
https://drive.google.com/drive/folders/1-VlUA5PG07F213LY0G1oouMiVxF9c8Vm?usp=sharing

