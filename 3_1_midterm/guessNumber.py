from random import randint
number = randint(1, 100)
correct = False
print("Take a guess number between 1 and 100")
while not correct:
    userNumber = int(input())
    if userNumber > number:
        print('The number is too big')
    elif userNumber < number:
        print("The number is too small")
    else:
        correct = True
print('Correct!')
