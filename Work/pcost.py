# pcost.py


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        cost = 0
        for rowno, row in enumerate(f, start=1):
            row = row.split(',')
            try:
                cost += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")
                continue
        return cost


cost = portfolio_cost('Data/missing.csv')
print("Total cost", cost)
