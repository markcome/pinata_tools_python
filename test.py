
# TEST SCRIPT
# This is a test file from which you can take reference from the usage of "pinata_tools.py"

from pinata_tools import *

if __name__ == "__main__":

    # Params
    config_path = "pinata_key.json"
    file_path = "test.jpeg"

    # Read pinata config file
    keys = read_pinata_config(config_path)

    if (keys != None):

        # Pin the file to IPFS via Pinata
        file_URI = pin_to_IPFS(file_path, keys)

        # Unpin the file from IPFS vie Pinata
        unpin_from_IPFS(file_URI, keys)