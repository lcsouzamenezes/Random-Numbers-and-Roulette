from random import randint

r = 18.5 #randint(0,36)
x = randint(0,36)
y = randint(0,36)

zplus = 0
zminus = 0

count = 0
turns = 100

while count < turns:
    f = open("output.txt", "a")
    if x > r and y < x and y != 0:
        f.write("+ " + str(x) + "  "+ str(y) +"\n") 
        zplus += 1
    elif x > r and y > x:
        f.write("- " + str(x) + "  "+ str(y) +"\n")
        zminus += 1
    elif x < r and y > x:
        f.write("+ " + str(x) + "  "+ str(y) +"\n")
        zplus += 1
    elif x < r and y < x:
        f.write("- " + str(x) + "  "+ str(y) +"\n")
        zminus += 1
    elif y == 0:
        f.write("- " + str(x) + "  "+ str(y) +"\n")
        zminus += 1
    else: 
        f.write("- " + str(x) + "  "+ str(y) +"\n")
        zminus += 1
    x = y
    y = randint(0,36)
    count += 1

print('Turns played: ' + str(count))
print(str(zplus) +'/' + str(turns) + ' won')
print(str(zminus)  +'/' + str(turns) + ' lost')

input()