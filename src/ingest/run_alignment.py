import pandas as pd
from src.ingest.load_data import load_data
from src.ingest.time_alignment import convert_to_utc, global_grid, align_all

RAW_PATH = "data/raw/GlobalWeatherRepository.csv"
OUT_PATH = "data/interim/aligned-weather.parquet"

def main():
    df = load_data(RAW_PATH)
    df = convert_to_utc(df)
    
    grid = global_grid(df)
    aligned = align_all(df, grid)
    
    aligned.to_parquet(OUT_PATH)
    
if __name__ == "__main__":
    main()