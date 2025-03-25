import os
import streamlit as st
from requests import get
import pandas as pd
#API Key: Stored as environment variable
nasa_key = os.environ.get("NASA_OPEN_API_KEY")
notifications = get(f"https://api.nasa.gov/DONKI/notifications?api_key={nasa_key}").json()

st.set_page_config(page_title="Space Weather Notifications", page_icon="📷")

st.markdown("# Space Weather Notifications")
st.sidebar.header("Space Weather Notifications")
st.write(
    """This page shows the notifications of space weather events from NASA. The amount of each event 
        within the span of the past month can be seen in the chart below."""
)
#Bar Chart of Number of events per month
event_types = ["CME", "GST", "IPS", "FLR", "SEP", "MPC", "RBE", "HSS"]
event_counts = {event: 0 for event in event_types}

# Count the occurrences of each event from your JSON data
# This is a placeholder - you'll need to adapt this to your actual JSON structure
for event in notifications:  # Assuming 'data' is a list of events
    event_type = event.get('messageType')  # Adjust according to your JSON structure
    if event_type in event_types:
        event_counts[event_type] += 1

# Create a DataFrame from the counts
df = pd.DataFrame({
    'Event': list(event_counts.keys()),
    'Count': list(event_counts.values())
})

# Display the bar chart
st.bar_chart(df, x='Event', y='Count')
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
for notification in notifications:
    st.subheader(f"{notification["messageIssueTime"]} : {notification["messageType"]}", divider="gray")
    with st.expander("Notification Details"):
        st.write(notification["messageBody"])