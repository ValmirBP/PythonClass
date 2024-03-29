from random import randint
from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 70 " + Emoji.challenge),Color.reset))

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
        price = float(input(f'{Color.greenBold}Enter the price of the product: {Color.reset}'))
        if price < 0 :
            price(f'{Color.red}Price can not be negative{Color.reset}')
        else:
            return price
      except ValueError:
            print(f'{Color.red}invalid input for price {Color.reset}')

def askContinue():
    while True:
        answer = input(f'{Color.greenBold}\n Do you want to continue? [Y] Yes [N] No {Color.reset}').strip().upper()
        if answer == 'Y':
            print(f'{Color.greenBold}OK!{Color.reset}')
            print()
            return True
        elif answer == 'N':
            print()
            return False
        else:
            print(f'{Color.red}Invalid input {Color.reset}')

def CheapPriceCk():
    global cheapestProd

    if cheapestProd == 0:
        cheapestProd =  price
    elif price < cheapestProd:
        cheapestProd =  price
        return cheapestProd


while True:
    product =  input(f'{Color.greenBold}Enter the name of the product: {Color.reset}').strip()
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

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 70 END" + Emoji.challenge),Color.reset))
