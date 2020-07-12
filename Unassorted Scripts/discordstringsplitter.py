start = "Cyberpunk 2077? Well what happened to "
num = 1
while num < 2077:
    start += "Cyberpunk " + str(num) + " and "
    num += 1

def discord(string):
    x = 0
    a = 1999
    not_done = 1
    while not_done == 1:
        if(a>len(string)):
            a=len(string)
            not_done = 0
        print(string[x:a])
        print("\n")
        x = x + 2000
        a = a + 2000

discord(start)
