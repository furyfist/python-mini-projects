import random

ans = input("Roll the dice? (y/n): ")

if ans == "n" or ans == "N":
    print("Thanks for Playing!")
elif ans =="y" or ans =="Y":
    response = random.randint(1,6)
    response2 = random.randint(1,6)
    print(f"you rolled : {response} and {response2}")
else:
    print("Invalid Choice")
    