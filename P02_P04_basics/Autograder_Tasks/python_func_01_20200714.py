def computepay(h,r):
    if h > 40 : 
        pay = 40*r
        pay = pay + (h-40)*r*1.5
    return pay
hrs = input("Enter Hours:")
hf = float(hrs)
rate = input("Enter rate:")
rf = float(rate)
p = computepay(hf,rf)
print("Pay",p)
