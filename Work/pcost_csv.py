# pcost_csv.py
import csv
import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(filename)
print("Total cost:", cost)
