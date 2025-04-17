import streamlit as st

st.set_page_config(
    page_title="Space Information UI",
    page_icon="⭐",
)

st.write("# ⭐Space Information UI⭐")

st.markdown(
    """
    Curious as to what's going on in our solar system? How about looking at other cool space things?
    This site lets you do so by using a variety of NASA Open APIs to show you what's going on in space.
    
    Their APIs are free to use and there are a ton to check out. You can sign up for your own API access here:
    https://api.nasa.gov/
    """
)
st.image("src/meme.jpg")