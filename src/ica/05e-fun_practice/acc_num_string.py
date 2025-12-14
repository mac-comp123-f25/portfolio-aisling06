def string_of_nums(n):
    ans_str = ""
    for x in range(1, n+1):
        ans_str = ans_str + str(x)
        ans_str = ans_str + " "
    return ans_str

print(string_of_nums(10))