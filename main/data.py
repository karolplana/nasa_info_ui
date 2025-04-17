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

def get_notifications(api_key: str) -> dict:
    """
    :Purpose: Queries the NASA DONKI API to get the notification information.
    :param api_key: String containing the NASA API key.
    :return: Dictionary containing the json notification data.
    """
    try:
        notifications = get(f"https://api.nasa.gov/DONKI/notifications?api_key={api_key}").json()
        return notifications
    except ValueError as e:
        st.error(f"Error: {str(e)}")
