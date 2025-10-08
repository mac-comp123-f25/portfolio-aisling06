def add_tax(price, tax_rate):
    print('adding tax inputs:', price, tax_rate)
    tax_amt = price * tax_rate
    print(tax_amt, 'return value:', price + tax_amt)
    return price + tax_amt
total = add_tax(25.99, 0.0725)
total = round(total, 2)
print(total)