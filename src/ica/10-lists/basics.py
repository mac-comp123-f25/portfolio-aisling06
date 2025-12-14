def every_other(list):
    return list[::2]
print (every_other([1, 2, 3]))

def sum_positive(numbers):
    return sum(x for x in numbers if x > 0)
print (sum_positive([-1, 1, 2, 3]))