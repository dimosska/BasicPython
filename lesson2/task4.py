n = int(input('Enter number:'))
sum = 0
for i in range(1, n+1):
    sum += int(input(f'Enter number #{i}: '))

result = sum/n
print(result)
