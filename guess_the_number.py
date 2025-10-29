import random

picked_no = random.randint(1, 100)
tries = 0
max_tries = 8

i = int(input("Enter a number: "))
tries += 1

while i != picked_no and tries < max_tries:
    print("Ha ha! You're stuck in my loop!")
    
    if i < picked_no:
        print("Too small!")
    else:
        print("Too large!")
    
    i = int(input("Enter a number: "))
    tries += 1

# Check why the loop ended
if i == picked_no:
    print(f"You got it! The number was {picked_no}")
    print(f"Well done! You guessed it in {tries} tries.")
else:
    print(f"You failed! Out of trials.")
    print(f"The number was {picked_no}")
