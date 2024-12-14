from time import time
import random
import hashlib
from block import Block
import _json
from rawToList import turnRawToListOfInt
from transaction import Transaction
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.all_transactions = []
        self.length = 0

    def newBlock(self, proof,text, previous_hash=None):

        prevH = self.last_block.getPublicHash()
        newH = self.hash()

        pubH = newH.pop(0)
        privH = newH

        newB = Block(len(self.chain), text, prevH, privH, pubH)
        self.chain.append(newB)
        return newB
    def createGenesis(self):
        #in the future, these will be random
        prevH = 14
        newH = 2627 


        genesis = Block(0,'First Block!',prevH, newH)
        if len(self.chain) == 0:
            self.chain.append(genesis)
        else:
            print('chain not empty tf u think u doin')
    
    def mineBlock(self):
        if not self.pending_transactions:
            print("no transactions to mine at this time")
            return
        prevH = self.last_block.getPublicHash() 
        newH = self.hash()
        pubH = newH.pop(0)
        privH = newH
        newB = Block(len(self.chain),f"this is the {len(self.chain)}th block",prevH, privH, pubH)
        self.pending_transactions = self.pending_transactions[1:]
        return
        

    def newTransaction(self, sender, receiver, amount):
        #creates a new transaction and appends it to the transaction chain
        transac = Transaction(sender, receiver, amount)
        self.pending_transactions.append(transac)



    #returns a list with 3 integers [public, priv1, priv2]
    def hash():
        #hashes a block using 
        random1 = random.randint(0,70000)
        random2 = random.randint(0,70000)
        while random1 == random2:
            random2 = random.randint(0,7000)
        intList = turnRawToListOfInt()
        return [intList[random1] * intList[random2], intList[random1], intList[random2]]
    
    def calculateHash(self):

        pass
    #verifies that every block's hash is equal to the hash AND
    #checks that the previous publicHash is equal to the product of its two private
    def isChainValid(self):
        index = len(self.chain) - 1
        while index < len(self.chain):
            prevB = self.chain[index - 1]
            currB = self.chain[index]

            if currB.verifyPrivateAndPublic() is False:
                print("somethin wrong!")
                return False
            if currB.previousHash != prevB.powHelper():
                print('something wrong')
                return False
            index -= 1
        return True
    
 
    

    def printEntireChain(self):
        for index in range(len(self.chain)):
            print(self.chain[index])
        return

    @property
    def last_block(self):
        return self.chain[-1]

    #takes in a previous block and a current block)
    # compares the public hash of the previous block with the two private of the previous
    def proofOfWork(self, prevBlock, currBlock):
        
        intList= turnRawToListOfInt()
        lenintList = len(intList)
        goal = prevBlock.getPublicHash()
        checker = currBlock.getPREVPublicHash()

        #check if previousNode.publicHash is equal to currNode.previousPublicHash
        if goal != checker:
            return False

        #if they are equal, we want to check that the privateHash(list of 2 primes)
        # is equal to the product of two primes that we are going to be finding here 

        #we use binary search to make this algorithm O(n * log_2(n)) time complexity
        for pi in range(0,lenintList):
            lo = 0
            hi = lenintList
           

            proof = intList[pi]



            while lo < hi:
                mid =  (hi + lo) // 2
                last_proof = intList[mid]
                result = self.validProof(last_proof,proof,goal)
                if result == 0:
                    print('found that hoe!')
                    print('double checking')
                    if last_proof * proof == goal:
                        return True

                elif result > 0:
                    high = mid -1
                else:
                    lo = mid + 1 
        print("nothign found!")
        return False

    def validProof(candidate1, candidate2, prevPubHash):
        return (candidate1 * candidate2 )- prevPubHash
        '''
        validate the proof, does the hash of last_proof and current_proof
        multiply up to the goal
        
        ''' 
    def powHelper(self, prevB, currB):
        return self.proofOfWork(self,prevB,currB)

