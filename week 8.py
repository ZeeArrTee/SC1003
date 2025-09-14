import random

width = 4
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def gen_number():
    numbers = []
    for i in range(0, width):
        random.shuffle(numlist)
        numbers.append(numlist[1])
    return numbers


def input_numbers():
    guess = input("input a 4 digit number")
    while guess.isdigit == False or len(guess) != width:
        guess = input("wrong fromat! input again")

    user_guess = []

    for i in range(0, width):
        user_guess.append(int(guess[i]))

    return user_guess


def compare(guess, num):
    bull = 0
    cow = 0
    for i in range(0, width):
        if guess[i] == num[i]:
            bull += 1
        elif guess[i] in num:
            cow += 1

    return (bull, cow)


num = gen_number()
attempt = 0

while True:
    # print(num)
    guess = input_numbers()
    # print(guess)
    attempt += 1  # include successful attempt
    comp = compare(guess, num)
    print(comp[0], "A", comp[1], "B")
    # print (comp)
    if comp[0] == width:
        print("congrats you guessed correctly!!! You did it in", attempt, "attempts")
        break
    else:
        print("try again",str(guess),"is wrong")
