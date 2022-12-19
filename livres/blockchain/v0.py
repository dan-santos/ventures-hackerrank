# V0
# -- Classe bloco
# 	init: dado, tempo, previous_hash, hash
# 	calculate_hash
#
# -- Classe blockchain
# 	init: create_genesis
# 	create_genesis
# 	add_block
# 	verifica_blockchain

import time
from hashlib import sha256
import json

class Block:
    def __init__(self, index: int, data, previous_hash: str):
        self.index = index
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = previous_hash

    
    def calculate_hash(self):
        json_block = json.dumps(self.__dict__, ensure_ascii=False, sort_keys = True).encode("utf-8")
        hash_block = sha256(json_block).hexdigest()
        return hash_block
    

# block = Block(0, "Transação", "oi")

class Blockchain:
    def __init__(self):
        # self.array = [Block(0, 'Bloco_Genesis', ''),]
        self.array = []
        self.array.append(self.create_block('Genesis'))

    def create_block(self, data):
        if len(self.array) == 0:
            index = 0
            previous_hash = 'nao tem'
        else:
            index = self.array[-1].index + 1
            previous_hash = self.array[-1].hash
        
        block = Block(index, data, previous_hash,)
        
        block.hash = block.calculate_hash()
        self.array.append(block)


blockchain = Blockchain()
print(blockchain.array[0].__dict__)
blockchain.create_block(Block(1, 'Primeira transação', ''))
print(blockchain.array[1].__dict__)