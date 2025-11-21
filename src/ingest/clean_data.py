import pandas as pd

def to_minutes(x):
    if isinstance(x, str) and ("AM" in x or "PM" in x):
        t = pd.to_datetime(x).time()
        return t.hour * 60 + t.minute
    return None 


def clean(df):
    df['last_updated'] = pd.to_datetime(df["last_updated"], errors="coerce")
    
    time_cols = ['sunrise', 'sunset', 'moonrise', 'moonset']

    for i in time_cols: 
        df[i] = df[i].apply(to_minutes)