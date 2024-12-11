import streamlit as st
import pandas as pd

from algorithms.nutriscore_2017 import nutriscore_2017_Master
from algorithms.nutriscore_2023 import nutriscore_2023_Master
from data import (
    energy_points,
    fiber_points,
    fruits_veg_points,
    protein_points,
    salt_points,
    saturated_fat_points,
    sugar_points,
    energy_points_2023,
    saturated_fat_points_2023,
    sugar_points_2023,
    salt_points_2023,
    fiber_points_2023,
    protein_points_2023,
    fruits_veg_points_2023,
)

# Page Title
st.title("Nutri-Score Calculator")

# Sidebar for Algorithm Selection
algorithm = st.sidebar.radio("Select Algorithm Version", ["2017 (Original)", "2023 (Updated)"])

# macros Input Section
st.header("Enter Nutritional Information (per 100g)")
energy = st.number_input("Energy (kJ)", min_value=0.0, step=20.0)
saturated_fat = st.number_input("Saturated Fat (g)", min_value=0.0, step=0.2)
st.markdown(
    '<p style="color:gray;font-size:small;">Important: Not total fats, SATURATED!.</p>', 
    unsafe_allow_html=True
)
sugars = st.number_input("Sugars (g)", min_value=0.0, step=2.0)
st.markdown(
    '<p style="color:gray;font-size:small;">Important: Only pure sugars, not total carbs.</p>', 
    unsafe_allow_html=True
)
salt = st.number_input("Salt (g)", min_value=0.0, step=0.1)
def convert_salt_to_sodium(salt):
    """Convert salt (g) to sodium (mg)."""
    return int(salt / 2.5 * 1000)

sodium = convert_salt_to_sodium(salt)

if algorithm == "2017 (Original)":
    st.markdown(
        f'<p style="color:gray;font-size:small;">This value will be automatically converted to sodium (mg). Sodium = {sodium}.</p>', 

        unsafe_allow_html=True
    )
fiber = st.number_input("Fiber (g)", min_value=0.0, step=0.4)
protein = st.number_input("Protein (g)", min_value=0.0, step=0.4)
fruits_veg = st.number_input("Fruits, Vegetables, Legumes (%)", min_value=0, max_value=100)

# marking scheme Functions


def score_to_letter_and_color2017(score):
    """Convert numeric Nutri-Score to letter and color."""
    if score <= -1:
        return "A", "green"
    elif 0 <= score <= 2:
        return "B", "lightgreen"
    elif 3 <= score <= 10:
        return "C", "yellow"
    elif 11 <= score <= 18:
        return "D", "orange"
    else:
        return "E", "red"

def score_to_letter_and_color2023(score):
    """Convert numeric Nutri-Score to letter and color."""
    if score <= 0:
        return "A", "green"
    elif 1 <= score <= 2:
        return "B", "lightgreen"
    elif 3 <= score <= 10:
        return "C", "yellow"
    elif 11 <= score <= 18:
        return "D", "orange"
    else:
        return "E", "red"

# show Nutri-Score
if st.button("Calculate Nutri-Score"):
    if algorithm == "2017 (Original)":
        score = nutriscore_2017_Master(energy, saturated_fat, sugars, sodium, fiber, protein, fruits_veg)
        st.success(f"2017 Nutri-Score: {score}")
        letter, color = score_to_letter_and_color2017(score)

        

    elif algorithm == "2023 (Updated)":
        score = nutriscore_2023_Master(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg)
        st.success(f"2023 Nutri-Score: {score}")
        letter, color = score_to_letter_and_color2023(score)

        
        

    # Display the Nutri-Score Letter
    st.markdown(f"<h2 style='color: {color};'>Nutri-Score Letter: {letter}</h2>", unsafe_allow_html=True)

# Append Screenshot
st.markdown("---")  # Add a separator line
st.subheader("Points Attribution")
try:
    st.image("screenshot1.png", caption="Found on nutriscore website", use_container_width=True)
except FileNotFoundError:
    st.error("The file 'screenshot1.png' was not found. Please verify the file path.")
