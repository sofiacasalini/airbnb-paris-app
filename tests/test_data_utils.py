import pandas as pd
from src.data_utils import filter_data

def test_filter_data():
    df = pd.DataFrame({
        "price": [50, 200, 600],
        "room_type": ["Entire home/apt", "Private room", "Shared room"]
    })
    out = filter_data(df, 10, 500, "Private room")
    assert len(out) == 1
    assert out.iloc[0]["room_type"] == "Private room"
