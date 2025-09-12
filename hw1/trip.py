price_per_gallon = 3.16
miles_per_gallon = 25
miles = 750
gas_tank = 19.5
total_gallon = miles / miles_per_gallon
total_price = total_gallon * price_per_gallon
miles_one_tank = gas_tank * miles_per_gallon
number_of_stops = miles / miles_one_tank
total_price = round(total_price, 2)
number_of_stops = int(number_of_stops)
print("The trip distance is", miles, ".", "Total cost of gas is $", total_price, ".", "Number of stops is", number_of_stops, ".")
