from flask import Flask, redirect, url_for, render_template, request
import requests  # needed for API pull
import json  # allows for json manipulation
import numpy as np
import matplotlib.pyplot as plt
import cgi
import cgitb


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

  # add data into arrays


# x = np.arange(1, (len(closes1)+1))
def createChart(stockOne, stockTwo):
    x = np.array(dates)  # stores axes' values from arrays
    y = np.array(closes1)
    z = np.array(closes2)

    plt.title('{sym1} (Green) vs {sym2} (Blue)'.format(
        sym1=stockOne, sym2=stockTwo))
    plt.xlabel("Date from {firstDay} to current day".format(firstDay=dates[0]))
    plt.ylabel('Value of Share ($)')

    ax = plt.gca()

    ax.axes.xaxis.set_ticklabels([])

    plt.plot(x, y,  color='green')
    plt.plot(x, z, color='blue')

    plt.grid(True)

    plt.savefig("chart.png")
    plt.close()

    # plt.show()


form = cgi.FieldStorage()
datePrime = form.getvalue('dt')
print(datePrime)
stock1Prime = form.getvalue('s1')
stock2Prime = form.getvalue('s2')

if (isDateReal(datePrime) == False):
    print("bad date")
    exit()  # precheck for date

addData(str(datePrime), stock1Prime, stock2Prime)
dates.reverse()
createChart(stock1Prime, stock2Prime)

f = open("stockpage.html", "w")  # opens html page under the handle
message = """<html>
    <head> </head>
    <body> <img src = "chart.png" </body>
    </html>"""
# by using .format, I can replace the interim variables in the message variable with the newly updated data retrieved from the API without having to couple the order of the words or deal with lengthy parantheses
f.write(message)
f.close()

'''
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if (request.method == "POST"):
        datePrime = request.form["dt"]
        print("data has been retrieved")
        stock1Prime = request.form["s1"]

        stock2Prime = request.form["s2"]

        return ("Check out stockpage.html!")

    else:

        return render_template("base.html")


if __name__ == "__main__":
    app.run()

if (isDateReal(datePrime) == False):
    print("bad date")
    exit()  # precheck for date

addData(str(datePrime), stock1Prime, stock2Prime)
dates.reverse()
createChart(stock1Prime, stock2Prime)

'''


'''from flask import Flask, redirect, url_for, render_template, request
import requests  # needed for API pull
import json  # allows for json manipulation
import numpy as np
import matplotlib.pyplot as plt









###
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

  # add data into arrays


# x = np.arange(1, (len(closes1)+1))
def createChart(stockOne, stockTwo):
    x = np.array(dates)  # stores axes' values from arrays
    y = np.array(closes1)
    z = np.array(closes2)

    plt.title('{sym1} (Green) vs {sym2} (Blue)'.format(
        sym1=stockOne, sym2=stockTwo))
    plt.xlabel("Date from {firstDay} to current day".format(firstDay=dates[0]))
    plt.ylabel('Value of Share ($)')

    ax = plt.gca()

    ax.axes.xaxis.set_ticklabels([])

    plt.plot(x, y,  color='green')
    plt.plot(x, z, color='blue')

    plt.grid(True)

    plt.savefig("chart.png")
    plt.close()

    # plt.show()


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if (request.method == "POST"):
        day = request.form["dt"]

        firstStock = request.form["s1"]

        secondStock = request.form["s2"]

        return redirect(url_for(('datep'), date2=day, stock1=firstStock, stock2=secondStock))

    else:
        return render_template("base.html")


@app.route("/datep/<string:date2>/<string:stock1>/<string:stock2>")
def datep(date2, stock1, stock2):

    if (isDateReal(date2) == False):
        exit()  # precheck for date

    addData(date2, stock1, stock2)
    dates.reverse()
    createChart(stock1, stock2)
    print("plaese work")
    return render_template("stockpage.html")


    # return(dates[0] + str(closes1[0]) + str(closes2[0]))
'''
'''
    x = np.array(dates)  # stores axes' values from arrays
    y = np.array(closes1)
    z = np.array(closes2)
    plt.title('{sym1} (Green) vs {sym2} (Blue)'.format(
        sym1=stock1, sym2=stock2))
    plt.xlabel("Date from {firstDay} to current day".format(firstDay=dates[0]))
    plt.ylabel('Value of Share ($)')
    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([])
    plt.plot(x, y,  color='green')
    plt.plot(x, z, color='blue')
    plt.grid(True)
    plt.savefig("chart.png")
    plt.show()
    '''


'''
if __name__ == "__main__":
    app.run(debug=True)
    '''
