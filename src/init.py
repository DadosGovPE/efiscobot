from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import dotenv_values


ENV = dotenv_values(".env")
URL = ENV['URL_LOGIN']
CPF = ENV['CPF']

def config(path_folder: str, headless: bool):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("geo.enabled", False)
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", path_folder)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")
    fp.set_preference("dom.disable_beforeunload", True)
    fp.set_preference("browser.download.manager.closeWhenDone", True)

    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument('-headless')

    driver = webdriver.Firefox(fp, options=options)

    return driver
    

if __name__ == "__main__":    
    
    '''
    CRIANDO UM WEBDRIVER E SUBMETENDO AO LOGIN

    PROBLEMA: COMO PASSAR O CAPTCHA?


    '''

    driver = config(".", False)
    driver.get(URL)

    secs = 15
    try:        
        # Espera pelo input field
        login_button = WebDriverWait(driver, secs).until(
            EC.element_to_be_clickable((By.ID, "btt_ok"))
        )
        login_button.click()
        
        # Espera pelo input field
        account_id_input = WebDriverWait(driver, secs).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#accountId[name='accountId']"))
        )
        account_id_input.send_keys(CPF)

        # Espera pelo o botão de continuar
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#enter-account-id.button-continuar"))
        )
        submit_button.click()

        print("Login realizado.")

    except TimeoutException:
        print("Timed out.")
    except NoSuchElementException:
        print("Um ou mais elementos não encontrados.")
    except Exception as e:
        print(f"Erro: {str(e)}")
