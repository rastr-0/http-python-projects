import requests
import matplotlib.pyplot as plt
import json
import time


def main():
    dynamic_of_buying_euro = ({})
    user_input = 'start'
    while True:
        url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
        print('please, input date: ')
        # 1.12.2018 as example
        date = input()
        if date == 'stop':
            break
        r = requests.get(url + date)
        data = json.loads(r.text)
        for i in data['exchangeRate']:
            if len(i) > 3:
                if i['currency'] == 'EUR':
                    dynamic_of_buying_euro[date] = i['purchaseRate']
    values = []
    for key, value in dynamic_of_buying_euro.items():
        print(key, value)
        values.append(value)
    plt.plot(values)
    plt.ylabel('dynamic of buying euro by dates')
    plt.show()


if __name__ == '__main__':
    main()
