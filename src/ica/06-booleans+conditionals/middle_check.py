def middle_value(num1, num2, num3):
    if num1 > num2 and num1 < num3:
        return num1
    elif num1 < num2 and num2 < num3:
        return num2
    else:
        return num3

if __name__ == "__main__":
  assert middle_value(5, 2, 77) == 5
  assert middle_value(-10, 50, 57) == 50
  assert middle_value(-1, -6, -3) == -3
  print("All tests passed!")
