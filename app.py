import streamlit as st
import math

st.title("Circle Area Calculator")

# Input for radius
a = st.number_input("Enter the radius of the circle:", min_value=0.0, format="%.2f")

# Calculate and display area if a valid radius is provided
if a > 0:
    area = math.pi * a**2
    st.write(f"Area of the circle is: {area:.2f}")
