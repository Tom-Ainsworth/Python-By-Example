nums = [1, 2, 3, 4]


def reverse(arr):
    length = len(arr)
    print(length)
    for i in range(0, len(arr), 1):
        nums[i] = arr[int(len(arr))]


reverse(nums)

print(nums)
