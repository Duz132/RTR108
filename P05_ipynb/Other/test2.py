init = float(0.9)
l = []
for i  in range(0,31):
    print("i=",i)
    l.append(init + ( float(i) / 100 ))
    print("l ",i," = ",l[i])
