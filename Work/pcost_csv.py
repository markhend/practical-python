# pcost_csv.py
import csv
import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        cost = 0
        for row in rows:
            print(row)
            try:
                cost += int(row[1]) * float(row[2])
            except ValueError:
                print("warning: missing data", row)
                continue
        return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost:", cost)
