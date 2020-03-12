Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
>>> a
10
>>> a^2
8
>>> a*a
100
>>> a-2
8
>>> a^2
8
>>> a+
SyntaxError: invalid syntax
>>> a+2
12
>>> __builtins__
<module 'builtins' (built-in)>
>>> print(__builtins__.__dco__)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(__builtins__.__dco__)
AttributeError: module 'builtins' has no attribute '__dco__'
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
Traceback (most recent call last):
  File "/home/user/RTR108/python_test.py", line 6, in <module>
    print(cos(a))
NameError: name 'cos' is not defined
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
Traceback (most recent call last):
  File "/home/user/RTR108/python_test.py", line 7, in <module>
    print(cos(a))
NameError: name 'cos' is not defined
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
-0.8390715290764524
-0.8390715290764524
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10, 'math': <module 'math' (built-in)>, 'cos': <built-in function cos>}
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
-0.8390715290764524
-0.8390715290764524
Traceback (most recent call last):
  File "/home/user/RTR108/python_test.py", line 13, in <module>
    print(cos_V1(a))
NameError: name 'cos_V1' is not defined
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
-0.8390715290764524
-0.8390715290764524
-0.8390715290764524
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
-0.8390715290764524
-0.8390715290764524
-0.8390715290764524
(-0.8390715290764524+0j)
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
-0.8390715290764524
-0.8390715290764524
-0.8390715290764524
-0.8390715290764524
(-0.8390715290764524+0j)
>>> 
================= RESTART: /home/user/RTR108/python_test.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_test.py', 'a': 10}
-0.8390715290764524
-0.8390715290764524
-0.8390715290764524
-0.8390715290764524
(-0.8390715290764524+0j)
-0.8390715290764524
>>> history
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    history
NameError: name 'history' is not defined
>>> diary
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    diary
NameError: name 'diary' is not defined
>>> 
