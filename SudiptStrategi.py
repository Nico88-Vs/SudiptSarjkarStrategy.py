import streamlit as st
from ApiConnector import Connector as connector

st.title("start")
if st.button('connect'):
    connector.Connect()
