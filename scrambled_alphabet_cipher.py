from microbit import *
 
# Atbash cipher.
def scrambled_alphabet(text):
    alpha  = "abcdefghijklmnopqrstuvwxyz 123456789:,{}'"
    crypta = "b2mnf}3ay,p16 lu7v4j:{'58czgiot9xkhswqedr"
    result = ""
 
    for letter in text:
        index = alpha.find(letter)
        result = result + crypta[index]
 
    return result
 
# The script starts executing statements from here.
 
sleep(1000)
 

print()
 
while True:
    plaintext = input("Enter a string: ")
    
    result = scrambled_alphabet(plaintext)
 
    print("result =", result)