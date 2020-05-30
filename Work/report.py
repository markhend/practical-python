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
# pprint(portfolio)
total = 0.0
for s in portfolio:
    # print(s)
    total += s['shares'] * s['price']
print(f"portfolio total cost basis ${total}")
print()

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock, price = row
                prices[stock] = float(price)
            except ValueError:
                # print("missing data...skipping row")
                continue
    return(prices)

prices = read_prices('Data/prices.csv')
# pprint(prices)

for holding in portfolio:
    print(prices[holding['name']])