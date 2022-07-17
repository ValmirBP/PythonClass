from emoji import emojize


print("{:=^50}\n".format(emojize(" CHALLENGE 031 :crossed_swords:  ")))

print("Write a Software that calculate the distance in kilometers ans show the ticket price \nconsider U$ 0.50 per KM for 200 KM limit and U$ 0.45 for more\n")

dist = float(input("Type the  distance: "))

if dist <= 200:
    ticket = dist * 0.50
    print("The Total is ${:.2f} " .format(ticket))
else:
    ticket = dist * 0.45
    print("The Total is ${:.2f} " .format(ticket))

print("{:=^50}\n".format(emojize(" CHALLENGE 031 END :2nd_place_medal:  ")))
