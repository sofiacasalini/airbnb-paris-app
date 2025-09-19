import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load Airbnb Paris dataset"""
    df = pd.read_csv(path, low_memory=False)
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
    df = df.dropna(subset=["price"])
    return df

def filter_data(df: pd.DataFrame, price_min=10, price_max=500, room_type=None):
    """Filter listings by price and room type"""

    df = df[(df["price"] >= price_min) & (df["price"] <= price_max)]
    if room_type:
        df = df[df["room_type"] == room_type]
    return df