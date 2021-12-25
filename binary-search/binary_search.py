import time
import random
# NAIVE search VS Binary search

# naive search: scan entire list and ask if its equal to target
# if yes, return index
# if no, return -1
def naive_search(l,target):
    # example l = [1,3,20,25]
    for i in range (len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conquer
# we will leverage the fact that our list is SORTED
def binary_search(l, target,low=None, high=None):
    # example: l = [1,2,3,4,5,6] should return 3 if target is 4
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    midpoint = (low+high) //2

    # not in list
    if high < low:
        return -1

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint-1) # reccursion
    else:
        # target > l[midpoint]
        # return binary_search(l[midpoint + 1:],target) without low and high parameters
        return binary_search(l,target,midpoint+1,high)

if __name__ == '__main__':
    # l = [1,2,3,45,67]
    # target = 45
    # print(naive_search(l, target))
    # print(binary_search(l, target))
    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length)) # range from -30000 to 30000
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("binary search time: ", (end-start)/length, "seconds")