print("{:=^50}".format(" CALLENGE 015 "))

print("write a program that read from the user the days of a car rental and  how much kilometers it has been riden as well  show on the screen the total cost of the  rent  consider the  that car category is costs U$ 60.00 per day  and U$ 0.15 per Km")

days= int(input("How much days of the  rent: "))
km= int(input("How much Kilometers riden:  "))
rent = (days*60)+(km*0.15)
print("The Total cost of  the rent is U${:.2f}".format(rent))

print("{:=^50}".format(" CHALLENGE  015 END "))