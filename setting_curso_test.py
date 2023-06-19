import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver #indica que se proporciona el objeto "driver" a las pruebas, y después de la ejecución de las pruebas
    driver.quit()

def test_validar_setting_de_curso(driver):
    
    driver.get("")

    # Espera hasta que se cargue completamente la página web
    wait = WebDriverWait(driver, 10)
    correo = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))

    try:
        # Busca el selector de correo electrónico
        correo = driver.find_element(by=By.XPATH, value="//input[@name='email']")
        correo.click()
        correo.send_keys("qa@trainme.cloud")
    except NoSuchElementException:
        print("No se pudo encontrar el elemento de correo electrónico en la página web")

    try:
        # Busca el selector de contraseña
        password = driver.find_element(by=By.XPATH, value="//input[@name='password']")
        password.clear()
        password.send_keys("qwerty")
    except NoSuchElementException:
        print("No se pudo encontrar el elemento de contraseña en la página web")

    # botón de inicio de sesión y se hace click
    boton_inicio_sesion = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    boton_inicio_sesion.click()

    # Espera hasta que se cargue completamente la página de gestión
    wait.until(EC.url_contains("/management"))

    # Verifica que la URL actual contenga el endpoint de gestión
    assert "/management" in driver.current_url, "La validación del endpoint ha fallado"

    try:
        # Esperar a que el botón de cambio de rol sea visible
        boton_cambio_rol = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='headlessui-menu-button-:rp:']")))
        boton_cambio_rol.click()
    except TimeoutException:
        print("No se pudo encontrar el botón de cambio de rol dentro de 30 segundos")

    # Seleccionar el rol deseado
    rol_select = driver.find_element(by=By.XPATH, value="//*[@id=headlessui-menu-button-:r3e:]")
    rol_select.click()

    # seleccion seccion de cursos
    seccion_cursos = driver.find_element(by=By.XPATH, value="//a[contains(text(),'Cursos')]")
    seccion_cursos.click()

    # seleccion de curso deseado
    curso_basic_progra = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/main/div[1]/div[3]/div[4]/div[2]/div[1]/img")
    curso_basic_progra.click()

    # selección de setting's del curso
    setting_curso = driver.find_element(By=By.XPATH, value= "/html/body/div/div/div[1]/div/div[2]/div/div")
    setting_curso.click()

    # introduce el titulo del curso
    title_curso = driver.find_element(by=By.XPATH, value="//input[@name='name']")
    title_curso.click()
    title_curso.send_keys("Curso de programacion avanzada")

    # introduce descripcion del curso
    description_curso = driver.find_element(by=By.XPATH, value="//textarea[@name='description']")
    description_curso.click()
    description_curso.send_keys("Esto es un curso para aprender a usar python con selenium webdriver.")

    # seleccion de disponibilidad del curso
    disponibilidad_curso = driver.find_element(By=By.XPATH, value= "//input[@name='available_course']")
    disponibilidad_curso.click()

    # boton guardar
    boton_guardar = driver.find_element(By=By.XPATH, value= "//button[@type='submit']")
    boton_guardar.click()

    # espera a que aparezca el mensaje de confirmación
    mensaje_confirmacion = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'flex') and contains(@class,'w-full') and contains(@class,'flex-col') and contains(@class,'items-center') and contains(@class,'space-y-4') and contains(@class,'sm:items-end')]")))

    # verifica que el mensaje sea el que esperas
    assert mensaje_confirmacion.text == "Correcto! Se guardó correctamente"

    # Espera 5segundos antes de cerrar el navegador
    time.sleep(5)