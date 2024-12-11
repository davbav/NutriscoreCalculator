import streamlit as st
import pandas as pd #this is for graphs
import altair as alt #this is for graphs
from algorithms.nutriscore_2017 import nutriscore_2017_Master
from algorithms.nutriscore_2023 import nutriscore_2023_Master
from data import (
    energy_points,
    saturated_fat_points,
    sugar_points,
    salt_points,
    fiber_points,
    protein_points,
    fruits_veg_points,
    energy_points_2023,
    saturated_fat_points_2023,
    sugar_points_2023,
    salt_points_2023,
    fiber_points_2023,
    protein_points_2023,
    fruits_veg_points_2023,
)

# Page Title
st.title("Interactive Nutri-Score Analysis")
st.markdown("Adjust the sliders to see how points and total Nutri-Score change dynamically:")

# Sidebar for Algorithm Selection
algorithm = st.sidebar.radio("Select Algorithm Version", ["2017 (Original)", "2023 (Updated)"])

# Default Input Values
energy = st.sidebar.number_input("Energy (kJ)", min_value=0.0, step=20, value=530.0)
saturated_fat = st.sidebar.number_input("Saturated Fat (g)", min_value=0.0, step=0.2, value=0.6)
sugars = st.sidebar.number_input("Sugars (g)", min_value=0.0, step=2, value=2.8)
salt = st.sidebar.number_input("Salt (g)", min_value=0.0, step=0.1, value=0.65)
fiber = st.sidebar.number_input("Fiber (g)", min_value=0.0, step=0.4, value=1.1)
protein = st.sidebar.number_input("Protein (g)", min_value=0.0, step=0.4, value=4.8)
fruits_veg = st.sidebar.number_input("Fruits, Vegetables, Legumes (%)", min_value=0.0, max_value=100.0, step=5.0, value=39)

# MArking scheme Functions
def score_to_letter_and_color2017(score):
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

# Calculate Points and Nutri-Score - the same calculation that is done in algorithms for the calculator on the first page. Just done in a different way referencing the data.py rather than directly calculating the points. gets the same result tho.
if algorithm == "2017 (Original)":
    sodium = salt / 2.5 * 1000
    points = [
        energy_points(energy),
        saturated_fat_points(saturated_fat),
        sugar_points(sugars),
        salt_points(sodium),
        -fiber_points(fiber),
        -protein_points(protein),
        -fruits_veg_points(fruits_veg),
    ]
    score = nutriscore_2017_Master(energy, saturated_fat, sugars, sodium, fiber, protein, fruits_veg) 
    letter, color = score_to_letter_and_color2017(score)

elif algorithm == "2023 (Updated)":
    points = [
        energy_points_2023(energy),
        saturated_fat_points_2023(saturated_fat),
        sugar_points_2023(sugars),
        salt_points_2023(salt),
        -fiber_points_2023(fiber),
        -protein_points_2023(protein),
        -fruits_veg_points_2023(fruits_veg),
    ]
    score = nutriscore_2023_Master(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg)
    letter, color = score_to_letter_and_color2023(score)

# Prepare Bar Chart Data
input_labels = ["Energy", "Saturated Fat", "Sugars", "Salt", "Fiber", "Protein", "Fruits/Veg"]
bar_data = pd.DataFrame({
    "Input": input_labels,
    "Points": points,
})
bar_data["Color"] = [ #diffferenciate the positive and negative points by color
    "red" if label in ["Energy", "Saturated Fat", "Sugars", "Salt"] else "green"
    for label in bar_data["Input"]
]

# Create Altair Bar Chart - the one imported at the begining 
bar_chart = alt.Chart(bar_data).mark_bar().encode(
    x=alt.X("Input:O", sort=None, title="Input macros"),
    y=alt.Y("Points:Q", title="Points"),
    color=alt.Color("Color:N", scale=None, legend=None),
    tooltip=["Input", "Points"]
).properties(
    width=600,
    height=400,
    title="Points Breakdown by Input Type"
)

# Display the Interactive Bar Chart and Total Nutri-Score
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Points Breakdown")
    col1.altair_chart(bar_chart)

with col2:
    st.markdown(f"<h3 style='color: {color};'>Updated Nutri-Score: {letter}</h3>", unsafe_allow_html=True)
    st.text(f"Total Points: {score}")

# Line Plot for Sensitivity Analysis
st.subheader("Sensitivity Analysis: Effect of a Single Input on Total Nutri-Score")

# Select variable for sensitivity analysis
variable = st.selectbox(
    "Select Variable to Analyze",
    ["Energy", "Saturated Fat", "Sugars", "Salt", "Fiber", "Protein", "Fruits/Veg"]
)

# Define a range for the selected variable so the graph won't look crazy
ranges = {
    "Energy": range(0, 3001, 100),
    "Saturated Fat": [round(x * 0.1, 1) for x in range(0, 51)],
    "Sugars": [round(x * 0.1, 1) for x in range(0, 101)],
    "Salt": [round(x * 0.1, 1) for x in range(0, 51)],
    "Fiber": [round(x * 0.1, 1) for x in range(0, 51)],
    "Protein": [round(x * 0.1, 1) for x in range(0, 51)],
    "Fruits/Veg": range(0, 101, 5),
}

selected_range = ranges[variable]
scores = []

# Iterate over the range and calculate scores
for value in selected_range:
    # Update only the selected variable, keep others constant
    if variable == "Energy":
        energy = value
    elif variable == "Saturated Fat":
        saturated_fat = value
    elif variable == "Sugars":
        sugars = value
    elif variable == "Salt":
        salt = value
    elif variable == "Fiber":
        fiber = value
    elif variable == "Protein":
        protein = value
    elif variable == "Fruits/Veg":
        fruits_veg = value

    if algorithm == "2017 (Original)":
        sodium = salt / 2.5 * 1000
        score = nutriscore_2017_Master(energy, saturated_fat, sugars, sodium, fiber, protein, fruits_veg)
    elif algorithm == "2023 (Updated)":
        score = nutriscore_2023_Master(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg)

    scores.append(score)

# Prepare line chart data
line_data = pd.DataFrame({
    variable: selected_range,
    "Nutri-Score": scores,
})

# Create Altair Line Chart
line_chart = alt.Chart(line_data).mark_line().encode(
    x=alt.X(f"{variable}:Q", title=variable),
    y=alt.Y("Nutri-Score:Q", title="Total Nutri-Score for different inputed values for this config."),
    tooltip=[variable, "Nutri-Score"]
).properties(
    width=700,
    height=400,
    title=f"Sensitivity Analysis: Effect of {variable}"
)

# Display the line chart
st.altair_chart(line_chart)
