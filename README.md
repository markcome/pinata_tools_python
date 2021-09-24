# Pinata tools for Python
*** 
This project contain a set of Pinata tools fot Python designed by SignorCrypto
***

## Pinata API Keys
The Pinata API Keys are used as the authentication method to interact 
with your Pinata account. After you created a Pinata account 
you can create API Keys.
Once you created the new dedicated API Keys you have to put them 
in the ```pinata_key.json``` file.

## Pinata tools
The ```pinata_tools.py``` file contains a set of tools to interact with IPFS via 
Pinata gateway. In particular:
- ```read_pinata_config``` function is used to read the Pinata 
API keys from the ```pinata_key.json``` file.
- ```pin_to_IPFS``` function pin (upload) to IPFS via Pinata gateway the file given as parameter
 and return the URI of the pinned file.
- ```unpin_from_IPFS``` function unpin (delete) from IPFS via Pinata gateway
 the file corresponding to the URI given as parameter.
 
In order to run these function the script need the ```requests``` python module (https://docs.python-requests.org/en/latest/user/install/#install).

## Test
The ```test.py``` file contains an example of the utilization of the above described functions. The test will pin and unpin the ```test.jpeg``` image.

***
