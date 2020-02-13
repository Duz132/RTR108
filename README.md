# RTR108_2020
Datormācība(speckurss) elektroniskā klāde (2020 REBMO1 2. semestris)

## 1. nodarbība
python - python execute  
exit() - python exit  
vars() - variables  
type(a) - mainīga a tips  
print("%s"%(a.__doc__))    
ipython - ipython execute  
a. + TAB - ātrs komandas papildinājums  
print(a.__doc__)    
nano fails.py - python skripts  
python fails.py - script execute python  
python --version - noklusēta python versia  
chmod 744 fails - parāda failu par izpildāmo  
idle & - atvert shell logu  
& pēc python vai idle - komandloga strādās pēc stārtēšanas  
file - open - 2 logi ar failu un kom logu  
failā ctrl+s ; F5 - save & execute failu  
print(__builtins__.__doc__)    
__builtins__.TypeError    
cmath - kompleksu skaitļu bibliotēka  
(*)(bez()) (failā) - all  
python -m http.server 8000 &  
pēc tam firefox-ā localhost:8000 VAI 127.0.0.1 un enter - translācija  
kill - stop server  
kill -9 procesa numurs (piem kill -9 2355) - stop server process (using ps -aux | grep 8000 var atrast processa numuru)(-9 - forsēta kill)  
ngrok - serviss (public URLs)  
ps -aux | grep 8000 (kad serveris strādā) - atlasa visas rindas ar elementu 8000  
ifconfig - atrast ip?(piem 10.152.17.95)  
ls -lt ../Downloads - atrast mapi downloads  
unzip ../Downloads/ngrok-stable-linux-amd64.zip - unzip failu  
./ngrok http 8000 - startē ngrok serveri(forwarding - ip)  
"PYTHONUNBUFFERED=x python3 -m http.server &> server.log & echo $! > http.server.pid" - komanda lai būtu servera log fails  
"kill $(cat http.server.pid)" - komanda lai kill augšējas komandas serveri  
jupiter notebook - atskaitem  
BOOLEAN EXPRESSION
== - boolean (bool) expression, answer true/false (5 == 5 OR 5 == 6)  
x != y               # x is not equal to y  
x > y                # x is greater than y  
x < y                # x is less than y  
x >= y  (NOT =>)             # x is greater than or equal to y  
x <= y (NOT =<)              # x is less than or equal to y  
x is y               # x is the same as y  
x is not y           # x is not the same as y  
LOGICAL OPERATORS  
AND (x > 0 and x < 10)  
OR (n%2 == 0 or n%3 == 0)  
NOT (not (x > y) is true if x > y is false)  
CONDITIONAL EXECUTION  
IF    
if x > 0 :  
   print('x is positive')  
pass (statement does nothing, usually as a place holder for code i haven't written yet)  
if x < 0 :  
   pass    # need to handle negative values  
if x%2 == 0 :  
   print('x is even')  
else :  
   print('x is odd')  
if x < y:  
    print('x is less than y')  
elif x > y:  (ELIF = else if)  
    print('x is greater than y')  
else:  
    print('x and y are equal')  
input() - function to input sth  
int() - function to make for example string number to integer  
float() - function to make for example string number to float  
EXCEPTIONS  
TRY and EXCEPT s that you know that some sequence of instruction(s) may have a problem and you want to add some statements to be executed if an error occurs  
inp = input('Enter Fahrenheit Temperature:')  
try:  
    fahr = float(inp)  
    cel = (fahr - 32.0) * 5.0 / 9.0  
    print(cel)  
except:  
    print('Please enter a number')  
Python starts by executing the sequence of statements in the try block. If all goes well, it skips the except block and proceeds. If an exception occurs in the try block, Python jumps out of the try block and executes the sequence of statements in the except block  
FUNCTIONS  
type() - returns type of variable (type(32) -> class 'int')  
max() - returns max(strādā arī ar string (ASCII))  
min() - returns min(strādā arī ar string (ASCII))  
len() - returns number of characters in the string or tells us how many items are in its arguments  
str() - convert to string  
import math - import math module (sin, cos, log that computes logarithms base e)  
import random - import random module  
import random  
for i in range(10):  # including 0.0 but not 1.0  
    x = random.random()  
    print(x)  
range(5) - gatavo skaiļus no 0 līdz 5 neieskaitot  
randint(5, 10) - integer between 5 and 10 icluding both  
t = [1, 2, 3]  
random.choice(t)  
choice - choose an element from a sequence at random  
ADDING NEW FUNCTIONS  
def - keyword  
def print_lyrics():  
    print("I'm a lumberjack, and I'm okay.")  
    print('I sleep all night and I work all day.')  
  
To end the function, you have to enter an empty line (this is not necessary in a script).  
To execute function print_lyrics use print_lyrics()  
You can call functions in other function!  
math.sin you pass a number as an argument. Some functions take more than one argument:  
math.pow takes two, the base and the exponent.  
bruce - argument to a parameter  
LOOPS  
WHILE  
n = 5  
while n > 0:  
   print(n)  
   n = n - 1    
print('Blastoff!')  
Counts down to 5 and says Blastoff!  
INFINITE LOOP  
n = 10  
while True:  
    print(n, end=' ')  
    n = n - 1  
print('Done!')  
This loop is obviously an infinite loop because the logical expression on the while statement is simply the logical constant True  
break - exit from loop  
continue - statement to skip to the next iteration without finishing the body of the loop for the current iteration  
while True:  
    line = input('> ')  
    if line[0] == '#':  
        continue  
    if line == 'done':  
        break  
    print(line)  
print('Done!')  
  
> hello there  
hello there  
> # don't print this  
> print this!  
print this!  
> done  
Done!  
  
del a - delete variable a  
  
friends = ['Joseph', 'Glenn', 'Sally']  
for friend in friends:  
    print('Happy New Year:', friend)  
print('Done!')  
  
print("%d * %d = %d"%(a,a,a*a)) (primērs)  
  
None - special constant value which we can store in a variable to mark the variable as "empty"  
  
smallest = None  
print('Before:', smallest)  
for itervar in [3, 41, 12, 9, 74, 15]:  
    if smallest is None or itervar < smallest:  
        smallest = itervar  
    print('Loop:', itervar, smallest)  
print('Smallest:', smallest)  
