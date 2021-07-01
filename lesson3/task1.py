def list_average(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)


a = [8, 10, 47, 13, 2, 6]

print(list_average(a))  # 14.333333333333334
