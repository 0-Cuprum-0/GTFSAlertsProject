import wifi_data

import network
import requests
import time

ssid = wifi_data.ssid
password = wifi_data.password
# Connect to network
def connect_wifi(ssid, password):
    # Connect to your network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    
    # Wait for connection
    timeout = 10
    while not station.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1
    
    if station.isconnected():
        print('Connected to WiFi')
        print(station.ifconfig())
        return True
    else:
        print('Connection failed. Timeout reached')
        return False

if connect_wifi(ssid, password):    
    # Make GET request
    try:
        response = requests.get("http://10.205.90.140:8000/data")
        # Get response code
        response_code = response.status_code
        # Get response content
        response_content = response.content
        print(response_content)
        # Print results
        print('Response code: ', response_code)
        print('Response content:', response_content)
    except Exception as e:
        print('An error occurred during the request:', str(e))
else:
    print('Failed to connect to WiFi')


