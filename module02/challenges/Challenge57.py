from emoji import emojize


class color:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightGrey = '\033[37m'
    darkGrey = '\033[90m'
    lightRed = '\033[91m'
    lightGreen = '\033[92m'
    yellow = '\033[93m'
    lightBlue = '\033[94m'
    pink = '\033[95m'
    lightCyan = '\033[96m'
    reset = '\033[0m'

print(color.green," CHALLENGE 57 ".center(50, emojize(":axe:")),color.reset)

print("Develop  a software that read the sex of a pearson, but only accept tha values like M or F, in case if it is wrong ask again until the right value")


sex = input("Type your sex: ") 
while sex not in 'fFmM':
    print("invalid data!!") 
    sex = input("Please Type your sex: ") 
print("Information  stored") 
print("done")