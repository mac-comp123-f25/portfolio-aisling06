import math
def rect_area(wid, len):
    wid = math.ceil(wid)
    len = math.ceil(len)
    area = wid * len
    return area
def roof_cost(area, sqf_cost):
    cost = area * sqf_cost
    return cost
def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)
print(estimate_green_roof(54.25, 32.8, 35))