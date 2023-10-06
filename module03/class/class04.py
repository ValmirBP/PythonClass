# dictionaries

data = dict()
#  or
data1 = {}
#  they are the same  thing
data1= {'name': 'pedro'
        ,'age' : 25}

print()

print(data1['name'])
print(data1['age'])

print()
data1['sex'] = 'm'
print (data1)

print()

del data1['age']
print (data1)

movies = {}
movies['title'] = 'Star Wars'
movies['year'] = 1977
movies['Director'] = 'George Lucas'

print()

print(movies.values()) #Show the values of the  dict
print(movies.keys()) #Show the Keys of the  dict

print()

for k,v in movies.items():# all items from the dict
    print(f'the {k} is {v}')

print()

people ={'name': 'Valmir','age': 29,'sex':'you!'}
# print(people[0]) # error
print()
print(f'{people["name"]}' ) # error

print()
print(people.keys())

print()

print(people.values())
print()

print(people.values())
print()


for k in people.keys():
    print(k)

print()

for v in people.values():
    print(v)
print()

for k,v  in people.items():
        if k == 'name':
            print(f'what {v} loves?')
            print(f'{v} loves', end='')
        if k == 'sex':
            print(f' {k}')
            print(f'Yes {v}')

brazil = list()
state1 = {'uf': 'Rio de  Janeiro', 'slang' :'RJ'}
state2 = {'uf': 'Sao Paulo', 'slang' :'SP'}

brazil.append(state1)
brazil.append(state2)

print(brazil)
print(state1)
print(state2)
print(brazil[0]['uf'])
print(brazil[1]['uf'])


print()

state = dict()
brazil = list()

for c in range(0, 3):
    state['uf'] = str(input('Federal unit: '))
    state['slang'] = str(input('state slang: '))
    brazil.append(state.copy())

for e in brazil:
    for v in e.values():
        print(v, end=' ')
    print()
