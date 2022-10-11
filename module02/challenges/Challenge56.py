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

print("{}{:=^50}{}".format(colorDic['greenBold'], emoji.emojize(" CHALLENGE 056 :crossed_swords: "), colorDic['end']))

print("Develop a program that reads the name, age and gender of 4 people. At the end of the program, show: the average age of the group, what is the name of the oldest man and how many women are under 20.")

sumAge = 0
avgAge = 0
biggestAgeMan = 0
oldestMan = ""
totWomen20 = 0

for p in range (1,5):
    
    print("-"*25, f" PEARSON {p} ", "-"*25)
    name = str(input("Type here the name: ")).strip()
    age = int(input("Age: "))
    sex = str(input("sex M/F: ")).strip()
    sumAge += age

    if p == 1 and sex in 'Mm':
        biggestAgeMan = age
        oldestMan = name
    if sex in 'Mm' and age > biggestAgeMan:
        biggestAgeMan = age
        oldestMan = name
    if sex in 'Ff' and age == 20:
        totWomen20 += 1


avgAge = (sumAge / p)
print(f" The average of the ages  of the group is {avgAge}")
print(f" The oldest man is {oldestMan} and his age is {biggestAgeMan} ")
print(f" The total  of women less than 20 is {totWomen20} ")

print("{}{:=^50}{}".format(colorDic['greenBold'], emoji.emojize(" CHALLENGE 056 END :crossed_swords: "), colorDic['end']))