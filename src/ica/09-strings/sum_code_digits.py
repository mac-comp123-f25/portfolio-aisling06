def sum_digits(code_words):
    total = 0
    for word in code_words:
        digits = [ch for ch in word if ch.isdigit()]
        two_digit = int(digits[0] + digits[-1])
        total += two_digit
    return total


print(sum_digits(['jaw2n5btf9w', 'xxgg7x']))
print(sum_digits(['comp123', '1600grand', 'spring24']))
