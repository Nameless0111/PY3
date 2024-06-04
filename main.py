from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, address
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware,layer=0)

contract = w3.eth.contract(address=address,abi=abi)
print(w3.eth.get_balance('0xfAD4fd3730c7a45e4F9CCA54f909E902D9225104'))
print(w3.eth.get_balance('0x412a5Cd80B25ab8Eed118aB4Ad3494Cd3e14B2cc'))
print(w3.eth.get_balance('0x2Acf673e87C72ff87e94AB4df14634e7E0a2f1B5'))
print(w3.eth.get_balance('0xE12FEf4899757Ed07FfD6B6d77713fbeF87088B1'))
print(w3.eth.get_balance('0x557496f8894Bb25D29Fe66ece57EDa1c57Bd886c'))