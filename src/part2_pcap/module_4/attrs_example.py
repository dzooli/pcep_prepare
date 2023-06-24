"""
Demo for JSON input validation using the attrs library.
"""
import json
from pprint import pprint

from model import Server, Network, NetworkDecoder

VALID_SERVER = """
    { 
      "server_name": "super-server",
      "type": "pf"
    }  
    """
INVALID_SERVER = """
    { 
      "server_name": "inv-server",
      "type": "xyz"
    }  
    """
VALID_NETWORK = """
    {
        "network_id": 100,
        "nodes": [
            {
                "server_name": "server1"
            },
            {
                "server_name": "server2",
                "type": "pf"
            }
        ]
    }
    """
INVALID_NETWORK_STR_ID = """
    {
        "network_id": "100",
        "nodes": [
            {
                "server_name": "server1",
                "type": "clm"
            },
            {
                "server_name": "server2",
                "type": "pf"
            }
        ]
    }
    """
INVALID_NETWORK_TOO_BIG_ID = """
    {
        "network_id": 300,
        "nodes": [
            {
                "server_name": "server1",
                "type": "clm"
            },
            {
                "server_name": "server2",
                "type": "pf"
            }
        ]
    }
    """
RESULT_STR = "\nResult:"

if __name__ == "__main__":
    #
    # Server demo - simple and validated
    #
    print("Validation test for Server class...")
    print("Using this JSON input:", VALID_SERVER, RESULT_STR)
    pprint(Server(**json.loads(VALID_SERVER)))

    print("\nTrying validators...")
    print("Using this JSON input (invalid type for the age):", INVALID_SERVER)
    try:
        inv_class = Server(**json.loads(INVALID_SERVER))
    except ValueError as exc:
        print("Exception:", exc)

    #
    # Network valid demo
    #
    print("\nInitializing nested objects using JSON:", VALID_NETWORK, RESULT_STR)
    ok_net: Network = json.loads(VALID_NETWORK, object_hook=NetworkDecoder().decode)
    pprint(ok_net)

    #
    # Network invalid demo 1
    #
    print(
        "\nInitializing nested objects using invalid fields (network_id is a string):",
        INVALID_NETWORK_STR_ID,
        RESULT_STR,
    )
    pprint(json.loads(INVALID_NETWORK_STR_ID, object_hook=NetworkDecoder().decode))

    #
    # Network invalid demo 2
    #
    print(
        "\nInitializing nested objects using invalid fields (network_id is greater than max allowed):",
        INVALID_NETWORK_TOO_BIG_ID,
        RESULT_STR,
    )
    pprint(json.loads(INVALID_NETWORK_TOO_BIG_ID, object_hook=NetworkDecoder().decode))

    #
    # Already initialized but validated demo
    #
    print("\nChanging already initialized object attribute to an invalid value...")
    try:
        ok_net.network_id = 400
    except ValueError as exc:
        print("Exception:", exc)
