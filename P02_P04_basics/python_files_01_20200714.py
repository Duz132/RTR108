# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ovval = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    position = line.find("0")
    value = line[position:]
    value = float(value)
    count = count + 1
    ovval = ovval + value
average = ovval/count
print("Average spam confidence:", average)
