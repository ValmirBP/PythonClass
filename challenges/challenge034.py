from emoji import emojize
# teste

print("{:=^50}\n".format(emojize(" CHALLENGE 034 :crossed_swords:  ")))

print("Write a Software that calculate the salary increase of worker \nconsider: \nsalary bigger than U$ 1250,00 increase of 10% \nbottom or equal 15% \n")

salary = float(input("Type te salary of the worker: "))

if salary <= 1250:
    increase = salary * 1.15
    print(" your salary was U$ {:.2f}, but incraesing it on '15%' is U$ {:.2f}".format(salary,increase))
    
else:
    increase = salary * 1.10
    print(" your salary was U$ {:.2f}, but incraesing it on '10%' is U$ {:.2f}".format(salary,increase))

print("{:=^50}\n".format(emojize(" CHALLENGE 034 END :2nd_place_medal:  ")))
