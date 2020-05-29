# pcost.py


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        cost = 0
        for line in f:
            line = line.split(',')
            try:
                cost += int(line[1]) * float(line[2])
            except ValueError:
                print("warning: missing data", line)
                continue
        return cost


cost = portfolio_cost('Data/missing.csv')
print("Total cost", cost)

