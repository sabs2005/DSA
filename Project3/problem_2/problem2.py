def rotated_array_search(input_list, number, start, end):
    """    Find the index by searching in a rotated sorted array
    Args:       input_list(array), number(int): Input array to search and the target
    Returns:       int: Index or -1
    Time complexity: log n since we use binary search
    Space complexity: O(1) since no extra space is used."""

    if start > end:
        return -1

    mid = (start + end) // 2
    if input_list[mid] == number:
        return mid
    if ((input_list[start] <= input_list[mid] and input_list[mid] >= number >= input_list[start])
            or
            (input_list[start] > input_list[mid] and number > input_list[mid])):
        end = mid - 1
    else:
        start = mid + 1
    return rotated_array_search(input_list, number, start, end)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number, 0, len(input_list) - 1):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[0,1,2,3,4], 4])
test_function([[0,1,2,3,4], 5])
test_function([[-1,0,1,2,3,4], 4])

# Expected outputs
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass