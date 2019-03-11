#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jt
import time
import os

class gVars:

    timeLimit = 10#10 segundos
    tries = 0.0
    score = 0.0
    sumAllTimes = 0
    totalTime = 0
    #average = sumAllTimes/ tries

#funcao que é chamada para executar o teste propriamente dito
def tryMode():
    gVars.tries +=1
    phrase = jt.generatePhrase(5)
    phaseString = jt.generateStringRomanji(phrase)
    score = 0
    hiraphrase = str(jt.generateStringHira(phrase))
    print(hiraphrase)
    startTime = time.time()
    kstr = raw_input()
    elapsedTime = time.time()-startTime
    if int(elapsedTime) >= gVars.timeLimit:
        print("You took too long: " +  str(elapsedTime) + "seconds")

    elif kstr == phaseString:
        print("\ncorrect!")
        print("you took: " + str(elapsedTime)+ "Seconds ")
        gVars.score += 1
    
    else:
        print("\nWrong!, it was "+str(phaseString))
    
    #avoid divide by 0 lol
    gVars.sumAllTimes += elapsedTime
    #gVars.tries += 1

    time.sleep(4)
    mainMenuLoop()

def printMainMenu():
    os.system("clear")
    print("---------------")
    print("|This is a Hirana reading practice tool.")
    print("|your goal is to write in romanji what you read as fast as possible")
    print("|This will help you improve your read speed ")
    print("-----------------------------1")
    #avoid divide by zero 
    if gVars.tries > 0:
        print("current tries:"+ str(gVars.tries) + " average time: "+ str(gVars.sumAllTimes/gVars.tries) + " Seconds ")
        print("success rate: "+ str(gVars.score/gVars.tries))
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
    stage = 0 #0 = normal menu 1 = ingame loop
    if stage == 0:
        printMainMenu()

    



mainMenuLoop()

            
    