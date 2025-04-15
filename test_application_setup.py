from src.data import *
nasa_key = st.secrets["nasa_key"]

def test_get_aopd():
    image_of_the_day = get(f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}").json()
    image_url = image_of_the_day.get("url", None)
    assert image_url is not None
def test_get_donki():
    notifications = get(f"https://api.nasa.gov/DONKI/notifications?api_key={nasa_key}").json()
    assert notifications is not None