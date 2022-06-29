from calendar import monthcalendar
import json
import pip._vendor.requests  as requests
import re, time
import matplotlib.pyplot as plt
# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
# requesting data from url
data = requests.get(key)  
data = data.json()
prices = []
prices.append(float(data['price']))
counter = [0]

print(float(data['price']))

#Простая функция для получения графика через библиотеку Matplotlib
for i in range (1, 30):
    data = requests.get(key)
    data = data.json()
    price = (float(data['price']))
    prices.append(float(price))    
    counter.append(float(i))
    counter.append(i)
    print(price)
    time.sleep(1)

#Имитация кошелька
MoneyBag = 100 * prices[len(prices)-1] / prices[0]
print(MoneyBag)


#Вызов графика в графическом интерфесе
plt.plot(counter, prices, label = 'line 1')
plt.xlabel('Price')
plt.ylabel('Times')
plt.title('BTSUSD')
plt.show()




# print(data['price'])

# print(f"{data['symbol']} price is {data['price']}")