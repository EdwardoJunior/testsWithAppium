from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {
    "platformName" : "Android",
    "platformVersion": "11",
    "deviceName" : "emulator-5554",
    "app": "C:/Users/Edu/Documents/Integradora/APPMOBILE/Socialert/app/build/intermediates/apk/debug/app-debug.apk",
    "automationName" : "UiAutomator2",
    "noReset": True,
    "fullContextList": True
}




appium_options = AppiumOptions()
appium_options.load_capabilities(desired_caps)

try:
    driver = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)
    print("Driver inicializado correctamente")
except Exception as e:
    print(f"Error al iniciar el driver: {e}")
    driver = None

def test_login():
    if driver:
        time.sleep(5)
        try:
            email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "emailFieldLogin")))
            email.click()
            driver.execute_script("mobile: type", {"text": "edu@gmail.com"})
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "passwordFieldLogin").click()
            driver.execute_script("mobile: type", {"text": "Hola1123!"})
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'loginButton').click()

            time.sleep(5)
            driver.quit()
        except Exception as e:
            print(f"Prueba fallida: {e}")
    else:
        print("No se pudo iniciar el driver, no se puede realizar la prueba.")

test_login()