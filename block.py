from time import time

class Block:
    def __init__(self, index,text, previousHash, privatehash, publicHash):
        self.index = index
        self.text = text
        self.time = time()
        self.prevPublicHash = previousHash

        # private hash is a list of 2 primes
        self.privateHash = privatehash

        #public hash is a number that is the product of privateHash[0] and privateHash[1]
        self.publicHash = publicHash
    def getPublicHash(self):
        return self.publicHash
    def verifyPrivateAndPublic(self, candidate1, candidate2):
        if candidate1 * candidate2 == self.privateHash:
            return True
        else:
            return False
        

    def __str__(self):
        return f"index : {self.index}, text : {self.text}, time created : {self.time} 
        previous block hash : {self.previousHash}, 
        current block hash : {self.hash}"
