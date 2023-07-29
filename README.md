# Pashiz

Pashiz, with the symbol of `PSZ`, is an ERC-20 token that can be deployed on EVM-compatible blockchains. It has been developed with [Solidity](https://github.com/ethereum/solidity) and [Brownie](https://github.com/eth-brownie/brownie).


## Deployed Contract

Pashiz has been deployed in the Sepolia network in `0x9aa5Af5a2ea931a54FC48A0D73a5ab396E619f52`.  
Token information is accessible in Etherscan by this link:  
https://sepolia.etherscan.io/token/0x9aa5af5a2ea931a54fc48a0d73a5ab396e619f52


## How to Deploy and Test

1. Install Brownie (check the [installation guide](https://github.com/eth-brownie/brownie#installation)).  
2. Run `brownie compile` to compile contracts. it will build artifacts in `build/contracts`.  
3. Add your account to brownie accounts and replace its id in the `get_account` method of `scripts/deploy.py`, you don't need to do this step if you want to deploy on [ganache](https://github.com/trufflesuite/ganache).  
4. Run `brownie run scripts/deploy.py` to deploy the contract.  The deployment log will be stored in `build/deployments`.  
5. You can run the tests with the `brownie test`.  
