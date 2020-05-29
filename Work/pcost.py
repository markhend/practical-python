# pcost.py


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        cost = 0
        for line in f:
            line = line.split(',')
            cost += int(line[1]) * float(line[2])
        return cost


cost = portfolio_cost('Data/portfolio.csv')
print("Total cost", cost)
