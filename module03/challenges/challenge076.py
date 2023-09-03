from ClassColorsEmojis import *
from emoji import emojize
from tabulate import tabulate

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 76 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a program that has a single tuple with product names and their
respective prices, in sequence. At the end, show a price list, organizing the data in tabular form.
{Color.reset}\n""")

def AskContinue():
    while True:
        ask =  input(f'{Color.greenBold}\n Do you want to  continue? [Y]Yes [N]No {Color.reset}').strip().upper()
        if ask[0] == 'N':
            return False
        elif ask[0] == 'Y':
            return True
        else:
            print(f'{Color.redBold}\ninvalid input, use [Y]Yes [N]No{Color.reset}')

def checkValidPrice(prodName):
    while True:
        try:
            prodPrice = float(input(f'{Color.blueBold} Enter {prodName} price:  {Color.reset}'))
            return prodPrice
        except ValueError:
            print(f'{Color.redBold}\nInvalid value for product {prodName} {Color.reset}')

products = ()
while True:
    prodName = input(f'{Color.blueBold} Enter product name: {Color.reset}')
    prodPrice = checkValidPrice(prodName)
    products += (prodName,prodPrice,)
    answer = AskContinue()
    if not  answer:
        break

data = [products]
headers = ['product name','product price']
table = tabulate(data,headers=headers,tablefmt='grid')
print(table)

print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 76 END" + Emoji.challenge),Color.reset))
