import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎")

@st.cache_resource
def load_model():
    with open("diamond_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("💎 Diamond Price Predictor")
st.write("Diamond ki specifications daalo aur uski price (USD) pata karo.")

col1, col2 = st.columns(2)
with col1:
    carat = st.number_input("Carat", 0.2, 5.0, 0.7, step=0.01)
    cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])
with col2:
    depth = st.number_input("Depth %", 40.0, 80.0, 61.8, step=0.1)
    table = st.number_input("Table", 40.0, 100.0, 57.0, step=0.1)
    x = st.number_input("Length x (mm)", 0.0, 12.0, 5.7, step=0.01)
    y = st.number_input("Width y (mm)", 0.0, 60.0, 5.7, step=0.01)
    z = st.number_input("Depth z (mm)", 0.0, 35.0, 3.5, step=0.01)

if st.button("Predict Price"):
    row = pd.DataFrame([{
        "carat": carat, "cut": cut, "color": color, "clarity": clarity,
        "depth": depth, "table": table, "x": x, "y": y, "z": z,
    }])
    price = model.predict(row)[0]
    st.success(f"Predicted Price: ${price:,.2f}")