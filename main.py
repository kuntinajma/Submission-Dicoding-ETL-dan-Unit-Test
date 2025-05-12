from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, load_to_postgresql

def main():
    try:
        base_url = 'https://fashion-studio.dicoding.dev/'
        all_products = []

        print(f"Scraping main page: {base_url}")
        try:
            products = scrape_main(base_url)
            all_products.extend(products)
        except Exception as e:
            print(f"❌ Gagal scrape halaman utama: {e}")

        for page in range(2, 51):
            url = f"{base_url}page{page}"
            print(f"Scraping page {page}: {url}")
            try:
                products = scrape_main(url)
                all_products.extend(products)
            except Exception as e:
                print(f"❌ Gagal scrape page {page}: {e}")

        print(f"\nTotal produk berhasil di-scrape: {len(all_products)}")

        transformed_data = transform_data(all_products)
        save_to_csv(transformed_data)
        load_to_postgresql(transformed_data)

        save_to_google_sheets(
            transformed_data,
            spreadsheet_id='1PjmzXLfepXqWtLNZyswHsrV4LrWmZNzv11ecsMQXpEs',
            range_name='Sheet1!A1'
        )

    except Exception as e:
        print(f"❌ Kesalahan fatal dalam pipeline ETL: {e}")

if __name__ == '__main__':
    main()