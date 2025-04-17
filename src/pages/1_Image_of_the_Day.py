import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from src.data import get_apod

st.set_page_config(page_title="Astronomy Picture of the Day", page_icon="📷")

st.markdown("# 📷Astronomy Picture of the Day (AOPD)📷")
st.sidebar.header("Astronomy Picture of the Day")
st.write(
    """Curious as to what the Astronomy Picture of the Day is? Take a look at today's or 
       select a date of your choosing to view the image of that specific date. Read the caption
       for the explanation of the picture!"""
)

st.divider()

#API Key: Stored as environment variable
nasa_key = st.secrets["nasa_key"]
#Parameter for user to select the date of the image they would like to view
#defaults to today's date.
my_date = st.date_input("Date")
get_apod(nasa_key, my_date)


