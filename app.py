import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
from model_utils import load_model, predict_price
from data_utils import load_data

st.title("🏠 Paris Airbnb price explorer & predictor")

# ------------------------
# Load data with caching
# ------------------------
@st.cache_data
def get_data():
    return load_data("data/listings.csv") 
df = get_data()

# ------------------------
# Data exploration
# ------------------------
st.header("Paris Airbnb prices EDA")

# Map visualization: average price per neighbourhood
st.subheader("Price Distribution by Neighbourhood (Map)")

neigh_prices = df.groupby("neighbourhood_cleansed").agg(
    lat=("latitude", "mean"),
    lon=("longitude", "mean"),
    price=("price", "mean")
).reset_index()

layer = pdk.Layer(
    "ScatterplotLayer",
    data=neigh_prices,
    get_position=["lon", "lat"],
    get_radius=100,
    get_fill_color="[255, 0, 0, 140]",
    pickable=True,
)

view_state = pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=11)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# ------------------------
# Price distribution by month
# ------------------------
st.subheader("Price distribution by month")
df["date"] = pd.to_datetime(df["last_scraped"], errors="coerce")
df["month"] = df["date"].dt.month

fig, ax = plt.subplots()
df.groupby("month")["price"].mean().plot(kind="line", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Average Price (€)")
st.pyplot(fig)

# ------------------------
# Prediction
# ------------------------
st.header("💡Price predictor")

bedrooms = st.number_input("Number of bedrooms", min_value=0, max_value=10, value=1)
neighbourhood = st.selectbox("Neighbourhood", df["neighbourhood_cleansed"].unique())

model = load_model("models/price_model.joblib")
prediction = predict_price(model, {"bedrooms": bedrooms, "neighbourhood_cleansed": neighbourhood})

st.write(f"💡 Predicted price: €{prediction:.2f}")
