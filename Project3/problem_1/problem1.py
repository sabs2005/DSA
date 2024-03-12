def binarySearchSqrt(number):
    """Use binary search to ."""
    if number == 0 or number ==1:
        return number
    if number < 0:
        return('invalid input')
    start = 0
    end = number//2
    while start <= end:
        mid = (start + end)//2
        if mid*mid == number:
            return mid
        elif mid * mid < number:
            start = mid + 1
            sqrt = mid
        else:
            end = mid-1
    return sqrt


print ("Pass" if  (3 == binarySearchSqrt(9)) else "Fail")
print ("Pass" if  (0 == binarySearchSqrt(0)) else "Fail")
print ("Pass" if  (4 == binarySearchSqrt(16)) else "Fail")
print ("Pass" if  (1 == binarySearchSqrt(1)) else "Fail")
print ("Pass" if  (5 == binarySearchSqrt(27)) else "Fail")
print ("Pass" if  ('invalid input' == binarySearchSqrt(-4)) else "Fail")
print ("Pass" if  (100 == binarySearchSqrt(10000)) else "Fail")
print ("Pass" if  (1 == binarySearchSqrt(2)) else "Fail")

# Expected output
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass