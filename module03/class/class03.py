# test =list ()
# test.append('Guston')
# test.append(40)
# print(test)

# people = list()
# # people.append(test) // makes a link  between relative (test) to parent (people)
# people.append(test[:])
# #  When try to  change  any index of array it will change both positions of array
# test[0] =  'Mary'
# test[1] =  '20'
# # people.append(test)
# people.append(test[:])
# print(people)

guys = [['John',58],['Mary',55],['Alice',30],['Pedro',29]]
# print(guys[0] [0])
# print(guys[2] [1])
# print(guys[3] [1])

for person,age in guys:
    print(f'{person} is {age} years old.')
print()

family = list()
familyInteg = list()
name = ''
age  = 0
majAge = minAge = 0

for person in range(0,3):
    name = input('Name:')
    age = int(input('age:'))
    familyInteg.append(name)
    familyInteg.append(age)
    family.append(familyInteg[:])
    familyInteg.clear()

for name, age in family:
    if age >=21:
        print(f'{name} is {age} is in major age, can buy  weed')
        majAge += 1
    else:
        print(f'{name} is {age} is in not major age, can not buy weed')
        minAge += 1

print(f'This family have {majAge} that can buy weed  and {minAge} that can´t')