# Tuple  are imutable

lunch =  ('hamburger', 'juice','pizza','pudim')

# lunch =  ('hamburger', 'juice','pizza','pudim')
# lunch =  (    '0',        '1',   '2',   '3')

print(lunch) #('hamburger', 'juice','pizza','pudim')
print(lunch[1]) # Juice
print(lunch[3]) # pudim
print(lunch[-4]) # 4 -4 = 0  hamburger
print(lunch[1:3]) # from 1 to 3  where last not count (juice, pizza)
print(lunch[2:])  # from 2 to end  ('pizza' ,'pudim')
print(lunch[:2])  # from beginning to 2 where dont count last ('hamburger', 'juice')

# lunch[1] = 'pop'
# print (lunch[1]) # error

print('*' * 20)

for food  in lunch: # no  index
    print (f'I´ll eat {food}')
print(f'I´m full!')

print('*' * 20)

for pos, food  in enumerate(lunch): # With  index
    print (f'I´ll eat {food} on {pos}')
print(f'I´m full!')

print('*' * 20)

for food2  in range (0,len(lunch)):
    print (f'I´ll eat {lunch[food2]} on {food2}')
print(f'I´m full!')

print('*' * 20)
# sorted
lunch =  ('pizza','pudim', 'hamburger', 'juice')
print (lunch)
print (f'Sorted {sorted (lunch)}')

print('*' * 20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #will join  tuples

print(c) # (2, 5, 4, 5, 8, 1, 2)
print(len(c)) # 7

print('*' * 20)

print(c.count(5)) # show how many times it shows #2
print(c.count(9)) # show how many times it shows #0

print('*' * 20)

c = b + a
print(c) # (2, 5, 4, 5, 8, 1, 2)
print(c.index(8)) # show first index show #4
print(c.index(5)) # show first index show #1
print(c.index(2)) # show first index show #0

print('*' * 20)

person = ('Valmir', 29, 'M', 100)
del(person) # del the tuple from memory
print(person) # error