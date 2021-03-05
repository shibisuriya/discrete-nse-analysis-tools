import pandas as pd
from nsepy.history import get_price_list
from nsepy import get_history
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import timedelta 
import csv 

#Get the time peroid for which the historic data
mon = int(input("How many months data do you want to download (from today)? "))
endDate = date.today()
startDate = date.today() - relativedelta(months=+mon)
print("Start date: ", startDate)
print("End date: ", startDate)

#Get the symbol of all the stocks trading in NSE (National stock exchange of India) by downloading the previous day's bhavcopy.
yesterday = date.today() - timedelta(days = 1) 
prices = get_price_list(dt=yesterday)

#This script is going to write the results to both the console and a .csv file.
#Print the column names on the console
print("Symbol", "Average price", "Average volume", "Average no. of trades", "Average deliverable qty", "fromDate", "toDate", "NoOfDays")

#Open a .csv file to write the results.
#Writing the column names to the .csv file.
csvFile = open("report.csv", 'w+', newline = '')
columns = [["Symbol", "Average price", "Average volume", "Average no. of trades", "Average deliverable qty", "fromDate", "toDate", "NoOfDays"]]
write = csv.writer(csvFile) 
write.writerows(columns) 

#Open a text file to note down the names of the stocks which generate an exeception.
fail = open("fail.txt", "w+")

#Select stocks one by one from `prices` and download its historic data for the range specified by `startDate` and `endDate`.
for symbol in prices['SYMBOL']:
    try:
        data = get_history(symbol=symbol, start=startDate, end=endDate)
        averagePrice = round(data['Close'].mean())
        averageVolume = round(data['Volume'].mean())
        averageNoOfTrades = round(data['Trades'].mean())
        averageDeliverableQty = round(data['Deliverable Volume'].mean())

        #If a stock gets listed 3 months back and we ask nsepy to download 6 months historic data (starting from today), then nsepy retrieves only 3 months data 
        #instead of throwing an exeception. So, it is important to note the number of days between the `startDate` and the `endDate`.
        fromDate = max(data.index)
        toDate = min(data.index)
        NoOfDays = (fromDate - toDate).days
    except ValueError:
        print("*********** %s: valueError ***********" %symbol)
        fail.write(symbol + "\n")

    else:
        #Write the result to the .csv file.
        row = [[symbol, averagePrice, averageVolume, averageNoOfTrades, averageDeliverableQty, fromDate, toDate, NoOfDays]]
        write.writerows(row) 

        #Write the result to the console.
        print(symbol, averagePrice, averageVolume, averageNoOfTrades, averageDeliverableQty, fromDate, toDate, NoOfDays)

csvFile.close()
fail.close()