print('------------------')
print('While loop')
print('------------------')
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print('------------------')
print('Infinite loop')
print('------------------')
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
print('------------------')
print('Finishing iterations with continue')
print('------------------')
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
print('------------------')
print('For loop')
print('------------------')
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
print('------------------')
print('Counting and summing loops')
print('------------------')
count = 0
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    total = total + itervar
print('Count: ', count)
print('Total: ', total)
print('------------------')
print('Max loops')
print('------------------')
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
print('------------------')
print('Min loops')
print('------------------')
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
