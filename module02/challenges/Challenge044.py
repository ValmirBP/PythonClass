from sys import float_repr_style
from emoji import emojize


colorDic = {
    'bold'          : '\033[1m'
    ,'redBold'          : '\033[31m'
    ,'green'        : '\033[32m'
    ,'yellow'       : '\033[33m'
    ,'blue'         : '\033[34m'
    ,'redBold'      : '\033[1;31m'
    ,'greenBold'    : '\033[1;32m'
    ,'yellowBold'   : '\033[1;33m'
    ,'blueBold'     : '\033[1;34m'
    ,'end'          : '\033[m'
}

print ("{}{:=^50}{}".format(colorDic['greenBold'], emojize("CHALLENGE 44 :crossed_swords:"), colorDic["end"]))

print ("write software that calculate a value of a product considering its normal price and payment condition \nfull:money|check 10% \nfull discount ticket 5% \npart payment 3 times or more on credit card 20%\n")

total = float(input("{}Type  here  the total: {}".format(colorDic['blue'], colorDic['end'])).strip())
payMethod = str(input("{}Now choose the payment M: money | check, DT: Discount Ticket, CC: Credit Card: {}".format(colorDic['redBold'],colorDic['end'])).strip().upper())

if payMethod == "M":
    total = total - (10/100 * total) 
    print("the total is: {} ${:.2f} {}".format(colorDic['greenBold'], total, colorDic['end']))

elif payMethod == "DT":
    total = total - (5/100 * total) 
    print("the total is: {} ${:.2f} {}".format(colorDic['greenBold'], total, colorDic['end']))

elif payMethod == "CC":
    total = total - (20/100 * total) 
    print("the total is: {} ${:.2f} {}".format(colorDic['greenBold'], total, colorDic['end']))

else:
    print ("{}invalid condition{}".format(colorDic['redBold'], colorDic['end']))

print ("{}{:=^50}{}".format(colorDic['greenBold'], emojize("CHALLENGE 44 END:crossed_swords:"), colorDic["end"]))
