from fyers_apiv3 import fyersModel
import webbrowser

class Connector():
    
    def __init__(self):
        # Replace these values with your actual API credentials
        self.client_id = "46OAC8DRLG-100"
        self.secret_key = "94I7H2K4SZ"
        self.redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
        self.response_type = "code"  
        self.state = "sample_state"
    
    def connect(self):
        # Create a session model with the provided credentials
        session = fyersModel.SessionModel(
            client_id=self.client_id,
            secret_key=self.secret_key,
            redirect_uri=self.redirect_uri,
            response_type=self.response_type
        )
        
        # Generate the auth code using the session model
        response = session.generate_authcode()
        
        webbrowser.open(response, new=1)
        
        






