from blockchain import Blockchain
import random
import string

def getRandomString(length):
    characters = string.ascii_letters + string.digits
    # Generate a random string by randomly selecting characters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

mychain = Blockchain()

#creating genesis block

mychain.createGenesis()

print(mychain)

mychain.newBlock("this is da 2nd cuh")


for index in range(0, 30):
    length = random.randint(0,50)
    randomStr = getRandomString(length)
    mychain.newBlock(randomStr)

print(len(mychain.chain))

print(mychain)

result = mychain.isChainValid()

if result == True:
    print('hooray!')
else:
    print(':(')

