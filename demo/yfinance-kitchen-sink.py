# kitchen sink for using yfinance

# github: https://github.com/ranaroussi/yfinance
# pip install: pip install yfinance --upgrade --no-cache-dir
# conda install: conda install -c ranaroussi yfinance
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print("Stock Info:")
print(msft.info)

# get historical market data
print("Historical Market Data:")
hist = msft.history(period="max")
print(hist)

# show actions (dividends, splits)
print("Actions:")
print(msft.actions)

# show dividends
print("Dividends:")
print(msft.dividends)

# show splits
print("Splits:")
print(msft.splits)

# show financials
print("Financials:")
print(msft.financials)
print(msft.quarterly_financials)

# show major holders
print("Major Holders:")
print(msft.major_holders)

# show institutional holders
print("Institutional Holders:")
print(msft.institutional_holders)

# show balance sheet
print("Balance Sheet:")
print(msft.balance_sheet)
print(msft.quarterly_balance_sheet)

# show cashflow
print("Cashflow:")
print(msft.cashflow)
print(msft.quarterly_cashflow)

# show earnings
print("Earnings:")
print(msft.earnings)
print(msft.quarterly_earnings)

# show sustainability
print("Sustainability:")
print(msft.sustainability)

# show analysts recommendations
print("Analyst Recommendations:")
print(msft.recommendations)

# show next event (earnings, etc)
print("Next Event:")
print(msft.calendar)

# show options expirations
print("Option Expirations:")
print(msft.options)

# get option chain for specific expiration
# data available via: opt.calls, opt.puts
opt = msft.option_chain(msft.options[0])
print("1st Option Expiration - " + msft.options[0] + ":")
print(opt)
