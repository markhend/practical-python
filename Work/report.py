import csv
import fileparse


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    # portfolio = []
    # with open(filename) as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         record = dict(zip(headers, row))
    #         stock = {
    #             'name': record['name'],
    #             'shares': int(record['shares']),
    #             'price': float(record['price'])
    #         }
    #         portfolio.append(stock)
    return fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])


def portfolio_cost(portfolio):
    # portfolio of stocks (dict of name, shares, price)
    cost = 0.0
    for s in portfolio:
        cost += s['shares'] * s['price']
    # print(f"portfolio total cost basis {cost}")
    return cost


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    # prices = {}
    # with open(filename, 'r') as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         try:
    #             stock, price = row
    #             prices[stock] = float(price)
    #         except ValueError:
    #             # print("missing data...skipping row")
    #             continue
    return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))


# prices = read_prices('Data/prices.csv')

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


def main(argv):
    files = argv[1:-1]
    for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, 'Data/prices.csv')
        print()


if __name__ == '__main__':
    # files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
    import sys
    main(sys.argv)
