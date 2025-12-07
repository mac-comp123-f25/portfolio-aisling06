money = 732
dollars = money // 100
money1_remain = money - dollars * 100
quarters = money1_remain // 25
money2_remain = money1_remain - quarters * 25
dimes = money2_remain // 10
money3_remain = money2_remain - dimes * 10
nickels = money3_remain // 5
money4_remain = money3_remain - nickels * 5
pennies = money4_remain // 1
money5_remain = money4_remain - pennies
print(f"""Dollars: {dollars}
Quarters: {quarters}
Dimes: {dimes}
Nickels: {nickels} 
Pennies: {pennies}""")

