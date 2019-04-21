import random

guess_number = random.randint(1, 100)
print('숫자를 맞혀 보세요. (1~100)')

while True:
    user_input = int(input())
    if user_input == guess_number:
        break
    elif user_input > guess_number:
        print('숫자가 너무 큽니다. ')
    elif user_input < guess_number:
        print('숫자가 너무 작습니다. ')
print("정답입니다. 입력한 숫자는", guess_number, "입니다. ")
