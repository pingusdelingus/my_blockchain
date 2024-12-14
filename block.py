from time import time
import datetime
#https://portfolio-2md0.onrender.com/
class Block:
    def __init__(self, index,text, previousPublicHash, privatehash, publicHash):
        self.index = index
        self.text = text
        self.time = time()
        self.prevPublicHash = previousPublicHash

        # private hash is a list of 2 primes
        self.privateHash = privatehash

        #public hash is a number that is the product of privateHash[0] and privateHash[1]
        self.publicHash = publicHash
    
    def getPREVPublicHash(self):
        return self.prevPublicHash
    def getPublicHash(self):
        return self.publicHash
    def verifyPrivateAndPublic(self,):
        candidate1 = self.privateHash.pop(0)
        candidate2 = self.privateHash.pop(0)
        if candidate1 * candidate2 == self.publicHash:
            return True
        else:
            return False
    def verifyCandidates(self, cand1, cand2):
        list1 = []
        list1.append(cand1)
        list1.append(cand2)
        return set(list1) == set(self.privateHash)
    def putUnsafe(self):
        print(f"private hash : {self.privateHash}, public hash : {self.publicHash}, previous public hash : {self.prevPublicHash}")

        

    def __str__(self):
        t = self.time
        dt_object = datetime.datetime.fromtimestamp(t)
        formatted_date_time = dt_object.strftime("%d/%m/%Y %H:%M:%S")
        t = formatted_date_time
        return f"index : {self.index}, text : {self.text}, time created : {t} \nprevious block hash : {self.prevPublicHash}, \ncurrent block public hash : {self.publicHash}"
