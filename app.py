import streamlit as st
import pandas as pd
import data_utils
import model_utils
import json

st.title("🏠 Paris Airbnb - price explorer & predictor")

# Load data
DATA_PATH = "data/listings.csv.gz"
df = data_utils.load_data(DATA_PATH)

# Sidebar filters
st.sidebar.header("Filters")
price_range = st.sidebar.slider("Price range", 10, 500, (50, 200))
room_type = st.sidebar.selectbox("Room type", options=[None] + list(df["room_type"].unique()))

# Filtered dataset
filtered = data_utils.filter_data(df, price_range[0], price_range[1], room_type)
st.write(f"Showing {len(filtered)} listings")
st.dataframe(filtered.head(20))

# Price distribution
st.subheader("Price distribution")
st.bar_chart(filtered["price"].value_counts().sort_index())

# Prediction section
st.subheader("💡 Price prediction")
min_nights = st.number_input("Minimum nights", 1, 365, 3)
reviews = st.number_input("Number of reviews", 0, 500, 10)
avail = st.slider("Availability (days/year)", 0, 365, 180)

model = model_utils.load_model()
with open("models/metadata.json") as f:
    meta = json.load(f)

features = [[min_nights, reviews, avail]]
pred = model.predict(features)[0]
st.write(f"💰 Predicted price: €{pred:.2f}")
