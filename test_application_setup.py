from src.data import *
import streamlit as st
#hi 

nasa_key = st.secrets["nasa_key"]

def test_get_aopd():
    image_of_the_day = get(f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}").json()
    image_url = image_of_the_day.get("url", None)
    print(image_url)
    
def test_get_donki():
    notifications = get(f"https://api.nasa.gov/DONKI/notifications?api_key={nasa_key}").json()
    print(notifications)
    assert notifications is not None
