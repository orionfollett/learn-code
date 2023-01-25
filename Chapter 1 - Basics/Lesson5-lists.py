#Lesson 5 - Lists

#What if you have multiple enemies in your game, and they each have a variable that tracks if they can see the player

#You could do something like this:
canFirstEnemySeePlayer = False
canSecondEnemySeePlayer = True
canThirdEnemySeePlayer = False
#etc...

#This would get old pretty quickly, so instead Python has something called a list.

#A list is a collection of data
#it looks like this:
enemyDetectionList = [False, True, False]

#you can access values in a list by putting brackets after the name of the list and typing an index:
enemyDetectionList[0] # all lists start at 0, this would access the first item in the list
enemyDetectionList[1]#this is the next item
enemyDetectionList[2]#this is the last item

print(enemyDetectionList[0])
print(enemyDetectionList[1])
print(enemyDetectionList[2])

#enemyDetectionList[100] #if you try to access an item that is not in the list, like in this case the 100th item, it will error

#There are lots of cool things you can do with lists, for example what if you wanted to add a fourth enemy?

print("Before append " + str(enemyDetectionList))
enemyDetectionList.append(True)
print("After append " + str(enemyDetectionList))




