import pandas as pd


# convert local time to UTC
def convert_to_utc(df):
    df = df.copy()
    
    df['last_updated'] = (
        df.apply(lambda row: row['last_updated']
                 .tz_localize(row['timezone'], ambiguous='NaT', nonexistent='NaT')
                 .tz_lozalize('UTC'), axis=1
                 )
    )
    
    df.rename(columns={'last_updated': 'UTC'})
    return df

# compute global 6 hour grid
def global_grid(df):
    t_min = df['utc_time'].min()
    t_max = df['utc_time'].max()
    
    grid = pd.data_range(
        start = t_min,
        end = t_max,
        freq = '6H',
        tz = 'UTC'
    )
    
    return grid

# reindex each capital onto the grid
def align_capitals(df_capital, grid):
    out = (
        df_capital
        .set_index('utc_time')
        .reindex(grid)
    )
    
    out['capital'] = df_capital['location_name'].iloc[0]
    
    return out

def align_all(df, grid):
    frames = []
    for cap, sub in df.groupby('location_name'):
        aligned = align_capitals(sub, grid)
        frames.append(aligned)
    
    return pd.concat(frames)