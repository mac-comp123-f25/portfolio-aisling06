def  sum3(values):
    """ Return the sum of the first three numbers"""
    assert type(values) is list or type(values) is tuple
    assert len(values) >= 3
    assert type(values[0]) is int or type(values[0]) is float
    assert type(values[1]) is int or type(values[1]) is float
    assert type(values[2]) is int or type(values[2]) is float
    return values[0] + values[1] + values[2]

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) )
  print( sum3(5) )
  print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )
