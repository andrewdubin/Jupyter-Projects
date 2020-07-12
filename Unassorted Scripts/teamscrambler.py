import random as rn
names = ["Cam","Andrew","Janaya","Miles","David",
         "Kyle","Spyce","Nick","Travis","Tyler"]
team1 = []
team2 = []
while len(names) != 0:
    name1 = rn.choice(names)
    team1.append(name1)
    names.remove(name1)
    name2 = rn.choice(names)
    team2.append(name2)
    names.remove(name2)
print(team1)
print(team2)
