def sort_012(input_list):
    """    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:       input_list(list): List to be sorted
    Use a pointer to point to the first index, the index of next expected 0 and next expected 2.
    The 1 takes care of itself. This way there is a single traversal of the list elements and hence the
    time complexity:O(n) where n is the number of elements in the list,
    space complexity:O(1) since no extra space is used."""

    next0 = 0
    next2 = len(input_list)-1
    front = 0

    while front <= next2:
        if input_list[front] == 0:
            input_list[next0],input_list[front] = 0, input_list[next0]
            next0 += 1
            front += 1
        elif input_list[front] == 2:
            input_list[next2], input_list[front] = 2, input_list[next2]
            next2 -= 1
        else:
            front += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 0, 0, 0, 0, 0])
test_function([1, 1, 1, 1, 1])
test_function([])

# Expected outputs
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 2]
# Pass
# [1, 1, 1, 1, 1]
# Pass
# []
# Pass
