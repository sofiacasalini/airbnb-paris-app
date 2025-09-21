import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer


def train_and_save_model(df, path="models/price_model.joblib"):
    features = ["bedrooms", "neighbourhood_cleansed"]
    X = df[features]
    y = df["price"]

    # Preprocessing: handle missing values + scale numeric + one-hot encode categorical
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("imputer", SimpleImputer(strategy="median")),  # fill missing numeric
                ("scaler", StandardScaler())
            ]), ["bedrooms"]),
            ("cat", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),  # fill missing categorical
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ]), ["neighbourhood_cleansed"])
        ]
    )

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, path)
    return pipeline

def load_model(path="models/price_model.joblib"):
    return joblib.load(path)

def predict_price(model, inputs: dict):
    df_input = pd.DataFrame([inputs])
    return model.predict(df_input)[0]
