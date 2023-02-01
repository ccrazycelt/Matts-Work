
"""
    Description of program: A game where you have to guess three numbers in there designated positions
    Filename: PICOfermiBAGEL.py
    Author: Matt Waeldner
    Date: Jan 8th, 2023
    Course: 1352
    Assignment: roject 1 - A Guessing Game (called Pico Fermi Bagels)
    Collaborators: Alex
    Internet Source: DU Guest Wifi
"""
'''
import random
#The target values
target=[]
#generating 3 random numbers
#I need to make them 3 differnt numbers
while len(target) != 3:
    for i in range (15):
        first = str(random.randint(0, 9))
        second = str(random.randint(0, 9))
        third = str(random.randint(0, 9))
        target.append(first)
        if first != second:
            target.append(second)
        if third != second and third != first:
            target.append(third)
        if first == second or second == third or first == third:
            target.clear() 

#Setting up guess list so I can use it in the while loop
guess_list = []
attempts = 0
#While not fermi, fermi, fermi
while guess_list != target:
    attempts +=1
#Resets the guess list to zero so each attempt does not add on to one another
    guess_list = []
#the 3 numbers the user gives
    guess = str(input("Give me three numbers, you are in the pico fermi bagel gauntlet!: "))
#converting the numbers in the guess to seperate values in the list
    for i in guess:
        guess_list.append(i)
    #MAKING SURE THERE IS NO repeating didgets
    while len(guess_list) != len(set(guess_list)):
        attempts += 1
        guess_list = []
        guess = str(input("Figure it out bub, no repeating didgets!: "))
        for i in guess:
            guess_list.append(i)
        
#Checking if the number and the guess are equal and in the same spot(fermi)
    for i in range(len(target)):
        if target[i] == guess[i]:
            print("fermi")
#checks if the guess is in the target list after it checks
#the guess with the target list with the matching index and value
        elif (guess[i] == target[0]) or (guess[i] == target[1]) or (guess[i] == target[2]):
            print("pico")
#else: the guess value is not in the target list
        else:
            print("bagel")

print(f"Congrats, hurdy gurdy fermi in {attempts} trys!")

'''