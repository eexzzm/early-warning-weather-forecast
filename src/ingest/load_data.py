from   src.clean.clean_data import clean

def load_data(path):
    import pandas as pd
    df = pd.read_csv(path)
    df = clean(df)
    
    return df