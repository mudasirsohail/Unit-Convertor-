import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[from_unit] / conversion_dict[to_unit])
    return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

st.set_page_config(page_title="⚡ Advanced Unit Converter", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
        .css-18e3th9 {
            background-color: #1e1e1e !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("⚙️ Features")
st.sidebar.write("📏 Length Conversion")
st.sidebar.write("⚖️ Weight Conversion")
st.sidebar.write("🌡️ Temperature Conversion")
st.sidebar.write("💰 Currency Conversion")
st.sidebar.write("💾 Data Storage Conversion")
st.sidebar.write("⏲️ Time Conversion")  # Added Time Conversion option

category = st.sidebar.radio("Select a category:", ["Length", "Weight", "Temperature", "Currency", "Data Storage", "Time"])

if category == "Length":
    st.subheader("📏 Length Converter")
    length_units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001, "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254}
    from_unit = st.selectbox("From:", list(length_units.keys()))
    to_unit = st.selectbox("To:", list(length_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert 🔄"):
        result = convert_units(value, from_unit, to_unit, length_units)
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    st.subheader("⚖️ Weight Converter")
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    from_unit = st.selectbox("From:", list(weight_units.keys()))
    to_unit = st.selectbox("To:", list(weight_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert 🔄"):
        result = convert_units(value, from_unit, to_unit, weight_units)
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    temp_scales = {"Celsius", "Fahrenheit", "Kelvin"}
    from_unit = st.selectbox("From:", temp_scales)
    to_unit = st.selectbox("To:", temp_scales)
    value = st.number_input("Enter value:", format="%.2f")
    
    if st.button("Convert 🔄"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Currency":
    st.subheader("💰 Currency Converter")
    currency_rates = {"USD": 1, "EUR": 0.85, "GBP": 0.75, "INR": 74.5, "PKR": 280}
    to_unit = st.selectbox("To:", list(currency_rates.keys()))
    from_unit = st.selectbox("From:", list(currency_rates.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert 🔄"):
        result = convert_units(value, from_unit, to_unit, currency_rates)
        st.success(f" {to_unit} {value} = {result:.2f} {from_unit}   ")

elif category == "Data Storage":
    st.subheader("💾 Data Storage Converter")
    data_units = {"Bytes": 1, "Kilobytes": 1024, "Megabytes": 1024**2, "Gigabytes": 1024**3, "Terabytes": 1024**4}
    from_unit = st.selectbox("From:", list(data_units.keys()))
    to_unit = st.selectbox("To:", list(data_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert 🔄"):
        result = convert_units(value, from_unit, to_unit, data_units)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Time":  # New Time conversion logic
    st.subheader("⏲️ Time Converter")
    time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800, "Months": 2628000, "Years": 31536000}
    from_unit = st.selectbox("From:", list(time_units.keys()))
    to_unit = st.selectbox("To:", list(time_units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert 🔄"):
        result = convert_units(value, from_unit, to_unit, time_units)
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
