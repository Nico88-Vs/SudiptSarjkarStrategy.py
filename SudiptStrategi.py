import streamlit as st
import ApiConnector as cnn
from urllib.parse import urlparse, parse_qs

st.title("start")

# Ottieni i parametri dalla query string dell'URL
# query_params = st.experimental_get_query_params()
# st.write(query_params)
try:
    debug = st.query_params.keys()
    query_params = st.query_params.get("auth_code")
    
    st.write(query_params)
    
    st.write( debug)
     
    if "auth_code" in query_params:
        auth_code = query_params["access_token"][0]  # Estrai il primo valore di auth_code
        refreshcode = query_params["refresh_token"][0]
        st.write(f"Authorization Code: {auth_code}")
        
        if "AUTH" not in st.session_state:
            st.session_state.AUTH = query_params["access_token"][0]
            
        if "REFRESH" not in st.session_state:
            st.session_state.REFRESH = query_params["refresh_token"][0]
        
        # Qui puoi chiamare la funzione per ottenere il token
        # ...logica per generare il token...
    else:
        st.write("Please authorize the app to continue.")
    
except :
    pass

if "AUTH" in st.session_state:
    st.write(st.session_state.AUTH)
else:
   st.write("nooooo") 
            
if "REFRESH" in st.session_state:
    st.write(st.session_state.REFRESH)

connector = cnn.Connector()

if st.button('connect'):
    
    connector.connect()
