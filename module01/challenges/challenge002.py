import datetime
print ('{:=^50}'.format(' CHALENGE 02 '))

print('whrite a program to recieve the year, month and the day of the birth, and show on screen the whole information and calculate the age of the user\n')

y = int(input ('Type the year you´ve born '))
m = input ('Type the month you´ve born ')
d = input ('Type the day you´ve born ')
n = input('Type your name ? ')
a = datetime.date.today().year - y

if d == 1 :
   dm = 'st'
    
elif d == 2 :
   dm = 'nd'
    
else :
   dm = 'th'

   print(' Hi, {}! \n Your Birth day is {}-{}-{}{}\n Your age is {}'.format(n,y,m,d,dm,a) )
    
# print ('Hi ' + n + '\n you´ve born in ' + m + ' '+ d + dm + ' of ',  y )
# print ('And your age is ' , a )
ans = input ('Does it correct? ')

if ans == 'y' or ans == 'Y' :
    print ('Ok Thank you! \n Bye!')

print ('{:=^50}'.format(' CHALENGE 02 END'))