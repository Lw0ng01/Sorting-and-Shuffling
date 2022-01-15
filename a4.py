'''
Sorting and shuffling functions for Assignment 4.

Students should not modify the functions in this module.
'''

import random


def exchange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp


def selection_sort(t):
    n = len(t)
    for i in range(0, n - 1):
        min_val = t[i]
        min_i = i
        # search t[i + 1:] for the minimum value
        for j in range(i + 1, len(t)):
            elem_j = t[j]
            if elem_j < min_val:
                min_val = elem_j
                min_i = j
        # exchange t[i] and t[min_i]
        exchange(t, i, min_i)


def insertion_sort(t):
    n = len(t)
    # i is the length of the sorted sublist
    for i in range(1, n):
        # element to add to the sorted sublist is t[i]
        j = i
        if j == 0:
            return
        while j > 0 and t[j] < t[j - 1]:
            exchange(t, j, j - 1)
            j = j - 1


def insertion_sort2(t):
    n = len(t)
    for i in range(1, n):
        x = t[i]
        j = i - 1
        while j >= 0 and t[j] > x:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = x


def _merge(a, lo, mid, hi, aux):
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:
            aux[k] = a[j]; j += 1
        elif j == hi:
            aux[k] = a[i]; i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]; j += 1
        else:
            aux[k] = a[i]; i += 1
    a[lo:hi] = aux[0:n]


def _sort(a, lo, hi, aux):
    n = hi - lo
    if n <= 1: return

    mid = (lo + hi) // 2
    _sort(a, lo, mid, aux)
    _sort(a, mid, hi, aux)
    _merge(a, lo, mid, hi, aux)


def merge_sort(a):
    n = len(a)
    aux = [0] * n
    _sort(a, 0, n, aux)


def partial_shuffle(t):
    n = len(t)
    for i in range(0, n // 8):
        a = random.randrange(n)
        b = random.randrange(n)
        exchange(t, a, b)
