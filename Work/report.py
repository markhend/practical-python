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
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio


# portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
# pprint(portfolio)
total_cost = 0.0
for s in portfolio:
    # print(s)
    total_cost += s['shares'] * s['price']
print(f"portfolio total cost basis {total_cost}")
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


current_prices = read_prices('Data/prices.csv')
# pprint(current_prices)

total_value = 0.0
for holding in portfolio:
    total_value += (current_prices[holding['name']] -
                    holding['price']) * holding['shares']
print(f"portolio gain/loss {total_value:0.2f}\n")


def make_report(portfolio, prices):
    report = []
    for s in portfolio:  # s = stock
        price_change = prices[s['name']] - s['price']
        report.append(
            (s['name'], s['shares'], prices[s['name']], price_change))
    return report


report = make_report(portfolio, current_prices)
print('%10s %10s %10s %10s' % ('Name', 'Shares', 'Price', 'Change'))
seps = ('-'*10)
print('%10s %10s %10s %10s' % (seps, seps, seps, seps))
for r in report:
    print('%10s %10d %10s %10.2f' % (r[0], r[1], '$'+str(r[2]), r[3]))
print()
# for name, shares, price, change in report:
#     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
