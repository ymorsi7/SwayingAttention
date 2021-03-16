# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 09:37:05 2021

@author: Yusuf Morsi
"""
import enchant as e

userInput = "switch"

vowelList = "aeiouAEIOU"
consonantList = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
def english_to_pig_latin(userInput):
    if userInput[0] in vowelList:
        userInputVow = userInput + 'way'
        print(userInputVow)
    else:
        for i in userInput:
            if i[0] in consonantList:
                userInput = i[1:]+i[0]
            else:
                break;
        userInputCon = userInput + 'ay'
        print(userInputCon)
            
    
english_to_pig_latin(userInput)

    












# def pig_latin_to_english():
