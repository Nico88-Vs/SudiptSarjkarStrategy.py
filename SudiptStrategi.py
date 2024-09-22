import streamlit as st
import ApiConnector as cnn

st.title("start")
if st.button('connect'):
    cnn.Connector.connector.Connect()
