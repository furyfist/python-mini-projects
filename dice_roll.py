#LOOP
    # always map out whats you going to do
    # Ask: roll a dice?
    # if user enters y -> generates two random numbers
    # if user entes n -> print thank you message
    # else -> Invalid Choice

# Optimal Enhancements 
#   1. specify how many dice user wants to roll.
#   2. Feature Keeps track of how many time the user has rolled the dice during the session.

import random

cnt = int(input("How many times you wants to roll the dice? : "))
total = 0
while cnt > 0:
    print(f"Total times dice rolled : {total} ")
    
    cnt-=1
    ans = input("Roll the dice? (y/n): ").lower()
    if ans == "n":
        print("Thanks for Playing!")
        break
    elif ans =="y":
        total+=1
        response = random.randint(1,6)
        response2 = random.randint(1,6)
        print(f"({response},{response2})")
    else:
        print("Invalid Choice")
