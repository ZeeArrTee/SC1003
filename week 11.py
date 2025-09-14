#rewrit the len function that is recursive but does not use an accumulator

list1=[1,2,3,4,5,6,7,8,9,0]

def lengt(list):
    if list ==[]: #when list is empty = 0
        return 0
    else: #when list is not empty
        return 1 + lengt(list[1:]) #cut off one from the list and compute the rest of the list
    #the recursion will compute 2,3,4,5,6,7,8,9,0
    #3,4,5,6,7,8,9,0
    #4,5,6,7,8,9,0
    #5,6,7,8,9,0
    #6,7,8,9,0
    #7,8,9,0
    #8,9,0
    #9,0
    #0
    #

print(lengt(list1))

#accumulator but tail recursive
count = 0

def accu_len(list,count):
    if list == []:
        return count #if return 0, the final count is discared to be 0
    #for i in accu_len(list[1:]): #slowly subtract the list one by one and add to the accumulator per loop
     #count += 1 dont need for loop instead add the accumulator to the recursive itself
    else:
        return accu_len(list[1:],count + 1 ) # redoes the list with a shorter list but each shortening increases count by 1

print(accu_len(list1,count))

def inter_len(list,count):
    if list == []:
        return count
    else:
        for i in list:
            count += 1

    return count

print(inter_len(list1,count))


str1='gghgoheeoboiuihfiasdhfosahgiurhsrtoyovjokbjvjrngouhanbfnguhiusehskofnojsvhoSJB'
strTest = 'aeiou'

#WRITE A CODE THAT COMPUTES NO OF VOWELS IN A STRING
#RECURSIVE BUT NOT ACCUMULATE

def str_recurv(str):
    if str == "":
        return 0
    else:
        return str_recurv(str[1:]) + 1

print(str_recurv(strTest))

#accumulate but tail recursive

count2 = 0

def str_accumu(str,count):
    if str == "":
        return count
    else:
        return str_accumu(str[1:],count + 1)

print(str_accumu(str1,count2))

#iterateion

def str_iterate(str,count):
    if str == "":
        return count
    else:
        for i in str:
            count += 1

    return count

print(str_iterate(strTest,count2))
#######################################################################################################

userinput = int(input("input the length of bits in the binary string:"))

strbin = ''

list1 = []

def generateBinaryString(n,str,list):
    if n == 0:
        list.append(str) #appends the string into the list
        return list
    else:
        generateBinaryString(n-1,str + '0',list) #appends 0 to the str and decreases n
        generateBinaryString(n-1,str + '1',list)
        return list

generateBinaryString(userinput,strbin,list1)

list2=[]
list3=[]

if userinput == 2:
    list2 = ['01','10','11']
    print(list2)
elif userinput == 1:
    print(list1)
else:

    for i in list1: #only works for n>3
        for y in range(len(i)): #iterate through excluding last elements
            if not(y==0 or y ==len(i)-1): #checking all the no before y are not 0 when y is 0
                if (i[y-1] == '0' and i[y] == '0') or (i[y]=='0' and i[y+1] == '0'):
                    list2.append(i)
    print(list1)
    print(list2)
    for i in list1:
        if i in list2:
         list1.remove(i)
    print(list1)

#############################################################################################################
#The Hamming weight of a binary string is the number of 1s occurring in it. Write a
#recursive Python function that takes in integers n ≥ 1, c ≥ 0 and returns the list of all
#binary strings (in any order) of length n and Hamming weight at most c.
#1)take input
#2)generate binary string
#3)select ones that fufill the hemming weight and puts it into a list

BinaryStringLength=int(input("input the length of binary string:"))
HemmingWeight=int(input("input the length of Hemming weight:"))

Q4list = []
Q4listFinal = []

str4 = ''

generateBinaryString(BinaryStringLength,str4,Q4list) #generates a list of n bits into Q4list

print(Q4list)

for String in Q4list:
    CountOf1 = 0  # sets the count to 0 per string
    for character in String:
        if character == '1':
            CountOf1 += 1 #gives a count of 1s
    if CountOf1 <= HemmingWeight:
        Q4listFinal.append(String)

print(Q4listFinal)

############################################################################################################################################################






