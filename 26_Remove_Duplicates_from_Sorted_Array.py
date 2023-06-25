def removeDuplicates(nums):
    # there are two pointers one is l which start from l=1
    # other pointer start with r=1
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:  # this compares the value from previous row
            nums[l] = nums[r]
            l = l+1
    print(nums)
    return l

    # this is an example of linear code since there is no extra memoery allocations


if __name__ == "__main__":

    import sys

    nums = sys.argv[1]
    nums = list(eval(nums))
    print(nums)
    a = removeDuplicates(nums)
    print(a)

# EXAMPLE here input is [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] output we get as [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
# beyond k=5 it doesnt matter what you print

#Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
