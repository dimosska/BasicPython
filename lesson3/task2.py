def arg_sum(*elems):
    result = 0
    for el in elems:
        result += el
    return result


print(arg_sum(1, 2, 3, 4, 85))  # 95
