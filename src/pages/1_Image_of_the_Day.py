import streamlit as st
from requests import get

def get_apod(api_key: str, my_date: str) -> None:
    """
    :Purpose: Queries the NASA AOPD API to get the astronomy picture of the day.
    :param api_key: String containing the NASA API key.
    :param my_date: Date for the image the user would like to view.
    :return: None
    """
    #Query for the image corresponding to the date selected
    try:
        # Try to retrieve the image URL and title from the response
        image_of_the_day = get(f"https://api.nasa.gov/planetary/apod?date={my_date}&api_key={api_key}").json()
        image_url = image_of_the_day.get("url", None)

        if image_url:
            # If the URL is found, display the image
            st.header(image_of_the_day.get("title", "No Title"))
            st.image(
                image_url,
                caption=f"{image_of_the_day.get('explanation', 'No explanation')} \n\nCopyright: "
                        f"{image_of_the_day.get('copyright', 'No copyright information')}"
            )
        else:
            # If the URL is None or not found, raise an error
            raise ValueError("Image URL not found in the API response. Try a different date or try again later.")

    except ValueError as e:
        # Handle the case where the image URL is not found
        st.error(f"Error: {str(e)}")

    except Exception as e:
        # General error handling for any other issues (e.g., network issues, invalid response)
        st.error(f"An unexpected error occurred: {str(e)}")
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


