from ClassColorsEmojis import *
from emoji import emojize

print ("{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 73 " + Emoji.challenge),Color.reset))

print(f"""\n{Color.cyan}Create a tuple filled with the top 20 of the Brazilian Football Championship
Table, in order of placement. Then show:
a) The top 5 teams.
b) The last 4 placed.
c) Teams in alphabetical order.
d) In what position is the Bahia team.
Please note that the list includes only 20 teams, but the actual Brazilian Football Championship
might have more teams competing. You can extend the list with more team names as needed.
{Color.reset}\n""")

brazilPopTeams = (
    "Flamengo",
    "Palmeiras",
    "Santos",
    "São Paulo FC",
    "Corinthians",
    "Fluminense",
    "Vasco da Gama",
    "Grêmio",
    "Cruzeiro",
    "Internacional",
    "Botafogo",
    "Atlético Mineiro",
    "Bahia",
    "Sport Recife",
    "Vitória",
    "Atlético Paranaense",
    "Coritiba",
    "Goiás",
    "Fortaleza",
    "Ceará"
)
print(f'{Color.greenBold} Top 5 teams {Color.reset}\n')
print(brazilPopTeams[0:5]) # a
print()
print(f'{Color.greenBold}Last 4 teams: {Color.reset}\n')
print(brazilPopTeams[16:]) # b
print()
print(f'{Color.greenBold}Alphabetical order teams {Color.reset}\n')
print(sorted(brazilPopTeams)) # c
print()
print(f'{Color.greenBold}Position of bahia Team {Color.reset}\n')
print(f'Bahia  is in position {brazilPopTeams.index("Bahia")+1} th') # d



print ("\n{}{:=^50}{}".format(Color.redBold,emojize("CHALLENGE 73 END" + Emoji.challenge),Color.reset))
