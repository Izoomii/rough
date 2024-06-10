from multiprocessing import Process
from flask import Flask, request, jsonify
import requests
import concurrent.futures
from config import client_port, server_port
from connections_repo import add_new_connection, get_connections, delete_connections
from challenge_service import generate_encoded_challenge
import time


app = Flask(__name__)




def start_server(host='0.0.0.0', port=server_port):
    print("Starting server...")    
    app.run(host=host, port=port, debug=True)


# Hello world route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# The client hits this route to connect
# Connecting here just means the server registers the client IP 
@app.route('/connect', methods=['POST'])
def get_ip():
    client_ip = request.remote_addr
    connections = get_connections()
    add_new_connection(client_ip, connections)
    return jsonify({'ip': client_ip})

@app.route("/all-connections", methods=['GET'])
def get_all_connections():
    connections = get_connections()
    return jsonify({
        'connections': connections
    })


@app.route('/broadcast-challenge', methods=['POST'])
def challenge_all_nodes():
    connections = get_connections()
    encoded_challenge = generate_encoded_challenge()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda ip: send_request(ip, encoded_challenge), connections))        
    return jsonify(results)

@app.route("/delete-all-nodes", methods=["DELETE"])
def delete_all_nodes():
    response = delete_connections()
    return jsonify(response)


def send_request(connection_ip, payload):
    url = f'http://{connection_ip}:{client_port}/challenge'    
    start_time = time.perf_counter()
    try:
        response = requests.post(url, json={'data': payload})
        end_time = time.perf_counter()
        return {'client': connection_ip, 'time': end_time - start_time, 'response': response.json()}
    except requests.exceptions.RequestException as e:
        end_time = time.perf_counter()
        return {'client': connection_ip, 'time': end_time - start_time, 'error': str(e)}





if __name__ == '__main__':
    start_server()
    