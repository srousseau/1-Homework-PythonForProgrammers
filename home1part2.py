# Scott Rousseau
# Homework 1 part 2

def queueadd(inputList, value):
    inputList.append(value)
    return inputList
	
def queueretrieve(inputList):
    return inputList.pop(0)
	
initialQueue = [1,2,3]
print "Initial Queue " 
print initialQueue
print "Queue after adding 7 "
print queueadd(initialQueue,7)
queueretrieve(initialQueue)
print "Queue after retrieving FIFO item"
print initialQueue


