def remove_all(value, lst):
    while lst.count(value) > 0:
        lst.remove(value)
nums = [-1, 1, 2, 3]
remove_all(1, nums)
print(nums)

