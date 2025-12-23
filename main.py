import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def button_menu(drive):
    button_menu = WebDriverWait(drive, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title = 'CARDÁPIO']"))
    )
    button_menu.click()

def button_datils(drive):
    actions = ActionChains(drive)
    button_details = WebDriverWait(drive, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[normalize-space()='+DETALHES']"))
    )

    for button in button_details:
        try:
            drive.execute_script('arguments[0].scrollIntoView(true);', button)
            drive.execute_script('arguments[0].click()', button)

            time.sleep(2)

            actions.send_keys(Keys.ESCAPE).perform()
        except Exception as error:
            print(f'Erro: {error}')

def after_button(drive):
    before = WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a/span[normalize-space()='2']"))
    )

    before.click()

def main():
    drive = webdriver.Chrome()
    drive.get('https://www.dardanella.com.br/inicio')
    drive.maximize_window()
    
    button_menu(drive)

    time.sleep(2)
    button_datils(drive)

    after_button(drive)

    time.sleep(3)
    drive.quit()


if __name__ == '__main__':
    main()