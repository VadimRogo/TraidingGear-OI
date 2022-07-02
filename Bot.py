from itertools import count
import json
from ast import Num
import json, time
from statistics import quantiles
from typing import Counter
import pip._vendor.requests  as requests
import numpy as np
import matplotlib.pyplot as plt
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
prices = []
times = int(input())
money = 1000
Counter = 0
JsonTikets= []
moneys = []
Countered = []
class Tiket:
    count = 0
    def __init__(self, num, quantity, price, time, sold):
        self.Counter = Counter
        self.quantity = quantity
        self.price = price
        self.time = time
        self.sold = sold
        # print('We but {} by {} at {}'.format(self.quantity, self.price, self.time))

    def MakeTiket(self):
        NewTiket = json.dumps({'Num': self.num, 'Quantity': self.quantity, 'Price': price, 'Time': time, 'sold': sold})



def BuyingProcess(price):
    global money
    TwentyPrecent = money / 100 * 20
    money -= TwentyPrecent
    quantity = round((TwentyPrecent) / float(price), 3)
    WTime = time.strftime('%X %x')
    sold = False
    print("We BUY in {}".format(price))
    T1 = Tiket(Counter, quantity, price, WTime, sold)
    JsonTiket = {"Counter": T1.Counter, "Price": T1.price,\
          "Time": T1.time, "quantity": T1.quantity, "SOLD": T1.sold, }
    JsonTikets.append(JsonTiket)

def SellingProcess(price):
    global money
    for Tiket in JsonTikets:
        if Tiket['SOLD'] == False:
            print('We SOLD some BTC')
            money += Tiket['quantity'] * price
            Tiket['SOLD'] = True
        else:
            print('We don"t have something for SELL')

def CentreWallue(prices):
    if max(prices) - min(prices) > max(prices) * 0.05:
        prices = np.array(prices)
        prices += max(prices) * 0.05
        print("Input was centered")

def MakeGraphBTC(prices, counter):
    x = prices
    y = counter

    plt.plot(y, x)
    plt.xlabel('Price')
    plt.ylabel('Counter')
    plt.show()
    
def MakeGraphMoneyBag(moneys, counter):
    x = moneys
    y = counter

    plt.plot(y, x)
    plt.xlabel('Money')
    plt.ylabel('Counter')
    plt.show()

for i in range(times):
    Countered.append(i)
    moneys.append(money)
    data = requests.get(key)
    data = data.json()
    price = round(float(data['price']), 3)
    prices.append(price)
    if price <= max(prices):
        Counter += 1
        BuyingProcess(price)
    elif price >= min(prices):
        SellingProcess(price)
    print(price)
    # CentreWallue(prices)
    print(money)
    time.sleep(1)
print(len(moneys), len(Countered), len(prices))

MakeGraphBTC(prices, Countered)
MakeGraphMoneyBag(moneys, Countered)
print(json.dumps(JsonTikets, sort_keys=False, indent=4))
print(Counter)
