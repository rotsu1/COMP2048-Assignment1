# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"

##Break the code via brute force search
i = 0
start_time = time.time()
for i in range(0, 26):
    key1 = chr(65 + i)
    for s in range(0, 26):
        key2 = chr(65 + s)
        for f in range(0, 26):
            key3 = chr(65 + f)
            key = key1 + key2 + key3
            engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                    rotor.ROTOR_II, rotor.ROTOR_III, key=key,
                                    plugs="AA BB CC DD EE")
            decrypted_code = engine.encipher(ShakesHorribleMessage)
            i += 1
            if decrypted_code[-12:] == crib:
                print(decrypted_code)
                print(f"It took {time.time() - start_time} seconds and {i} tries.")
                print(f"The key is {key}")

#part e
#3 rotors = 26^3 = 17576
#5 rotors + plug board = 5 * 4 * 3 * 26^3 * (26! / {6! * 10! * 2^10}) =  1.5896255521782635e+20
#Supose it takes 1/2 number of tries on average to get the decrypted code.
#Then it takes 8788 tries for 3 rotors and 7.948127760891317e+19 for 5 rotors and a plugboard.
#Therefore, it takes 9044296496235000 times more tries to get the original message for 5 rotors.