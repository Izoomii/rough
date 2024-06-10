import os
import base64
# Generates the 1KB challenge, and returns it encoded in Base64 
def generate_encoded_challenge():
    payload = os.urandom(1024)  # Generate a random 1KB payload
    encoded_payload = base64.b64encode(payload).decode('utf-8')
    return encoded_payload
