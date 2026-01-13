from bs4 import BeautifulSoup
import re


def extract_prices(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    prices = []

    rows = soup.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 2:
            continue

        size = cols[0].get_text(strip=True)
        price_text = cols[1].get_text(strip=True)

        price = _parse_price(price_text)

        prices.append({
            "size": size,
            "price": price
        })

    return prices


def _parse_price(text: str) -> float:
    cleaned = re.sub(r"[^\d,\.]", "", text)
    return float(cleaned.replace(",", "."))
