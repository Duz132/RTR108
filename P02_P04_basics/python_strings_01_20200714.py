text = "X-DSPAM-Confidence:  0.8475"
position1 = text.find("0")
position2 = text.find("5")
number = text[position1:position2+1]
num = float(number)
print (num)
