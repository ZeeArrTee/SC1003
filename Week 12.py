from operator import length_hint

Lx = [132,43,2,45,854,3255,223,1,464,567]
def mergesort(list1):
    lenght = len(list1)
    if len(list1)<2:
        return list1
    else:
        leftlist = list1[:lenght//2]
        rightlist = list1[lenght//2:]

        leftlist= mergesort(leftlist)
        rightlist = mergesort(rightlist)
        return merge(leftlist,rightlist)

def merge (leftlist,rightlist):
    sorted_list = []
    while leftlist and rightlist:
        if leftlist[0] < rightlist[0]:
            sorted_list.append(leftlist[0])
            leftlist.pop(0)
        elif leftlist[0] > rightlist [0]:
            sorted_list.append(rightlist[0])
            rightlist.pop(0)

    if leftlist:
        sorted_list.extend(leftlist)
    if rightlist:
        sorted_list.extend(rightlist)

    return sorted_list

print(mergesort(Lx))

def bubblesort(list1):
    for passnum in range(len(list1)):
        for i in range(len(list1)-passnum-1):
            if list1[i]>list1[i+1]:
                temp = list1[i+1] #swapping method
                list1[i+1] = list1 [i]
                list1[i] = temp
        print("pass:",passnum)
    return list1


print(bubblesort(Lx))
max