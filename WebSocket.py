from fyers_apiv3.FyersWebsocket import order_ws


class WebSocket():
    """description of class"""
    
    def __init__(self, token) :
        # Replace the sample access token with your actual access token obtained from Fyers
        self.access_token = token
        self.fyers = order_ws.FyersOrderSocket(
            access_token=self.access_token,  # Your access token for authenticating with the Fyers API.
            write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
            log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
            on_connect=onopen,          # Callback function to be executed upon successful WebSocket connection.
            on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
            on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
            on_general=onGeneral,       # Callback function to handle general events from the WebSocket.
            on_orders=onOrder,          # Callback function to handle order-related events from the WebSocket.
            on_positions=onPosition,    # Callback function to handle position-related events from the WebSocket.
            on_trades=onTrade           # Callback function to handle trade-related events from the WebSocket.
        )
       
        

        def onTrade(message):
            """
            Callback function to handle incoming messages from the FyersDataSocket WebSocket.
        
            Parameters:
                message (dict): The received message from the WebSocket.
        
            """
            print("Trade Response:", message)
        
        def onOrder(message):
            """
            Callback function to handle incoming messages from the FyersDataSocket WebSocket.
        
            Parameters:
                message (dict): The received message from the WebSocket.
        
            """
            print("Order Response:", message)
        
        def onPosition(message):
            """
            Callback function to handle incoming messages from the FyersDataSocket WebSocket.
        
            Parameters:
                message (dict): The received message from the WebSocket.
        
            """
            print("Position Response:", message)
        
        def onGeneral(message):
            """
            Callback function to handle incoming messages from the FyersDataSocket WebSocket.
        
            Parameters:
                message (dict): The received message from the WebSocket.
        
            """
            print("General Response:", message)
        def onerror(message):
            """
            Callback function to handle WebSocket errors.
        
            Parameters:
                message (dict): The error message received from the WebSocket.
        
        
            """
            print("Error:", message)
        
        
        def onclose(message):
            """
            Callback function to handle WebSocket connection close events.
            """
            print("Connection closed:", message)
        
        
        def onopen():
            """
            Callback function to subscribe to data type and symbols upon WebSocket connection.
        
            """
            # Specify the data type and symbols you want to subscribe to
            # data_type = "OnOrders"
            # data_type = "OnTrades"
            # data_type = "OnPositions"
            # data_type = "OnGeneral"
            data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"
        
            self.fyers.subscribe(data_type=data_type)
        
            # Keep the socket running to receive real-time data
            self.fyers.keep_running()
        
        
        def Connect():
            # Establish a connection to the Fyers WebSocket
            self.fyers.connect()

# ------------------------------------------------------------------------------------------------------------------------------------------
# Sample Success Response 
# ------------------------------------------------------------------------------------------------------------------------------------------
          
#   {
#     "s":"ok",
#     "orders":{
#         "clientId":"XV20986",
#         "id":"23080400089344",
#         "exchOrdId":"1100000009596016",
#         "qty":1,
#         "filledQty":1,
#         "limitPrice":7.95,
#         "type":2,
#         "fyToken":"101000000014366",
#         "exchange":10,
#         "segment":10,
#         "symbol":"NSE:IDEA-EQ",
#         "instrument":0,
#         "offlineOrder":false,
#         "orderDateTime":"04-Aug-2023 10:12:58",
#         "orderValidity":"DAY",
#         "productType":"INTRADAY",
#         "side":-1,
#         "status":90,
#         "source":"W",
#         "ex_sym":"IDEA",
#         "description":"VODAFONE IDEA LIMITED",
#         "orderNumStatus":"23080400089344:2"
#     }
#   }


