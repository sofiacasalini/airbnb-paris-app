import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.colorbar import ColorbarBase
from model_utils import train_and_save_model, load_model, predict_price
from data_utils import load_data

st.title("🏠 Paris Airbnb price explorer & predictor")

# ------------------------
# Load data with caching
# ------------------------
@st.cache_data
def get_data():
    df = load_data("data/listings.csv")
    df["price"] = (
        df["price"]
        .replace('[\€,]', '', regex=True)  # remove € and commas
        .astype(float)
    )
    return df
df = get_data()

# ------------------------
# Data exploration
# ------------------------
# Map visualization: average price per neighbourhood
st.header("Price distribution by neighbourhood")

neigh_prices = df.groupby("neighbourhood_cleansed").agg(
    lat=("latitude", "mean"),
    lon=("longitude", "mean"),
    price=("price", "mean")
).reset_index()

# Create colormap for Pydeck
min_price = neigh_prices["price"].min()
max_price = neigh_prices["price"].max()
cmap = cm.get_cmap("coolwarm")
norm = colors.Normalize(vmin=min_price, vmax=max_price)

# Apply color mapping
neigh_prices["color"] = neigh_prices["price"].apply(
    lambda p: [int(x*255) for x in cmap(norm(p))[:3]] + [180]  # RGB + alpha
)

# ScatterplotLayer
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=neigh_prices,
    get_position=["lon", "lat"],
    get_radius=200,
    get_fill_color="color",
    pickable=True,
)

view_state = pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=11)
st.pydeck_chart(pdk.Deck(layers=[scatter_layer], initial_view_state=view_state))

# ------------------------
# Colorbar for price
# ------------------------
fig, ax = plt.subplots(figsize=(6, 0.5))
fig.subplots_adjust(bottom=0.5)
cb1 = ColorbarBase(
    ax, cmap=cmap, norm=norm, orientation='horizontal'
)
cb1.set_label('Average Price (€)')
st.pyplot(fig)

# ------------------------
# Prediction
# ------------------------
st.header("💡 Price predictor")

# User inputs
bedrooms = st.number_input("Number of bedrooms", min_value=0, max_value=10, value=1)
neighbourhood = st.selectbox("Neighbourhood", df["neighbourhood_cleansed"].unique())

if st.button("Predict price"):
    # Train the model on the current dataset (or optionally load a pre-trained model)
    model = train_and_save_model(df)  # returns a fitted pipeline

    # Prepare input and predict
    prediction = predict_price(model, {"bedrooms": bedrooms, "neighbourhood_cleansed": neighbourhood})

    st.success(f"💡 Predicted price: €{prediction:.2f}")

