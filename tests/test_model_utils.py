import pandas as pd
from model_utils import train_and_save_model, load_model, predict_price


def test_model_training(tmp_path):
    df = pd.DataFrame({
        "bedrooms": [1, 2, 3],
        "neighbourhood_cleansed": ["A", "B", "C"],
        "price": [100, 150, 200]
    })
    model_path = tmp_path / "model.joblib"
    model = train_and_save_model(df, path=model_path)
    assert model is not None

def test_prediction():
    df = pd.DataFrame({
        "bedrooms": [1, 2],
        "neighbourhood_cleansed": ["A", "B"],
        "price": [100, 200]
    })
    model = train_and_save_model(df)
    pred = predict_price(model, {"bedrooms": 1, "neighbourhood_cleansed": "A"})
    assert isinstance(pred, float)