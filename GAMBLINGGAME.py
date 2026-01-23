import random
import sys
print('''╔═══════════════════════════════════════╗
║                                       ║
║   ♦ ♣   WELCOME TO SAAD'S   ♥ ♠       ║
║           GAMBLING GAME               ║
║                                       ║
╚═══════════════════════════════════════╝''')
bal = int(input("Enter your starting bal: $"))
if bal ==0:
    print("Good job. You lost before you began.")
    sys.exit(0)
    
guess = int(input("Bet a number between 0 to 5: "))

bid = int(input("Enter the amount of bid: $")) 
while True:
    if bid <= 0 or bid > bal:
        print("bid cant be higher than bal or negative")
        bid = int(input("Enter the amount of bid: $"))
    else:
        break
bal -= bid

a = int(random.uniform(0,6))


if guess == a:
    bid *= 2
    print(f"YOU WON ${bid} LETS GOOOOOOO!!!!!!")
    bal += bid
    print(f"You have ${bal} in ur balance")
else:
    bid = 0
    print(f"HAHAHAHAHSJAHIKSHAIK you lost :( the number was {a}")
    print(f"You got ${bal} (do you think thats enough) ")

again = input("Wanna bid again? (y/n): ")

while True:
    if again == 'y':
        if bal == 0:
            print("Bro seriously? you wanna bid again despite having $0? bruh")
            break
        guess = int(input("Bet a number between 0 to 5: "))

        bid = int(input("Enter the amount of bid: $")) 
        while True:
            if bid <= 0 or bid > bal:
                print("bid cant be higher than bal or negative")
                bid = int(input("Enter the amount of bid: $"))
            else:
                break
        bal -= bid

        a = int(random.uniform(0,6))


        if guess == a:
            bid *= 2
            print(f"YOU WON ${bid} LETS GOOOOOOO!!!!!!")
            bal += bid
            print(f"You have ${bal} in ur balance")
        else:
            bid = 0
            print(f"HAHAHAHAHSJAHIKSHAIK you lost :( the number was {a}")
            print(f"You got ${bal} (do you think thats enough) ")

        again = input("Wanna bid again? (y/n): ")
    else:
        print(f"Good choice, you are left with ${bal}")
        break


















