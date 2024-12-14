import os

filepath = 'primes.txt'

if os.path.exists(filepath):
    print('found!')
else:
    print('not found :(')


def turnRawToListOfInt():
    with open('primes.txt','r') as file:
        content = file.read()
    clean = content.replace('\n', '')
    stringList = clean.split(',')
    integer_list = [int(num) for num in stringList if num.strip().isdigit()]
    print(len(integer_list))
#    print(integer_list)
    return integer_list




        
       


        
        
        
       
#        number_list = (int(num) for num in lines.replace("\n", ",").split(",") if num.strip())
#        final_numbers = list(number_list)
#        print(f"length of final numbers is {len(final_numbers)}")
#        print(final_numbers[1:250:3])
#        return final_numbers
#        
turnRawToListOfInt()



