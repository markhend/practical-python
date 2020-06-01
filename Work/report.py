import csv
from pprint import pprint


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio


def portfolio_cost(portfolio):
    # portfolio of stocks (dict of name, shares, price)
    cost = 0.0
    for s in portfolio:
        cost += s['shares'] * s['price']
    # print(f"portfolio total cost basis {cost}")
    return cost


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


# prices = read_prices('Data/prices.csv')
# pprint(current_prices)

def portfolio_value_change(portfolio, prices):
    value = 0.0
    for s in portfolio:
        value += (prices[s['name']] -
                  s['price']) * s['shares']
    # print(f"portolio gain/loss {value:0.2f}\n")
    return value


def make_report(portfolio, prices):
    report = []
    for s in portfolio:  # s = stock
        price_change = prices[s['name']] - s['price']
        report.append(
            (s['name'], s['shares'], prices[s['name']], price_change))
    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10s %10.2f' % (r[0], r[1], '$'+str(r[2]), r[3]))
    # for name, shares, price, change in report:
    #     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')
    print()
