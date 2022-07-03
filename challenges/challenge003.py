print('{:=^50}'.format(' CHALLENGE 03 '))

print('White a program that ask  for the user  to  Type two numbers  and show on screen the result of each aritimetics')

n1 = int(input ('1st number '))
n2 = int(input ('2nd number '))
s = n1+n2
d = n1/n2
m = n1*n2
p = n1**n2
divInc = n1//n2


print('The Sum between {} and {} = {} \n'.format(n1,n2,s))
print('The Division between {} and {} = {:.3f} \n'.format(n1,n2,d))
print('The Multiplication between {} and {} = {}\n'.format(n1,n2,m))
print('The Emowerment between {} and {} = {}\n'.format(n1,n2,p))
print('The intire division between {} and {} = {}\n'.format(n1,n2,divInc))

if n1 > n2 :
   sub = n1-n2
   print ('the subtraction between {} and {} = {}\n '.format(n1,n2,sub))
    
else :
   sub = n2-n1
   print ('the subtraction between {} and {} = {}\n'.format(n2,n1,sub))


print('{:=^50}'.format(' CHALLENGE 03 END'))