# Boo Bear Sort
import random

#Basic variables
badInput = 0;

#First, get parms from user
listSize = int(input("How many elements are we sorting? (between 2 and 100)"))
if (listSize < 2 or listSize > 100):
    badInput = 1
    print("Bad Input")
    quit()
arraySize = int(input("What is the largest number? (must be bigger that the number of elements and less than 1000)"))
if (arraySize < listSize or arraySize > 1000):
    badInput = 2
    print("Bad Input")
    quit()

# Create array and assign zeros to all elements
sortArray = [0] * arraySize

# Create List
unsortList = []
for i in range(0,listSize):
    unsortList.append(random.randint(1,arraySize))

print("Original Unsorted List:")
print(unsortList)

#Starting Sort here

sortedList = []

for i in range(0, listSize):
    arrayX = unsortList[i]
    sortArray[arrayX] +=1

for i in range(0,arraySize):
    while sortArray[i] > 0:
        sortedList.append(i)
        sortArray[i] -=1

# Print Sorted List
print("Sorted List:")
print(sortedList)
