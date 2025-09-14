def minofnodes(t):
    if len(t)==0:
        return float("inf")
    if len(t) == 1:
        sum1 = t[0]
        return sum1
    else:
        left_tree=minofnodes(t[0])
        right_tree=minofnodes(t[2])
        if left_tree>right_tree:
            sum2 = right_tree
        elif left_tree<right_tree:
            sum2 = left_tree
        else:
            sum2 = t[1]
        return sum2


def mirror(t):
    if len(t)==0:
        return []
    if len(t)==1:
        t_mirror = t[0]
    else:
        left_tree=mirror(t[0])
        right_tree=mirror(t[2])
        t_mirror = [right_tree,t[1],left_tree]
    return t_mirror


list1 = [[[-7],-1,[]],-3,[[-8],-2,[-4]]]
print(mirror(list1))
