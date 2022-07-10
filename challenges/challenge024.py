from emoji import emojize

print("{:=^50}\n".format(emojize(" CHALLENGE 024 :crossed_swords:  ")))

print ("write a software that read from input the name of a city and chek if it starts whith 'SAINT' word\n")

city = input('Tipe the name of your city: ')
city = city.strip()
city = city.capitalize()
print("\nDoes your city  starts with Saint? {}".format(city.startswith("Saint")))

print("\n{:=^50}".format(" OTHER WAY TO RESOLVE IT "))

divCity = city.split()
result = divCity[0] == "Saint"

print("Does your city  starts with Saint? {}\n".format(result))

print("{:=^50}".format(emojize(" CHALLENGE 024 :2nd_place_medal:  ")))