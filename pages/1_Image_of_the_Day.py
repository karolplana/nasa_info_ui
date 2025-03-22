import os
import streamlit as st
from requests import get

#API Key: Stored as environment variable
nasa_key = os.environ.get("NASA_OPEN_API_KEY")

st.set_page_config(page_title="Astronomy Picture of the Day", page_icon="📷")

st.markdown("# Astronomy Picture of the Day")
st.sidebar.header("Astronomy Picture of the Day")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
#Parameter for user to select the date of the image they would like to view
#defaults to today's date.
my_date = st.date_input("Date")
#Query for the image corresponding to the date selected
image_of_the_day = get(f"https://api.nasa.gov/planetary/apod?date={my_date}&api_key={nasa_key}").json()
st.image(image_of_the_day.get("hdurl"))

