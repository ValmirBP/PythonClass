from emoji import emojize


colorDic = {
    'bold'          : '\033[1m'
    ,'red'          : '\033[31m'
    ,'green'        : '\033[32m'
    ,'yellow'       : '\033[33m'
    ,'blue'         : '\033[34m'
    ,'redBold'      : '\033[1;31m'
    ,'greenBold'    : '\033[1;32m'
    ,'yellowBold'   : '\033[1;33m'
    ,'blueBold'     : '\033[1;34m'
    ,'end'          : '\033[m'
}

emojiLst = {
    'cool'           : ':smiling_face_with_sunglasses:'
    ,'medalGold'     : ':1st_place_medal:'
    ,'medalSilver '  : ':2nd_place_medal:'
    ,'medal3rd'      : ':3th_place_medal:'
    ,'challenge'     : ':crossed_swords:'
    ,'notSoSincere'  : ':grinning_face_with_sweat:'
}

print("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLENGE 036 " + emojiLst['challenge']), colorDic['end']))
 
print("Write a Software that ask for the user his wage, a value of a house and the payment schedule \nCalculate the value of the mensal payment that do not  exceed 30 percent of his wage, due to the forbid the payment")

wage = float(input("type the wage: "))
ValueHouse = float(input("type the value of the house: "))
period = int(input("type the period of payment in months: "))

percentageWage = (ValueHouse/period)*100/wage
idealValue = (ValueHouse*100)/(wage*30)

if percentageWage > 30:

    print("\nSorry! Unfortunately is not possible to approve your finance due to is is over  than  30¢ of  your wage\n")
    print("But  Is possible to help you  to  buy your house if you invest {:.2f} will be possible to approve \nand get {} months to pay \nor {} year".format(idealValue, (ValueHouse/idealValue), (ValueHouse/idealValue)/12 ))

    answer= str(input("Do you want accept the deal? y/n "))
    
    if answer == "y" or answer == "Y":
        print("\nGood contact  any  consulter to sign the proposal")
    else:
        print("\nok! see you next time")

else:
        print("\nGood contact  any  consulter to sign the proposal")

print("{} {:=^50} {}".format(colorDic['greenBold'], emojize("CHALLENGE 036 END " + emojiLst['challenge']), colorDic['end']))