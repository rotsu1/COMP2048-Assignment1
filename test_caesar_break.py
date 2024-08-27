# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

message = "Lzrsdq ne bqxosnfqzogx"

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#part b
#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    #INSERT CODE TO REMEMBER MAX
    if freq > maxFreq and letter != " ":
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for index, letter in enumerate(letters):
    if letter == "e":
        e = index
    elif letter == maxLetter:
        maxLetterPosition = index
shift = maxLetterPosition - e
print("Predicted Shift:", shift)

totalLetters = 26
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        invkeys[letters[(index + shift) % 26]] = letter
    else: #uppercase
        invkeys[letters[((index + shift) % 26) + 26]] = letter
print("Cypher Dict:", invkeys)

decryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string

#part c

#get the counts of letters in lowercase
lowercase_message = message.lower()
letter_counts = Counter(lowercase_message)

maxFreq = -1
maxLetter = None
#get most frequent letter
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    if freq > maxFreq and letter != " ":
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#get the position of most frequent letter
for index, letter in enumerate(letters):
    if letter == maxLetter:
        maxLetterPosition = index


#get invkeys for each shifts
for i in range(1,26):
    invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
    for index, letter in enumerate(letters):
        # cypher setup
        if index < totalLetters: #lowercase
            invkeys[letters[(index + i) % 26]] = letter
        else: #uppercase
            invkeys[letters[((index + i) % 26) + 26]] = letter
    decryptedMessage = []
    #decrypt
    for letter in message:
        if letter == ' ': #spaces
            decryptedMessage.append(letter)
        else:
            decryptedMessage.append(invkeys[letter])
    print(f"{i} shifts")
    print("Decrypted Message:", ''.join(decryptedMessage) + '\n') #join is used to put list inot string    