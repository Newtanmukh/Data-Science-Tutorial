import streamlit as st
import langchain_helper


st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Arabic", "Mexican", "Bengali"))

if cuisine:
    response = langchain_helper.generate_restaurant_cuisine_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_response'].split(",")

    st.write("### MENU ITEMS ###")
    for item in menu_items:
        st.write("-", item)

