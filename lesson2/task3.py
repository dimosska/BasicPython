a = int(input('Enter a: '))
b = int(input('Enter b: '))

if a > b:
    a, b = b, a
for elem in range(a, a*b+1):
    if elem % a == 0 and elem % b == 0:
        result = elem
        break
print(result)
