import os
import streamlit as st
from requests import get
#API Key: Stored as environment variable
nasa_key = os.environ.get("NASA_OPEN_API_KEY")

st.set_page_config(page_title="Space Weather Notifications", page_icon="📷")

st.markdown("# Space Weather Notifications")
st.sidebar.header("Space Weather Notifications")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

#https://docs.streamlit.io/develop/api-reference/layout/st.expander
notifications = get(f"https://api.nasa.gov/DONKI/notifications?api_key={nasa_key}").json()
for notification in notifications:
    st.subheader(f"{notification["messageIssueTime"]} : {notification["messageType"]}", divider="gray")
    with st.expander("Notification Details"):
        st.write(notification["messageBody"])