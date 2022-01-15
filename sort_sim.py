import random
import time
import a4

def time_to_sort(sorter, t):
    '''
    Returns the times needed to sort lists of sizes sz = [1024, 2048, 4096, 8192]

    The function sorts the slice t[0:sz] using the sorting function
    specified by the caller and records the time required in seconds.
    Because a slice is sorted instead of the list t, the list t is not modified by
    this function. The list t should have at least 8192 elements.

    The times are returned in a list of length 4 where the times in seconds
    are formatted strings having 4 digits after the decimal point making it easier to
    print the returned lists.

    Parameters
    ----------
    sorter : function
             A sorting function from the module a4.
    t : list of comparable type
        A list of elements to slice and sort.

    Returns
    -------
    list of str
        The times to sort lists of lengths 1024, 2048, 4096, and 8192.

    Raises
    ------
    ValueError
        If len(t) is less than 8192.
    '''
    if len(t) < 8192:
        raise ValueError('not enough elements in t')
    times = []
    for sz in [1024, 2048, 4096, 8192]:
        # slice t
        u = t[0:sz]
        # record the time needed to sort
        tic = time.perf_counter()
        sorter(u)
        toc = time.perf_counter()
        times.append(f'{toc - tic:0.4f}')
    return times

def sim_sorted():
    t = list(range(8192))
    sort_helper2(t)

def sim_partial():
    t = list(range(8192))
    a4.partial_shuffle(t)
    sort_helper2(t)

def sim_reverse():
    t = list(reversed(range(8192)))
    sort_helper2(t)

def sim_shuffled():
    t = list(range(8192))
    random.shuffle(t)
    sort_helper2(t)

def sort_helper(t_list, sort_method, sort_name):
    time_list = time_to_sort(sort_method, t_list)
    print(time_list, sort_name)

def sort_helper2(t):
    sort_helper(t, a4.selection_sort, "selection sort")
    sort_helper(t, a4.insertion_sort, "insertion sort 1")
    sort_helper(t, a4.insertion_sort2, "insertion sort 2")
    sort_helper(t, a4.merge_sort, "merge sort")

sim_sorted()
sim_reverse()
sim_reverse()
sim_shuffled()

"""
the insertion sort method is still slower for a list that has any sort of variation, 
but excels in sorting lists that have some sort of order. Merge sort is fast regardless.
"""
