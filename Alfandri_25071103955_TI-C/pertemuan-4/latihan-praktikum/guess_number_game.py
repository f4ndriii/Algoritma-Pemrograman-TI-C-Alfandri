import random

# Generate angka acak dari 1 sampai 100
random_number = random.randint(1, 100)

def guess():
    return int(input("Guess the number (1-100): "))

health_point = 7

print("=== Guess The Number Game ===")
print("You have 7 chances!\n")

while health_point > 0:
    try:
        guess_number = guess()

    except ValueError:
        print("Error: Please enter a valid number!\n")
        continue

    else:
        if guess_number == random_number:
            print("Cihuyyy! You guessed it right!")
            break

        health_point -= 1

        if health_point > 0:
            if guess_number > random_number:
                print("Lower\n")
            else:
                print("Higher\n")
        else:
            print("Nice Try!")
            print("The correct number was:", random_number)

print("\nGame Over. Thank you for playing!")