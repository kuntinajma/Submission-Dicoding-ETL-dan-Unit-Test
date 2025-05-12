import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_main(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Gagal mengakses URL: {url}. Detail: {e}")

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

        for card in soup.find_all('div', class_='collection-card'):
            title_tag = card.find('h3', class_='product-title')
            title = title_tag.text.strip() if title_tag else 'Unknown Title'

            price_tag = card.find('div', class_='price-container')
            price = price_tag.text.strip() if price_tag else 'Price Unavailable'

            rating_tag = card.find('p', string=lambda text: text and 'Rating' in text)
            rating = rating_tag.text.strip() if rating_tag else 'No Rating'

            colors_tag = card.find('p', string=lambda text: text and 'Colors' in text)
            colors = colors_tag.text.strip() if colors_tag else 'No Color Info'

            size_tag = card.find('p', string=lambda text: text and 'Size' in text)
            size = size_tag.text.strip() if size_tag else 'No Size Info'

            gender_tag = card.find('p', string=lambda text: text and 'Gender' in text)
            gender = gender_tag.text.strip() if gender_tag else 'No Gender Info'

            products.append({
                'title': title,
                'price': price,
                'rating': rating,
                'colors': colors,
                'size': size,
                'gender': gender,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        print(f"✔ Berhasil scrape {len(products)} produk dari {url}")
        return products

    except Exception as e:
        raise Exception(f"Gagal parsing HTML dari {url}. Detail: {e}")