'''
Search related functions for Assignment 4.
'''


def sort1000(t):
    aux = [0] * 1000
    if not t:
        return
    else:
        for e in t:
            aux[e] += 1
        t = []
        for i in range(0, 1000):
            if aux[i] > 0:
                t += [i] * aux[i]
        return t


def min_val(t):
    if not t:
        return
    elif len(t) == 1:
        return t[0]
    else:
        x = len(t) // 2
        list1 = t[:x]
        list2 = t[x:]
        min1 = min_val(list1)
        min2 = min_val(list2)
        if min1 > min2:
            return min2
        else:
            return min1


