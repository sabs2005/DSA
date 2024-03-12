def rearrange_digits(input_list):
    """    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:       input_list(list): Input List
    Returns:       (int),(int): Two maximum sums
    On a descending sorted list put numbers at even indices and odd indices
    in a list each and return the list.
    Time complexity: Merge sort has the time complexity on nlogn so this program has that time complexity.
    Space complexity:O(1) since no extra space is used."""

    input_list = mergesort(input_list)
    # get 2 lists of numbers at even indices and odd indices from the sorted input list
    list1 = [n for i, n in enumerate(input_list) if i % 2 == 0]
    list2 = [n for i, n in enumerate(input_list) if i % 2 != 0]
    # create concatenated numbers from elements in each list
    num1 = sum(d * 10**i for i, d in enumerate(list1[::-1]))
    num2 = sum(d * 10 ** i for i, d in enumerate(list2[::-1]))

    return [num1, num2]

def mergesort(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    left_ind = 0
    right_ind = 0
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            merged.append(right[right_ind])
            right_ind += 1
        else:
            merged.append(left[left_ind])
            left_ind += 1
    merged += left[left_ind:]
    merged += right[right_ind:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 1], [1, 0]])
test_function([[1, 1, 1], [11, 1]])
test_function([[], []])

# Expected outputs
# Pass
# Pass
# Pass
# Pass
# Pass
