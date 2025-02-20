from collections import deque
def nums_square_sorted(nums):
    result = deque()
    l, r = 0, len(nums)-1

    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])

        if left > right:
            result.appendleft(left*left)
            l = l + 1
        else:
            result.appendleft(right*right)
            r= r - 1

        print(result)
    return(list(result))

nums = [-4, -1, 0, 3, 10]
print(nums_square_sorted(nums))