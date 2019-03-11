#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jt
import time
import os

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
        print("You took too long: " +  str(time.time()-startTime) + "seconds")

    elif kstr == phaseString:
        print("\ncorrect!")
        print("you took: " + str(time.time()-startTime))
    else:
        print("\nWrong!, it was "+str(phaseString))
    time.sleep(4)
    mainMenuLoop()

def printMainMenu():
    os.system("clear")
    print("---------------")
    print(":\t start training :press 1\n")
    print(":\t exit           :press 0\n")
    optn = input("write option")
    if optn == 0:
        exit(0)
    elif optn == 1:
        tryMode()
    else:
        print("Uknown option...")
        mainMenuLoop()

    
    


def mainMenuLoop():
    score = 0
    stage = 0 #0 = normal menu 1 = ingame loop
    if stage == 0:
        printMainMenu()

    



mainMenuLoop()

            
    