hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter hours rate:")
r = float(rate)
pay = 0
if h <= 40 :
    pay = pay + (40)*r
if h > 40 :
    pay = pay + 40*r
    pay = pay + (h-40)*r*1.5
print(pay)
