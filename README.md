# VoterX - Decentralised Voting Application using Django
A decentralized voting platform built using Django, Web3.py, and Ethereum smart contracts. This platform allows users to register as voters and cast their votes in a secure, transparent, and decentralized manner.

# Table of Contents
+ [Features](#features)
+ [Prerequisites](#prerequisites)
+ [Installation](#installation)
+ [Running the Project](#running-the-project)
+ [Smart Contracts](#smart-contracts)
+ [License](#license)
# Features
+ **Decentralized Voting:** Secure and transparent voting using Ethereum smart contracts.
+ **Voter Registration:** Admin can register voters by their Ethereum addresses.
+ **Voting:** Registered voters can cast their votes for candidates.
+ **Results:** Retrieve the current vote counts for each candidate.
# Prerequisites
Before you begin, ensure you have the following installed on your machine:

+ [Python 3.8+](https://www.python.org/downloads/)
+ [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/)
+ [Ganache](https://archive.trufflesuite.com/ganache/) (for local Ethereum blockchain)
+ [Truffle](https://archive.trufflesuite.com/) (for deploying smart contracts)

# Installation
1. Clone the repository:
```
git clone https://github.com/theshahzaibc/VoterX-Decentralised-Voting-Application-using-Django.git
cd VoterX
```
2. Set up Python environment:
```
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```
# Running the Project
1. Start Ganache:
Open Ganache and create a new workspace or quickstart a blockchain.
2. Deploy the smart contracts:
```
truffle migrate --reset
```
3. Configure Django settings:
Update the Django settings with the deployed contract address and ABI in `settings.py`.

4. Run Django development server:
```
python manage.py runserver
```
# Smart Contracts
The smart contracts are located in the `VoteX/contracts` directory. The primary contract is `Voting.sol`, which handles voter registration, voting, and tallying of votes.

**Deployment**
Smart contracts are deployed using Truffle. The deployment scripts are in the `VoteX/migrations` directory.

**Interacting with Smart Contracts**
We use `web3.py` to interact with the smart contracts from the Django backend. The contract ABI and address must be configured in `contract.py`.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
