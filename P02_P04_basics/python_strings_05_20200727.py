print('------------------')
print('Strings, length of a string, traversal through a string with a loop')
print('------------------')
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
print('------------------')
print('String slices')
print('------------------')
s = 'Monty Python'
print(s[0:5])
print(s[6:12])
fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])
print('------------------')
print('String are immutable')
print('------------------')
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)
print('------------------')
print('Looping and counting')
print('------------------')
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
print('------------------')
print('String comparison')
print('------------------')
word = input('Enter word\n')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
print('------------------')
print('Parsing strings')
print('------------------')
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)
