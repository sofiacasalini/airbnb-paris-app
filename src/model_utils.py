import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib, json

def train_model(df: pd.DataFrame, model_path="models/price_model.joblib", meta_path="models/metadata.json"):
    features = ["minimum_nights", "number_of_reviews", "availability_365"]
    target = "price"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    mse = mean_squared_error(y_test, model.predict(X_test))

    joblib.dump(model, model_path)

    metadata = {"features": features, "mse": mse}
    with open(meta_path, "w") as f:
        json.dump(metadata, f)

    return model, metadata

def load_model(model_path="models/price_model.joblib"):
    return joblib.load(model_path)
