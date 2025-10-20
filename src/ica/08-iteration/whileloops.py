def print_every_other(x):
    while x >= 0:
        print(x)
        x = x - 2
    print("Done!")


def print_every_fifth(x):
    while x >= 0:
        print(x)
        x = x - 5
    print("Done!")
print_every_other(7)
print_every_fifth(20)

def square_user_nums():
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)
    while user_num >= 0:
        print(user_num, "squared is", user_num ** 2)
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)
square_user_nums()

def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number (excluding the input number itself).
    """
    curr_val = 0   # loop variable
    total = 0      # accumulator variable
    while curr_val < topNum:
        total = total + curr_val
        curr_val = curr_val + 1
    return total

def add_user_nums():
    sum_of_nums = 0
    user_inp = input("Enter a number (0 to quit): ")
    user_num = int(user_inp)
    while user_num != 0:
        sum_of_nums = sum_of_nums + user_num   # update accumulator
        user_inp = input("Enter a number (0 to quit): ")  # ask again
        user_num = int(user_inp)

    return sum_of_nums
sum_to_n(5)
add_user_nums()


def nextWord(text):
    """
    Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next
    sequence of characters up to a space, tab, or newline.
    """
    wordStr = ""
    i = 0
    for ch in text:
        if ch in " \t\n":  # if character is space, tab (\t), or newline (\n)
            break
        else:
            wordStr = wordStr + ch
    return wordStr

def square_user_nums2():
    while True:
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)
        if user_num < 0:
            break
        print(user_num, "squared is", user_num ** 2)
print(nextWord('hello world'))
square_user_nums2()
