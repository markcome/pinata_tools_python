import requests
import json


def pin_to_IPFS(file_path, keys):
    """
    This function will pin (upload) the file to IPFS via Pinata gateway
    :param file_path: path of the file to be pinned (uploaded)
    :param keys: python dictionary which contains "API Key" and "API Secret" for Pinata API
    :return: the URI of the pinned file or None if the upload fails
    """
    # Output URI -> Choose which you prefer
    BASE_URI = "https://gateway.pinata.cloud/ipfs/"
    #BASE_URI = "https://ipfs.io/ipfs/"

    # Request info
    url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
    header = {"pinata_api_key": keys["API Key"], "pinata_secret_api_key": keys["API Secret"]}
    file = {'file': file_path}

    try:
        r = requests.post(url, headers=header, files=file, verify=True)
        print("Pinned file to IPFS with hash: {}".format(r.json()["IpfsHash"]))
        return "{}{}".format(BASE_URI,r.json()["IpfsHash"])
    except:
        print("ERROR while uploading the file to IPFS")
        return None

def unpin_from_IPFS(file_uri, keys):
    """
    This function will unpin (delete) the file from IPFS via Pinata gateway
    :param file_uri: URI of the file to be unpinned (deleted)
    :param keys: python dictionary which contains "API Key" and "API Secret" for Pinata API
    :return: true or false
    """
    # Request info
    url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
    header = {"pinata_api_key": keys["API Key"], "pinata_secret_api_key": keys["API Secret"]}
    file_hash = file_uri.split("/")[4]
    params = {"hashToUnpin": file_hash}

    try:
        r = requests.delete(url, headers=header, params= params , verify=True)
        print("Unpinned file to IPFS with hash: {}".format(file_hash))
        return True
    except Exception as e:
        print("ERROR while unpinning the file from IPFS")
        print(e)
        return False


def read_pinata_config(file_path):
    """
    This function read the Pinata json configuration file which contains "API Key" and "API Secret" for Pinata API
    :param file_path: path of the json file to read
    :return: python dictionary containing the info or None if fails
    """
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    except:
        print("ERROR while reading the pinata config file")
        return None




