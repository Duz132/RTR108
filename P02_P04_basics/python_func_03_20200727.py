print('------------------')
print('Built-in functions')
print('------------------')
print(max('Hello world'))
print(min('Hello world'))
print(len('Hello world'))
print(int('32'))
print(float('3.14159'))
print(str(32))
print('------------------')
print('Math functions')
print('------------------')
import math
print(math)
print('------------------')
signal_power=14
noise_power= 6
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
print('------------------')
radians = 0.7
height = math.sin(radians)
print(height)
print('------------------')
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
print('------------------')
print('Random numbers')
print('------------------')
import random
for i in range(10):
    x = random.random()
    print(x)
print('------------------')
print(random.randint(5, 10))
print('------------------')
t = [1, 2, 3]
print(random.choice(t))
print('------------------')
print('Adding new functions, definitions and uses')
print('------------------')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()
print('------------------')
print('Parameters and arguments')
print('------------------')
def print_twice(bruce):
    print(bruce)
    print(bruce)
print('------------------')
print_twice('Spam')
print_twice(17)
import math
print_twice(math.pi)
print_twice('Spam '*4)
print_twice(math.cos(math.pi))
print('------------------')
michael = 'Eric, the half a bee.'
print_twice(michael)
print('------------------')
print('Fruitful func and void func')
print('------------------')
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
