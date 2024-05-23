def compare_value(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1
        
print(compare_value(3,5))
print(compare_value(5,5))
print(compare_value(5,3))