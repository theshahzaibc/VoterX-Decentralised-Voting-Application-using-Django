from web3 import Web3
import json

# Connect to the local Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
assert web3.is_connected(), "Failed to connect to the blockchain"

# Set the default account (from Ganache)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Load the contract ABI and address
with open('../build/contracts/Voting.json') as f:
    voting_contract_json = json.load(f)
    voting_contract_abi = voting_contract_json['abi']

contract_address = "0x53695aB336466513d218A0b03BE3568f9A323aBC"
voting_contract = web3.eth.contract(address=contract_address, abi=voting_contract_abi)
