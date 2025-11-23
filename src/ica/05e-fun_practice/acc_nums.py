def sum_range(start_val, end_val):
    cnt = 0     # initialize accumulator to default value 0
    for x in range(start_val, end_val + 1):
        cnt = cnt + x     # update: add new x value to old value of cnt
    return cnt
#Call the function with a straightforward example of adding numbers in a range
print( sum_range(1, 3) )
#Call the function where the start and end values passed in are the same number
print(sum_range(5,5))
#Call the function where the start value is greater than the end value
print( sum_range(3,1) )
#Call the function where both values are negative
print( sum_range(-5,-3) )
