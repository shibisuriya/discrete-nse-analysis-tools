-> This python script can be used to find stocks (listed in NSE) which have good liquidity.
For example, NSE opens at 9:15 AM and closes at 3:30 PM, there are exactly 22,500 seconds between the opening bell and the closing bell.
So, it is wise to trade stocks which have average volume more than 22,500 i.e., 1 stock traded per second on an average.

-> This python script downloads the historic close price (day), volume, delivery quantities and number of trades of all the stocks listed
in NSE from the NSE's achieves and calculates their mean. The date range for which the historic data needs to be downloaded can be specified
by the user, for example the user can command the script to download 6 months, 24 months or n months data. The wider
the date range the better.

-> Use a spread sheet software such as libreoffice calc or MS excel to analyse the generated data.

-> Since the ISIN of the stocks are also written into report.csv from the bhavcopy, it is very easy to import this list to a charting platform such
as tradingview or investing.com.

