# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    tc = 0
    for line in f:
        line = line.split(',')
        tc += int(line[1]) * float(line[2])
    print("Total cost", tc)
