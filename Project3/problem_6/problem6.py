def get_min_max(ints):
    """    Return a tuple(min, max) out of list of unsorted integers.
    Args:       ints(list): list of integers containing one or more intgers
    time complexity: O(n) n is the number of items in list
    space complexity = O(1)"""

    if len(ints) == 0:
        return None
    max = ints[0]
    min = ints[0]
    for i in range(len(ints)):
        if ints[i] < min:
            min = ints[i]
        if ints[i] > max:
            max = ints[i]
    return (min, max)


### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1000)]  # a list containing 0 - 1000
random.shuffle(l)
print("Pass" if ((0, 999) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 0)]  #an empty list
random.shuffle(l)
print("Pass" if (None == get_min_max(l)) else "Fail")

l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

# Expected outputs
# Pass
# Pass
# Pass
# Pass