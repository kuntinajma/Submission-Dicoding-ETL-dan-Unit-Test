import pandas as pd
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('future.no_silent_downcasting', True)

def transform_data(products):
    print(f"\nJumlah data masuk: {len(products)}")
    
    df = pd.DataFrame(products)

    # Hapus baris dengan title yang mengandung 'unknown'
    df = df[~df['title'].str.lower().str.contains('unknown')]

    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True)
    df['price'] = df['price'].replace('', np.nan)
    df.dropna(subset=['price'], inplace=True)
    df['price'] = df['price'].astype(float) * 16000

    df['rating'] = df['rating'].replace(r'[^0-9.]', '', regex=True)
    df['rating'] = df['rating'].replace('', np.nan)
    df.dropna(subset=['rating'], inplace=True)
    df['rating'] = df['rating'].astype(float)

    df['colors'] = df['colors'].replace(r'\D', '', regex=True)
    df['colors'] = df['colors'].replace('', np.nan)
    df.dropna(subset=['colors'], inplace=True)
    df['colors'] = df['colors'].astype(int)

    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df['timestamp'] = pd.Timestamp.now().isoformat() 

    print(f"Jumlah data valid setelah transformasi: {len(df)}")
    return df