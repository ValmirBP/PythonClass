# Tuple  are imutable

lunch =  ['hamburger', 'juice','pizza','pudim']

# lunch =  ['hamburger', 'juice','pizza','pudim']
# lunch =  [    '0',        '1',   '2',   '3']

print (lunch)
del lunch[3] # removes index  3  == pudim
print (lunch)

lunch =  ['hamburger', 'juice','pizza','pudim']
lunch.pop(3)# removes index  3  == pudim
print (lunch)

lunch =  ['hamburger', 'juice','pizza','pudim']
lunch.remove('pizza') # removes the index with the value  entered
print (lunch)

lunch =  ['hamburger', 'juice','pizza','pudim']
lunch.pop()# removes last index == pudim
print (lunch)


if 'pizza' in lunch:
    lunch.remove('pizza')

values  = list(range(4,11)) # ordenated list
print (values)

values = [8,2,5,4,9,3,0] # unordenated list
print (values)

values.sort() #order the list
print (values)

values.sort(reverse= True) #order the list in reverse
print (values)


print (f'lengh of the array{len(values)}') #lenght of the value


values.pop() # delete the last  element  of list
print(values)

values.insert(2,0) # insert on index 2 number 0
print(values)

values.insert(2,2) #
print(values)
# values.remove(2) # remove the first index that it  shows
print(values)

values = [9, 8, 2, 0, 5, 4, 3, 2]
values2 = []
for num in values:
    if num != 2:
        values2.append(num)
print(values)
print(values2)

for ind,value in enumerate(values):
    print(f'on index {ind} there is {value}')

a = [9, 8, 0, 5, 4, 3]
# b = a # creatates a relation  with the parent
# b = a[:] # make a copy  of all elements
b = a.copy() # make a copy  of all elements
b[2] = 8
print(a)
print(b)