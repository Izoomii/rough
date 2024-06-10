

connections = []

def add_new_connection(client_ip, connectionsList):
    if client_ip not in connectionsList:
        connectionsList.append(client_ip)
        return True
    else:
        return False
    
def get_connections():
    return connections


def view_connections():
    print(f"Node count: {connections.__len__()}")
    print(connections)
    return {
        'count': connections.__len__(),
        'connections': connections
    }

def delete_connections():
    connections = []
    print("Removed all connections.")
    return {
        'connections': connections
    }