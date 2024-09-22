import streamlit as st
from ApiConnect import Connector as connector

st.title("start")
if st.button('connect'):
    connector.Connect()
