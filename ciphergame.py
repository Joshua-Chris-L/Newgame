########### Choose Grade program ########
""" 
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Harmonics": 95,
    "Draco": 75,
    "Neville": 60
}

for key in student_scores:
    score = student_scores[key]
    if score > 91:
        print("Grade = 'Outstanding' ")
    elif score > 81 and score < 90:
        print("Grade= 'Exceeds expectation'")
    elif score > 71 and score < 80:
        print("Grade = 'Acceptable' ")
    else:
        print("Grade= 'Fail'")
"""

#### Calculator program.
"""  
first_num = int(input("Enter your first number: "))
operation = input("Print an operation  '+', '*', '-', '/': ")
last_num = int(input("Enter your last number: "))

def add( first_num, last_num ):
    return (first_num + last_num)

def multiply( first_num, last_num ):
    return (first_num*last_num)

def subtract( first_num, last_num ):
    return (first_num - last_num)

def divide( first_num, last_num ):
    return (first_num/last_num)

if operation == "+":
    print(add(first_num, last_num))
elif operation == "*":
     print(multiply(first_num, last_num))
elif operation == "-":
    print(subtract( first_num, last_num ))
else:
    print(divide( first_num, last_num ))

"""
##### Black Jack  Game 

""" 
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10]
your_cards = random.sample(cards, 2)
computer_guess = random.sample(cards, 2)
#print(computer_guess)

sum_c = sum(computer_guess)
sum_y = sum(your_cards)

print(f"Your card is {your_cards}, current_score:{sum(your_cards)}")
print(f"Computer card is {computer_guess[0]}")
cont_game = input("Do you want to make another guess 'y' or 'n': ")

if cont_game == "n":
    if sum_y > sum_c:
        print(f"You win, Computer card is {computer_guess}. You have the jackpot")
    else:
        print(f"You lose Computer card is {computer_guess}. Computer has the jackpot")
else:
    new_guess = random.choice(cards)
    your_cards.append(new_guess)
    print(your_cards)
    your_new_cards = sum(your_cards)
    if your_new_cards > 21:
        print("You lose. Your card choice is greater than 21")
    elif your_new_cards > sum_c:
        print(f"You win, Computer card is {computer_guess}. You have the jackpot.")
    else:
        print(f"You lost. Computer card is  {your_new_cards} and Computer card is {sum_c}")
"""

""" 
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print("False")
            break
    else:
        print("True")
#print(False)

is_prime() 

"""

