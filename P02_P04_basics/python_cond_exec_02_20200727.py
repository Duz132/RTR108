print('------------------')
print('Boolean expressions')
print('------------------')
print(type(True))
print(type(False))
x=3
y=6
print(x != y)               # x is not equal to y
print(x > y)                # x is greater than y
print(x < y )               # x is less than y
print(x >= y)               # x is greater than or equal to y
print(x <= y)              # x is less than or equal to y
print(x is y)               # x is the same as y
print(x is not y)           # x is not the same as y
print('------------------')
print('Logical operators')
print('------------------')
x = 5
print(x > 0 and x < 10)
print('------------------')
print('If statement')
print('------------------')
x = 5
if x > 0 :
    print('x is positive')
if x < 0 :
    pass          # need to handle negative values!
print('------------------')
x = 3
if x < 10:
    print('Small')
print('------------------')
x = 5
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
print('------------------')
x = 4
y = 6
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
print('------------------')
x = 6
y = 4
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
print('------------------')
print('Try and except')
print('------------------')
inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
