## This service is for any functions interacting with the server
## All of these functions print and return, the print is for CLI
import json

import requests
from config import server_address

def server_get_all_nodes():
    print("Getting nodes...")
    url = server_address + "/all-connections"
    try:
        response = requests.get(url)
        data = response.json()
        res_json = {'server_response': data}
        print(json.dumps(res_json, indent=2))
        return res_json
    except requests.exceptions.RequestException as e:
        res_json = {'error': str(e)}, 500
        print(json.dumps(res_json, indent=2))
        return res_json


def server_register_self():
    print("Connecting to server...")
    url = server_address + "/connect"
    try:        
        response = requests.post(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        res_json = {'server_response': data}
        print(json.dumps(res_json, indent=2))
        return res_json
    except requests.exceptions.RequestException as e:        
        res_json = {'error': str(e)}, 500
        print(json.dumps(res_json, indent=2))
        return res_json


def server_request_challenge_broadcast():
    print("Requesting a challenge broadcast for all nodes from the server...")
    url = server_address + "/broadcast-challenge"
    try:
        response = requests.post(url)         
        response.raise_for_status()  
        data = response.json()
        res_json = {'server_response': data}        
        print(json.dumps(res_json, indent=2))
        return res_json
    except requests.exceptions.RequestException as e:
        res_json = {'error': str(e)}, 500
        print(json.dumps(res_json, indent=2))
        return res_json
    
    
def server_delete_nodes():
    print("Deleting all nodes...")
    url = server_address + '/delete-all-nodes'
    try:
        response = requests.delete(url)         
        response.raise_for_status()  
        data = response.json()
        res_json = {'server_response': data}        
        print(json.dumps(res_json, indent=2))
        return res_json
    except requests.exceptions.RequestException as e:
        res_json = {'error': str(e)}, 500
        print(json.dumps(res_json, indent=2))
        return res_json