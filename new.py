import random
import time

def timeListAccess(theList):
    index = random.randint(0, len(theList))
    start = time.time()
    for x in range(0, 1000):
        newNum = theList[index]
    end = time.time()
    print("Length of List %s" % len(theList))
    print("--- %s seconds ---" % (end - start))

def doThing():
    listSize = 1000
    increaseListAmount = 1000
    while listSize <= 100000:
        newList = list(range(0, listSize))
        timeListAccess(newList)
        listSize += increaseListAmount


doThing()