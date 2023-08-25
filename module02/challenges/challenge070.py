from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 68 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that reads the name and price of various products.
The program should ask whether the user is going to continue or not. At the end, show:

A) what is the total amount spent on the purchase.
B) how many products cost more than R$1000.
C) what is the name of the cheapest product.
{Color.reset}\n""")

products = []
prices =[]
cheapestProd = 0

def validPriceTag():
    while True:
      try:
        price = float(input(f'Enter the price of the product: '))
        if price < 0 :
            price(f'Price can not be  negative')
        else:
            return price
      except ValueError:
            print(f'invalid input for price`')

def askContinue():
    while True:
        answer = input('Do you want to continue? [Y] Yes [N] No ').strip().upper()
        if answer == 'Y':
            print('OK!!')
            return True
        elif answer == 'N':
            return False
        else:
            print('Invalid input')

def CheapPriceCk():
    global cheapestProd

    if cheapestProd == 0:
        cheapestProd =  price
    elif price < cheapestProd:
        cheapestProd =  price
        return cheapestProd


while True:
    product =  input('Enter the name of the product: ').strip()
    price = validPriceTag()
    products.append(product)
    cheap = CheapPriceCk ()
    prices.append(price)
    totalSpend = sum(prices)
    if not askContinue():
        break

for i,j in zip(products,prices):
    if j > 1000:
        print (f'{Color.yellowBold} prod: {i} -------- $ {j:.2f} M Expensive{Color.reset}')
    elif j == cheapestProd:
        print (f'{Color.yellowBold} prod: {i} -------- $ {j:.2f} Cheapest {Color.reset}')
    else:
        print (f'{Color.yellow} prod: {i} -------- $ {j:.2f} {Color.reset}')

print (f'{Color.yellowBold}Total $ {totalSpend} {Color.reset}')

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 68 END" + Emoji.challenge),Color.reset))
