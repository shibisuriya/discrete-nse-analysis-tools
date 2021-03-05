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

-> The report.csv present in this folder was created on 05-mar-2021 using 12 months historic data.

-> I used libreoffice calc to filter out some stocks which have `Average no. of trades` > 22,500 (as on 05-mar-2021) i.e., on an average more than 1 trade 
gets executed every second of the trading day (in the past 12 months i.e., from 05-mar-2020 to 05-mar-2021) in these scrips. Similarly filters of user's choice
can be applied to the columns of this .csv file (report.csv).
According to the analysis (as on 05-mar-2021) there are about 1,546 stocks listed in NSE of which only 171 stocks are listed before
365 days (i.e., before 05-mar-2020), have `Average number of trade` > 22500 and `Average volume` >= 22500. It is a good idea to trade
on only these 170 stocks since other stocks have insufficient daily OHLC data to perform reliable technical analysis on or they have
low liquidity. Refer ./liquidStocks.csv. 