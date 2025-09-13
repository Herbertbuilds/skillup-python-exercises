user = int(input("Enter a number: "))
name = input("Enter your name: ")


#while loop to print a message based on user input
while user < 7:
    message = "Hello,  {} How are you today?".format(name)
    print(message)
    user = user + 1
    if user == 7:
        break
else:
    print("""Please enter a number less than 7. 
          Exiting the loop.""")

    

#for loop to print each element in a tuple
i = (1,7,5)

for x in i:
    print(x)


#Nested loops
x= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in x:
    for j in i:
        print(j, end=' ')

sum = 0
for i in range(0, 21,):
    if i % 2 == 0:
        sum = sum + i
print(sum, end  =' ')



num = int(input("Enter ur number: "))
for i in range(1, num +1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()



#calculate the length of a list using a while loop without using len()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = 0
i = 0
try:
    while x[i]:
       length += 1
       i+= 1
except IndexError:
    print(length)



#1
#22
#333
#4444
#55555
num = int(input("Enter a number: "))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(i, end='')
        j += 1
    i += 1
    print()    


#guess the number game
import random
nump = random.randint(1000,9999)
n = int(input("Guess a 4 digit number: "))

while n != 10:
    num = nump
    core = 0
    while num % 10: 
        numc = num % 10
        nc = n % 10
        num = num // 10
        n = n // 10
        if numc == nc:
            core += 1
    if core == 4:
        print("You guessed the number correctly!")
        break
    else:
        print("%d digits are correct" % core) 
        n = int(input("Guess again: "))       
else :
    print("You have exited the game.")
