from ClassColorsEmojis import *
from emoji import emojize

print("{}{:=^50}{}".format(Color.redBold, emojize(" CHALLENGE 93 " + Emoji.challenge), Color.reset))

print(f"""\n{Color.cyan}Create a program that reads the name, gender and age of several people, 
      storing each person's data in a dictionary and all dictionaries in a list. 
      At the end, show: A) How many people were registered B) The average age C) 
      A list of women D) A list of people above the average age
{Color.reset}\n""")

# Function to check if the input is a valid integer
def checkInput():
    # Keep asking for input until a valid integer is entered
    while True:
        try:
            # Get the user input and convert it to an integer
            value = int(input(f'{Color.green} Enter the age : {Color.reset}'))
            # Return the integer value
            return value
        except ValueError:
            # Print an error message if the input is not a valid integer
            print(f'{Color.red}  Invalid input! enter the age as a number {Color.reset}')

# Function to check the user's gender
def checkGender():
    # Keep asking for input until the user enters either 'M' or 'F'
    while True:
        gender = input(f'{Color.greenBold}Enter Gender Male [M] Female[F]{Color.reset}').upper()
        if gender == 'M':
            # Return 'male' if the user enters 'M'
            return 'male'
        elif gender == 'F':
            # Return 'female' if the user enters 'F'
            return 'female'
        else:
            # Print an error message if the user enters an invalid option
            print(f'{Color.red} Invalid option! {Color.reset}')

# Function to ask the user if they want to continue
def continueOpt():
    # Print a message asking the user if they want to continue
    print(f'{Color.greenBold}Want to continue? yes[Y] No[N] (Default yes) {Color.reset}')
    # Get the user input and return the first character in uppercase
    flag = input()
    return flag[0].upper()

# Initialize variables
flag = 'Y' # Set the default value of flag to 'Y'
numberOfPeople = 0 # Initialize the number of people to 0
peopleList = [] # Initialize an empty list to store the information of people
femaleList = [] # Initialize an empty list to store the information of female people
aboveEverage = [] # Initialize an empty list to store the information of average above
average = 0 # Initialize the average age to 0

# Keep asking for input until the user wants to stop
while flag != 'N':
    # Get the user input for name
    name = input(f'{Color.greenBold} Enter the name: {Color.reset}')
    # Get the user input for gender and store it in the variable 'gender'
    gender = checkGender()
    # Get the user input for age and store it in the variable 'age'
    age = checkInput()

    # Add the information of the person into a dictionary
    personInfo = {
        'name' : name,
        'gender' : gender,
        'age' : age
    }

    # Increment the number of people
    numberOfPeople += 1
    # Append the dictionary to the list of people
    peopleList.append(personInfo)

    # Ask the user if they want to continue
    flag = continueOpt()

# Calculate the average age
average = sum(person['age'] for person in peopleList) / len(peopleList)

# Separate the female people from the list of people
femaleList = [person for person in peopleList if person['gender'] == 'female']

aboveEverage =[person for person in peopleList if person ['age'] >= average]

# Print the result
print(f'{Color.cyanBold} A) {numberOfPeople} people registered{Color.reset}')
print(f'{Color.cyanBold} B) {numberOfPeople} average of the ages {average} {Color.reset}')
print(f'{Color.cyanBold} C) {numberOfPeople} the weman are :{Color.reset}')

for woman in femaleList:
    print(f'{Color.cyanBold} {numberOfPeople} {name} {Color.reset}')
    
print(f'{Color.cyanBold} D) {numberOfPeople} the peple with above aged are :{Color.reset}')

for people in aboveEverage:
    print(f'{Color.cyanBold} {numberOfPeople} {name} {Color.reset}')


print("\n{}{:=^50}{}".format(Color.redBold, emojize("CHALLENGE 93 END" + Emoji.challenge), Color.reset))