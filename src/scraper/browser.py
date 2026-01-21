import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click_button_menu(drive: WebDriver) -> None:
    button_menu = WebDriverWait(drive, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title = 'CARDÁPIO']"))
    )
    button_menu.click()


def click_button_details(drive: WebDriver) -> list[str]:
    list_page_html: list[str] = []
    actions = ActionChains(drive)
    button_details = WebDriverWait(drive, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//button[normalize-space()='+DETALHES']")
        )
    )

    for button in button_details:
        try:
            drive.execute_script("arguments[0].scrollIntoView(true);", button)  # type: ignore
            drive.execute_script("arguments[0].click()", button)  # type: ignore

            time.sleep(1)

            html_page = drive.page_source
            list_page_html.append(html_page)

            actions.pause(2).send_keys(Keys.ESCAPE).perform()
        except Exception as error:
            print(f"Erro: {error}")
    # html = list_page_html[0]
    # with open('index.html', 'w', encoding='utf-8') as f:
    #     f.write(html)
    return list_page_html


def click_after_button(drive: WebDriver) -> list[str]:
    list_all_category: list[str] = []

    while True:
        try:
            html_pages = click_button_details(drive)
            list_all_category.extend(html_pages)

            after = WebDriverWait(drive, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[aria-label='Próximo page']")
                )
            )

            after.click()
            time.sleep(1.2)

        except TimeoutException:
            break
    return list_all_category


def click_category(drive: WebDriver, names_category: list[str]) -> None:
    pratos = "Pratos"
    jump = False

    drive.execute_script("window.scrollTo(0, 0);")  # type: ignore

    for indice, category in enumerate(names_category):
        if jump:
            jump = False
            continue
        try:
            drive.execute_script("window.scrollTo(0, 0);")  # type: ignore
            categories = WebDriverWait(drive, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//button[normalize-space()='{category}']")
                )
            )

            time.sleep(2)
            categories.click()

            if category == pratos:
                next_index = indice + 1
                if next_index < len(names_category):
                    next_category = names_category[next_index]

                    next = WebDriverWait(drive, 5).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"//button[normalize-space()='{next_category}']")
                        )
                    )
                    next.click()
                    jump = True

            click_after_button(drive)

        except Exception as e:
            print(f"Erro ao processar a categoria {category} {e}")

    time.sleep(2)


def main() -> None:
    list_category = [
        "Bebidas",
        "Calzones",
        "Lanches",
        "Petiscos",
        "Pizzas",
        "Pizzas Doces",
        "Pratos",
        "Saladas",
        "Massas",
        "Executivos",
        "Prato",
        "Peixes",
    ]

    drive = webdriver.Chrome()
    try:
        drive.get("https://www.dardanella.com.br/inicio")
        drive.maximize_window()

        click_button_menu(drive)

        click_category(drive, list_category)

        time.sleep(3)
    except Exception as a:
        print(a)
    finally:
        print("Finalizando...")
        drive.quit()


if __name__ == "__main__":
    main()
