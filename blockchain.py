from time import time
import random
import hashlib
import _json
from rawToList import turnRawToListOfInt
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.length = 0

    def newBlock(self, proof, previous_hash=None):
        #create a new block and APPEND to chain
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.current_transactions,
            'proof' : proof,
            'previous_hash' : self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def newTransaction(self, sender, receiver, ammount):
        #creates a new transaction and appends it to the transaction chain
        transaction = {
            'SENDER' : sender,
            'RECEIVER' : receiver,
            'AMMOUNT' : ammount            
        }
        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        #hashes a block using 
        random1 = random.randint(0,78497)
        random2 = random.randint(0,78497)
        while random1 == random2:
            random2 = random.randint(0,78497)


    @property
    def last_block(self):
        return self.chain[-1]

    
    def proofOfWork(self, last_proof, goal):
        
        intList= turnRawToListOfInt()
        lenintList = len(intList)
        
        
        for pi in range(0,lenintList):
            lo = 0
            hi = lenintList
           

            proof = intList[pi]
            last_proof = intList[mid]


            while lo < hi:
                mid =  (hi + lo) // 2
                last_proof = intList[mid]
                result = self.validProof(last_proof,proof,goal)
                if result == 0:
                    print('found that hoe!')
                    return [proof, last_proof]
                elif result > 0:
                    high = mid -1
                else:
                    lo = mid + 1 






        
        
        return proof

    def validProof(last_proof, proof, goal):
        return (last_proof * proof )- goal
        '''
        validate the proof, does the hash of last_proof and current_proof
        multiply up to the goal
        
        ''' 