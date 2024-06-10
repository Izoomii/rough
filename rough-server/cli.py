import argparse
from connections_repo import view_connections
import sys


################################################################
### The CLI for the server is not currently in use
################################################################


def create_parser():
    parser = argparse.ArgumentParser(description="CLI tool for managing the Flask server")
    parser.add_argument('command', help="Command to run", choices=[ 'help', 'view-nodes', 'challenge-nodes'])
    # parser.add_argument('--host', default='127.0.0.1', help="Host to run the server on")
    # parser.add_argument('--port', type=int, default=5000, help="Port to run the server on")
    return parser


def main(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args=args)

    # this is the command provided by the user
    cmd = parsed_args.command

    if cmd == 'help':
        parser.print_help()
    if cmd == 'view-nodes':
        view_connections()


if __name__ == '__main__':
    # start_server()
    main(sys.argv[1:])