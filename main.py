from scraper.browser import click_button_details
from scraper.extractor import extract_prices

html_pages = click_button_details(drive)

print(f"\nTotal de HTMLs capturados: {len(html_pages)}\n")

for i, html in enumerate(html_pages, start=1):
    print(f"===== MODAL {i} =====")

    prices = extract_prices(html)

    if not prices:
        print("Nenhum preço encontrado\n")
        continue

    for p in prices:
        print(f"Tamanho: {p['size']} | Preço: R$ {p['price']:.2f}")

    print()
