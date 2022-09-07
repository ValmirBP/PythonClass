import emoji

colorDic ={
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

print("{}{:=^50}{}".format(colorDic['greenBold'], emoji.emojize("CHALLENGE 056 :crossed_swords:"), colorDic['end']))

print("Develop a program that reads the name, age and gender of 4 people. At the end of the program, show: the average age of the group, what is the name of the oldest man and how many women are under 20.")

sumAge = 0
avgAge = 0
for i in range (1,3):
    print("-"*25 , " PEARSON {} ".format(i) , "-"*25 )
    name = str(input("Type here the name: "))
    age = int(input("Age: "))
    sex = str(input("sex M/F: ")).upper()
    sumAge += age
avgAge = (sumAge / 4")

print("{} {}".format(sumAge,avgAge))


    


print("{}{:=^50}{}".format(colorDic['greenBold'], emoji.emojize("CHALLENGE 056 END :crossed_swords:"), colorDic['end']))