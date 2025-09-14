import csv
import math
import sys

#This loads all the information from records.csv into a array so we can manipulate it
studentList = []

with open('C:/Users/tokyo/OneDrive/Desktop/SC1003/records.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if not row[0][0] == "T":#Easy hack to remove the header
            studentList.append(row)

#Dynamic value for extra marks!
GROUPSIZE = 5

#Sorts the students by tutorial groups
#This allows for easier manipulation later
def tutorialSortingFunc(e):
    return e[0]

studentList.sort(key=tutorialSortingFunc)

#We could just use a lambda function...could be too complicated...
#studentList.sort(key=lambda arr : arr[-1])

tutorialList = []

#Seperate students into tutorial groups(arrays)
#Seperate by checking the previous student's tutorial group, if different, create new tutorial group(array)
#This allows for easier manipulation
for i in range(0,len(studentList)):
    #if the current item(Tutorial Group) in the student array is not the same as the previous, we create a new array in the tutorial list
    if(studentList[i][0] != studentList[i-1][0]):
        tutorialList.append([])
    tutorialList[int(i/50)].append(studentList[i])#TODO REVIEW THIS, does this make sense
    

#Test Data
# tutorialList = [
#     [
#     ['G-1', '5002', 'CCDS', 'Aarav Singh', 'Male', '4.1'],  #
#     ['G-1', '4479', 'CCDS', 'Amelia Kim', 'Male', '4.6'], #
#     ['G-1', '2091', 'SOC', 'Adlan Bin Rahman', 'Male', '4.79'],
#     ['G-1', '1383', 'CCDS', 'Areeba Khan', 'Female', '4.8'],#
#     ['G-1', '2091', 'SOC', 'Adlan Bin Rahman', 'Male', '4.9'],
#     ['G-1', '3838', 'WKW SCI', 'Aarti Nair', 'Female', '4.95'], #
#     ['G-1', '4479', 'WKW SCI', 'Amelia Kim', 'Female', '5'], #
# ]
# ]

#This just returns the last item in the studentInfo Array which is the cGPA,
#This allows the .sort function to use it as a key to sort all the students
def cgpaSortingFunc(e):
    return e[-1]

#Enters Selected Student Info into Dictionary, then return it
#This allows us to track and easily reference info of students have selected.
def enterInfoIntoDictionary(studentInfo,genderSchoolDict):
    if studentInfo[2] in genderSchoolDict:#If theres <school name> in the dictionary's keys
        genderSchoolDict[studentInfo[2]] = genderSchoolDict[studentInfo[2]] + 1
        #We add to it
    else:
        genderSchoolDict[studentInfo[2]] = 1
        #Otherwise we create a new key and give it a value of 1

    if studentInfo[4] in genderSchoolDict:#If theres <gender> in the dictionary's keys
        genderSchoolDict[studentInfo[4]] = genderSchoolDict[studentInfo[4]] + 1
        #We add to it
    else:
        genderSchoolDict[studentInfo[4]] = 1
        #Otherwise we create a new key and give it a value of 1

    return genderSchoolDict
        
#This handles all the manipulation of the tutorialGroup Array we have to do
#such as iterating through to search for valid students
def handleValidityOfStudent(tutorialGroup,pointer,genderSchoolDict):

    secondBest = sys.maxsize

    #Can we improve this?, what are the benefits of starting from 0 and 
    #iterating rather than starting from the pointer? TODO 
    #This is here to calculate how many students we need to iterate over on each side

    if pointer < 0:
        itemsRight = abs(pointer + 1)
        
        #Normalize negative pointers
        #This is done so we can standardize working with one form of indexing(either positive or negative)
        pointer = len(tutorialGroup) + pointer
    else:
        itemsRight = len(tutorialGroup) - (pointer + 1)
    
    itemsLeft = pointer
    
    #Status can only be 3 values:
    #Valid=Both Gender and School is valid:
    #Here we want to just return the valid pointer
    #Invalid=Both Gender and School is invalid
    #Here we want to ignore the pointer and go next
    #<Pointer>(int)=Either Gender and School is valid
    #Here we want to check with our current secondBest,
    #To determine whether we need to change our secondBest, we need to determine how far 
    #the current and incoming secondBest is from the pointer
    #for the current, we can just abs(secondBest-pointer) for the absolute distance(no neg values)
    #for the incoming, we can just use x as it represents how far the incoming secondBest is from the pointer

    #Checks all items on the left of the pointer along with the student that the pointer is point to
    for x in range(0, itemsLeft + 1):
        status = checkValidityOfStudent(tutorialGroup,pointer-x,genderSchoolDict)

        if status == "Valid":
            print("Found Valid Student at the right",pointer-x)

            return pointer - x
        elif type(status) == int:
            if abs(secondBest-pointer) == x:#Edge case(Like edging)

                #In the case where the distances between the current and the incoming secondbest are the same
                #We will compare using their difference in cGPA, since the pointer's cGPA is the ideal one
                #We will then take the one with the least difference(most ideal)
                pointerCGPA = float(tutorialGroup[pointer][-1])
                currentSecondBestCGPA = float(tutorialGroup[secondBest][-1])
                incomingSecondBestCGPA = float(tutorialGroup[pointer-x][-1])

                if abs(pointerCGPA - currentSecondBestCGPA) > abs(pointerCGPA-incomingSecondBestCGPA):
                    secondBest = pointer - x
                    print("Second Best Changed",pointer - x)

            elif abs(secondBest-pointer) > x:
                secondBest = pointer - x
                print("Second Best Changed",pointer - x)

    #Checks all items on the right of the pointer
    for x in range(1, itemsRight + 1):
        status = checkValidityOfStudent(tutorialGroup,pointer+x,genderSchoolDict)

        if status == "Valid":
            print("Found Valid Student at the left",pointer+x)
            return pointer + x
        elif type(status) == int:
            if abs(secondBest-pointer) == x:#Edge case(Like edging)

                #In the case where the distances between the current and the incoming secondbest are the same
                #We will compare using their difference in cGPA, since the pointer's cGPA is the ideal one
                #We will then take the one with the least difference(most ideal)
                pointerCGPA = float(tutorialGroup[pointer][-1])
                currentSecondBestCGPA = float(tutorialGroup[secondBest][-1])
                incomingSecondBestCGPA = float(tutorialGroup[pointer+x][-1])

                if abs(pointerCGPA - currentSecondBestCGPA) > abs(pointerCGPA-incomingSecondBestCGPA):
                    secondBest = pointer+x
                    print("Second Best Changed",pointer + x)

            elif abs(secondBest-pointer) > x:
                secondBest = pointer+x
                print("Second Best Changed",pointer+x)
    
    #If we reach this point, we have not found a valid student and need to pick the secondBest option
    print("Ran out of students,give up")

    if secondBest == sys.maxsize:
        #If we have not found the secondBest, we simply return the original pointer 
        #as there is not even 1 "half valid" student
        #therefore the best option would be to choose based on cGPA
        print("Returned original pointer")
        return pointer
    else:
        print("Returned second best")
        return secondBest


def checkValidityOfStudent(tutorialGroup,pointer,genderSchoolDict):
    print("---------------------Checking Validity")
    print("Checking Validity of student",tutorialGroup[pointer])
    print("Pointer is at",pointer)
    print("Checking Against",genderSchoolDict)

    #If gender valid but school valid?
    #We need a second best incase we cant find the best
    schoolValid = True
    genderValid = True

    #We are checking the validity before we add the student
    #Therefore the valid number to check against would be the 
    #number that makes the school/gender the majority - 1
    #>= is equivalent

    if(tutorialGroup[pointer][2] in genderSchoolDict and genderSchoolDict[tutorialGroup[pointer][2]] >= int(GROUPSIZE/2)):#invalid due to School
        schoolValid = False

    if(tutorialGroup[pointer][4] in genderSchoolDict and genderSchoolDict[tutorialGroup[pointer][4]] >= int(GROUPSIZE/2)):#invalid due to Gender
        genderValid = False
    
    if(schoolValid and genderValid):
        print("Found Valid")
        return "Valid"
    elif(schoolValid or genderValid):
        print("Found a second best",pointer)
        return pointer
    else:
        print("Found Invalid")
        return "Invalid"

#CGPA sorting function

#Iterates through every tutorial group and sorts them by CGPA
#This is because for our algorithim, we have to get the highest, lowest then the middle
#Therefore it makes sense for us to sort everything for ease of access: 
#[0] would be the first item(Highest), [-1] would be the last item(lowest) etc.

#This flag is here to signify that its the last in group already,
#This saves us from having to calculate whether or not its the last again?
last = False

#We use this dictionary to store information about the students already chosen in the group.
#This allows us an easy way to see how many times a certain school or gender has been selected
currentGenderSchoolDict = dict()

for x in range(0,len(tutorialList)):
    tutorialGroup = tutorialList[x]

    tutorialGroup.sort(key=cgpaSortingFunc)

    totalGroupList = []#This will hold all the groups in the tutorial class
    groupingList = []#This will hold the current group being modified

    for y in range(0,len(tutorialGroup)):#iterates every tutorial group

        #CGPA choosing process

        #TODO Make it so if its even, we dont run the middle function, 
        #better to pick from the top and bottom only
        if y % GROUPSIZE == GROUPSIZE-1:#if it is the last member
            studentPointer = int(len(tutorialGroup)/2)
            last = True

        #if it is odd
        #we want to pick from the bottom
        elif y % 2:
            studentPointer = -1

        #if it is even  
        #we want to pick from the top
        else:
            studentPointer = 0   

        #Check if this student is valid
        studentPointer = handleValidityOfStudent(tutorialGroup,studentPointer,currentGenderSchoolDict)
        
        #Process the chosen student

        #Add it to the current group
        groupingList.append(tutorialGroup[studentPointer])
        
        #Add its information to the dictionary
        currentGenderSchoolDict = enterInfoIntoDictionary(tutorialGroup[studentPointer],currentGenderSchoolDict)
        
        #Remove it from the tutorial group
        tutorialGroup.pop(studentPointer)

        #If we reach the last student in the student in the tutorial group or the group
        #we want to add the group to the total group list
        #we then reset all the important variables so we can repeat the process again
        if last or not len(tutorialGroup):#prevents the lookup to conserve resources, LOLOLOLOL
            totalGroupList.append(groupingList)

            currentGenderSchoolDict = dict()
            groupingList = []
            last = False
    #We then replace the ungrouped tutorial group with the grouped one
    tutorialList[x] = totalGroupList

print(tutorialList[0])
    
    




