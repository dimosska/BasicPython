def factorial(n):
    result=1
    if n<1:
        return result
    else:
        for i in range(1,n+1):
            result*=i
    return result

print(factorial(5)) #120
print(factorial(7))  # 5040
print(factorial(30))  # 265252859812191058636308480000000
