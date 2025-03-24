import os
import streamlit as st
from requests import get
import pandas as pd
#API Key: Stored as environment variable
nasa_key = os.environ.get("NASA_OPEN_API_KEY")

st.set_page_config(page_title="Space Weather Notifications", page_icon="📷")

st.markdown("# Space Weather Notifications")
st.sidebar.header("Space Weather Notifications")
st.write(
    """This page shows the notifications of space weather events from NASA. The amount of each event 
        within the span of the past month can be seen in the chart below."""
)
#TODO: Add add chart with the data
# event_occurences = pd.DataFrame(
#     {
#      "Event Type": ["CME", "GST", "IPS", "FLR",
#      "SEP", "MPC", "RBE", "HSS"]
#      "Event Count": {}
#     }
# )
# st.bar_chart(event_occurences, x="month", y="event count")
# Create a sample dataframe
event_name_table = pd.DataFrame(
    {
     "Abbreviation": ["CME", "GST", "IPS", "FLR",
                      "SEP", "MPC", "RBE", "HSS"],
     "Event Name": ["Coronal Mass Ejection", "Geomagnetic Storm", "Interplanetary Shock",
                    "Solar Flare", "Solar Energetic Particle", "Magnetopause Crossing",
                    "Radiation Belt Enhancement", "High Speed Stream"]
     }
)

# Display the dataframe without the index column
st.dataframe(event_name_table, hide_index=True)
# Add stats for each event type
#https://docs.streamlit.io/develop/api-reference/layout/st.expander
notifications = get(f"https://api.nasa.gov/DONKI/notifications?api_key={nasa_key}").json()
for notification in notifications:
    st.subheader(f"{notification["messageIssueTime"]} : {notification["messageType"]}", divider="gray")
    with st.expander("Notification Details"):
        st.write(notification["messageBody"])