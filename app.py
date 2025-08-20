import streamlit as st
from func import get_weather

st.title("Weather App")
city = st.text_input("What city would you like to know the weather for?")

st.image("https://media.istockphoto.com/id/1257525705/photo/the-changes-of-weather-a-natural-phenomenon-of-the-differences-of-four-seasons.jpg?s=612x612&w=0&k=20&c=pd2FEbZITpqphzEJ51FBQFexzniU0AZNJctpksrehYQ=", use_column_width=True)

if city:
    temp, humidity, description = get_weather(city)
    st.write("Welcome to", city)
    st.write("Temperature is", temp)
    st.write("Humidity is", humidity)
    st.write("The skies show", description)