def difference(*args):
    if not args:
        print(0)
    else:
        max_value = max(args)
        min_value = min(args)
        result = round(max_value - min_value, 2)
        print(result)


difference(1, 2, 3)
difference(5, -5)
difference(10.2, -2.2, 0, 1.1, 0.5)
difference()
