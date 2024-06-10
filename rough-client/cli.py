import argparse
from server_service import server_get_all_nodes, server_register_self, server_request_challenge_broadcast, server_delete_nodes
import sys


def cli_register_self(args):
    return server_register_self()
def cli_get_all_nodes(args):
    return server_get_all_nodes()
def cli_request_challenge_broadcast(args):
    return server_request_challenge_broadcast()
def cli_delete_all_nodes(args):
    return server_delete_nodes()


def create_parser():
    parser = argparse.ArgumentParser(description="CLI tool for managing the Flask server")

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # register command
    register_parser = subparsers.add_parser(name='register', help='Register your IP address in the server, so that future challenge broadcasts are sent to you.')
    register_parser.set_defaults(func=cli_register_self)

    # get nodes command
    get_nodes_parser = subparsers.add_parser(name='get-nodes', help='Get a list of all nodes registered on the server.')
    get_nodes_parser.set_defaults(func=cli_get_all_nodes)

    # request broadcast command
    request_broadcast_parser = subparsers.add_parser(name='request-broadcast', help='Request a new challenge broadcast from the server, this broadcast is sent to all registered nodes.')
    request_broadcast_parser.set_defaults(func=cli_request_challenge_broadcast)

    # delete all nodes
    delete_nodes_parser = subparsers.add_parser(name='delete-nodes', help='Tell the server to remove all saved IP addresses.')
    delete_nodes_parser.set_defaults(func=cli_delete_all_nodes)

    return parser


def main(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args=args)

    # Call the function associated with the selected command
    if hasattr(parsed_args, 'func'):
        parsed_args.func(parsed_args)
    else:
        parser.print_help()
    


if __name__ == '__main__':
    # start_server()
    main(sys.argv[1:])