import pandas as pd
import numpy as np

SENTINELS = {
    "wind_kph": [2963.2],
    "pressure_mb": [3006],
    "gust_kph": [2970.4],
    "air_quality_Carbon_Monoxide": [-9999, 38879.3],
    "air_quality_Sulphur_dioxide": [-9999],
    "air_quality_PM10": [-1848.15, 6037.29]
}

PHYSICAL_BOUNDS = {
    "wind_kph": (0, 200),
    "gust_kph": (0, 250),
    "pressure_mb": (950, 1050),
    "air_quality_PM2.5": (0, 500),
    "air_quality_PM10": (0, 1000),
    "air_quality_Carbon_Monoxide": (0, 2000),
    "air_quality_Sulphur_dioxide": (0, 200),
    "air_quality_Nitrogen_dioxide": (0, 500),
    "air_quality_Ozone": (0, 600)
}

def clean_sentinels(df):
    for col, sentinels in SENTINELS.items():
        if col in df.columns:
            df[col] = df[col].replace(sentinels, np.nan)
    return df    

def clean_physical_bounds(df):
    for col, (low, high) in PHYSICAL_BOUNDS.items():
        if col in df.columns:
            df[col] = df[col].where((df[col] >= low) & (df[col] <= high), np.nan)
    return df
            


def clean(df):
    df['last_updated'] = pd.to_datetime(df["last_updated"], errors="coerce")
    df = clean_sentinels(df)
    df = clean_physical_bounds(df)
    
    return df