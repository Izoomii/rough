from flask import Flask, request, jsonify
import requests
import base64
from config import client_port
# from server_service import server_register_self
from challenge_service import handle_challenge

app = Flask(__name__)




## Client listens on this route for challenge broadcasts
@app.route("/challenge", methods=["POST"])
def get_challenge():    
    data = request.get_json()
    encoded_payload = data['data']
    payload = base64.b64decode(encoded_payload.encode('utf-8')) ## this is the actual bytes of the challenge
    ## handles challenge
    response = handle_challenge(payload_in_bytes=payload)    
    # res_json = jsonify(response)  # Ensure response is in JSON format
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=client_port, debug=True)
