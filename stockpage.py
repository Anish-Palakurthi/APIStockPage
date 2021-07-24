import requests  # needed for API pull
import json  # allows for json manipulation
import numpy as np
import matplotlib.pyplot as plt


date = input(
    "Enter a date in the form YEAR-MONTH-DAY from the last year")
stockOne = input("Enter the stock which you want information for:")
stockTwo = input("Enter a second stock you would like to compare to:")
# inputs for user

dates = []
closes1 = []
closes2 = []
# arrays for data storage

# "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=TSLA&date_from=2021-05-14"


def isDateReal(date):  # simplistic check that the date is properly formatted
    splitDate = date.split("-")
    splitDate[1] = splitDate[1].strip("0")
    splitDate[2] = splitDate[2].strip("0")

    if(int(splitDate[0]) != 2020):
        if(int(splitDate[0]) != 2021):
            print("year is invalid")
            return False
    if(int(splitDate[1]) > 12 or int(splitDate[1]) < 1):
        print('month is invalid')
        return False
    if(int(splitDate[2]) > 31 or int(splitDate[2]) < 1):
        print('day is invalid')
        return False

    return True

# takes two stocks and empties closing prices into respective arrays


def addData(date, stock1, stock2):
    dateUse = date
    api = requests.get(  # contacts API
        "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols={symbol1}&date_from={day}".format(day=dateUse, symbol1=stock1))

    data = api.text
    parsed_json = json.loads(data)
    # adds in each data and close price into array from data list
    for x in range(len(parsed_json["data"])):
        date = (
            (parsed_json["data"])[x])["date"]
        dates.append(date)
        close1 = ((parsed_json["data"])[x])["close"]
        closes1.append(close1)

    api = requests.get(
        "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols={symbol2}&date_from={day2}".format(day2=dateUse, symbol2=stock2))

    data = api.text
    parsed_json = json.loads(data)
    # same as before except only closing prices for second stock
    for x in range(len(parsed_json["data"])):
        close2 = ((parsed_json["data"])[x])["close"]
        closes2.append(close2)


if (isDateReal(date) == False):
    exit()  # precheck for date

addData(date, stockOne, stockTwo)  # add data into arrays


#x = np.arange(1, (len(closes1)+1))

x = np.array(dates)  # stores axes' values from arrays
y = np.array(closes1)
z = np.array(closes2)

plt.title('{sym1} (Green) vs {sym2} (Blue)'.format(
    sym1=stockOne, sym2=stockTwo))
plt.xlabel("Date")
plt.ylabel('Value of Share ($)')
plt.plot(x, y,  color='green')
plt.plot(x, z, color='blue')
plt.savefig("chart.png")
plt.show()
