# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)
total = 0.0
for s in portfolio:
    # print(s)
    total += s['shares'] * s['price']
print(total)
