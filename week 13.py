def merge_sort(data, key):
    if len(data) < 2:
        return data
    leftlist = data[:len(data)// 2]
    rightlist = data[len(data)// 2:]

    leftlist = merge_sort(leftlist,key)
    rightlist = merge_sort(rightlist,key)

    return merge(leftlist, rightlist, key)


def merge(left, right, key):
    final = []
    while left and right:
        if left[0][key] < right[0][key]:
            final.append(left[0])
            left.pop(0)
        elif left[0][key] > right[0][key]:
            final.append(right[0])
            right.pop(0)

    if left:
        final.extend(left)
    if right:
        final.extend(right)

    return final


persons = [
    {"name": "bob", "age": 15},
    {"name": "alice", "age": 12},
    {"name": "dave", "age": 13},
    {"name": "carol", "age": 10}]


list2 = merge_sort(persons,"age")

for i in list2:
    print(i)

def rule_to_binary(rule_number):
    rule_number=bin(int(rule_number))
    return f"{rule_number:08b}"

print (f"{12:344}")