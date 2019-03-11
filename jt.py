#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import codecs
import sys


#nonsensical random hiragana string generator.
    #it generates a random string, the point is to Type as fast as possible the result in romanji
          
hiraDict = {
    "a":"あ",
    "e":"え",
    "i":"い",
    "o":"お",
    "u":"う",
    "ka":"か",
    "ke":"け",
    "ki":"き",
    "ko":"こ",
    "ku":"く",
    "na":"な",
    "ne":"ね",
    "ni":"に",
    "no":"の",
    "nu":"ぬ",
    "ma":"ま",
    "me":"め",
    "mi":"み",
    "mo":"も",
    "mu":"む",
    "wa":"わ",
    "wo":"を",
    "chi":"さ",
    "se":"せ",
    "shi":"し",
    "so":"そ",
    "su":"す",
    "ha":"は",
    "he":"へ",
    "hi":"ひ",
    "ho":"ほ",
    "hu":"ふ",
    "ra":"ら",
    "re":"れ",
    "ri":"り",
    "ro":"ろ",
    "ru":"る"

}

listOfChars = [

    "a",
    "e",
    "i",
    "o",
    "u",
    "ka",
    "ke",
    "ki",
    "ko",
    "ku",
    "wa",
    "wo",
    "ha",
    "he",
    "hi",
    "ho",
    "shi",
    "chi",
    "na",
    "ne",
    "ni",
    "no",
    "nu",
    "ra",
    "re",
    "ri",
    "ro",
    "ru"         
    ]

syllabCount = listOfChars.__len__()
hiraString = list()



def generateRandomSyllab():
    ind = random.randint(0,syllabCount-1)
    ch = listOfChars[ind]
    return ch

def generatePhrase(size):
    phraze = list()
    for ind in range(size):
        phraze.append(generateRandomSyllab())
    return phraze



def generateStringRomanji(phrase):
    finalstr = str()
    for k in phrase:
        finalstr += k
    return str(finalstr)

def generateStringHira(phrase):
    finalstr = str()
    for k in phrase:
        finalstr += hiraDict.get(k)
    return str(finalstr)



