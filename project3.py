roblox = 0
fortnite = 0
siege = 0
minecraft = 0
print ("Answer these question with yes or no answers")
input()
answer1 = input ("Are you smart?")
if answer1 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    siege += 1
    minecraft += 1
elif answer1 == "no" or "No" or "NO" or "nO" or " No" or " nO" or " no" or " NO":
    fortnite += 1
    roblox += 1
answer2 = input ("Are you a good listener")
if answer2 == "no" or "No" or "NO" or "nO" or " No" or " nO" or " no" or " NO":
    siege -= 1
    roblox +=1
    fortnite += 1
elif answer2 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    siege +=1
answer3 = input("Are you strong-willed?")
if answer3 == "no" or "No" or "NO" or "nO" or " No" or " nO" or " no" or " NO":
    siege -= 1
elif answer3 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    siege += 1
answer4 = input ("Are you creative?")
if answer4 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    minecraft += 1
answer5 = input("Do you play videogames to relax?")
if answer5 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    minecraft += 2
    siege -= 1
    roblox += 1
elif answer5 == "no" or "No" or "NO" or "nO" or " No" or " nO" or " no" or " NO":
    siege += 1
answer6 = input("Do you play videogames on mobile?")
if answer6 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    minecraft += 1
    siege -= 1
    roblox += 1
elif answer6 == "sometimes":
    print ("cool")
answer7 = input("Are you good at videogames")
if answer7 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    siege += 1
    minecraft += 1
elif answer7 == "no":
    fortnite += 1
    roblox += 1
answer8 = input ("Do you like variety in videogames?")
if answer8 == "yes" or "Yes" or "YES" or "YEs" or " yes" or " Yes" or " YEs" or "YES":
    minecraft += 1
    roblox += 2
    fortnite += 0.5
elif answer8 == "no" or "No" or "NO" or "nO" or " No" or " nO" or " no" or " NO":
    siege += 1
#end of quiz
print (f"You're videogame compatibility is {siege} with Rainbow Six Siege, {roblox} with Roblox, {minecraft} with Minecraft, and {fortnite} with Fortnite")
#siege ending
if siege > roblox and siege > minecraft and siege > fortnite:
    print("Siege is the best game for you")
#roblox ending
elif roblox > siege and roblox > minecraft and roblox > fortnite:
    print ("Roblox is the best game for you")
#minecraft ending
elif minecraft > siege and minecraft > roblox and minecraft > fortnite:
    print("minecraft is the best game for you")
#fortnite ending
elif fortnite > roblox and fortnite > siege and fortnite > minecraft:
    print("fortnite is the best game for you")