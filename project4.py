import random

hidden_number = random.randint(0,1000)

#print(hidden_number)

#number es lachose
#the repeated lines are 10-17 and they get repeated 15 times unless they get it correct then they quit.
for i in range(15) :      
    number1 = int(input("Guess a number between  0-1000"))
    if number1 == hidden_number:
        print ("OH MY GOD YOU GOT THE NUMBER IM SO PROUD OF YOU!!!!!!!!!!!")
        quit()
    elif hidden_number > number1:
        print ("Wrong, the number is higher than that loser, jk your not a loser, your goated")
    elif hidden_number < number1:
        print ("Wrong, the number is less than that loser, jk your not a loser your goated")
print("You lose loser")