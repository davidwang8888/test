#!/usr/bin/env python
# -*- coding: utf-8 -*-


items = ['PS4', 'Switch', 'Xbox']
prices = [100, 90, 120]
buy_items = []

print('We have', end=' ')
print(*items, sep=', ', end='.\n')

# print items and prices
for i in range(3):
    print(items[i]+': ', '$', prices[i])
print()


money = int(input('How much money do you have? '))

while True:
    print()
    buy_item = input("What do you want to buy? (or bye) ").strip()

    if buy_item.lower() == 'bye':
        break
    elif buy_item in items:
        index = items.index(buy_item)
        price = prices[index]
        buy_item = '"' + items[index] + '"'
    else:
        print('-'*30)
        print("I don't know what you are talking about. Please try again.")
        continue

    amount = int(input('How many '+buy_item+' do you want to buy? '))

    if money < price * amount:
        print('-'*30)
        print("Sorry, you don't have enough money. Please try again.")
        continue
    else:
        buy_items.append((buy_item, price, amount))

    print('-'*30)
    print('You spend', price * amount, 'dollars to buy', amount, buy_item+'.')

    money -= price * amount
    print('You still have', money, 'dollars left.')

# bonus
total = 0
print('-'*30)
print()
print('You bought:')
for item, price, amount in buy_items:
    cost = price * amount
    print(item, 'x', amount, '=', cost)
    total += cost

print('-'*30)
print('Total  $', total)
print('You still have', money, 'dollars left.')
