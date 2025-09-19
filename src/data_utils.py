import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load Airbnb Paris dataset"""
    return pd.read_csv(path, low_memory=False)

def filter_data(df: pd.DataFrame, price_min=10, price_max=500, room_type=None):
    """Filter listings by price and room type"""
    df = df[(df["price"] >= price_min) & (df["price"] <= price_max)]
    if room_type:
        df = df[df["room_type"] == room_type]
    return df