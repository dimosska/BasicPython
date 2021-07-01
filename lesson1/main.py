a = int(input('Enter a: '))
oper = input('Enter operation: ')
b = int(input('Enter b: '))
if oper == '+':
    result = a+b
elif oper == '-':
    result = a-b
elif oper == '*':
    result = a*b
elif oper == '/':
    result = a/b
else:
    print('bad input')
print(result)
