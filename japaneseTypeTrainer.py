#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jt
import time

timeLimit = 10#10 segundos


#funcao que é chamada para executar o teste propriamente dito
def tryMode():
    phrase = jt.generatePhrase(5)
    phaseString = jt.generateStringRomanji(phrase)
    score = 0
    hiraphrase = str(jt.generateStringHira(phrase))
    print(hiraphrase)
    startTime = time.time()
    kstr = raw_input()
    if int(time.time() - startTime) >= timeLimit:
        print("You took too long! Meh!")
    elif kstr == phaseString:
        print("\ncorrect!")
        print("you took: " + str(time.time()-startTime))
    else:
        print("\nWrong!, it was "+str(phaseString))


def mainMenuLoop():
    score = 0
    stage = 0 #0 = normal menu 1 = ingame loop
    



tryMode()

            
    