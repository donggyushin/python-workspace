print("2진수로 변환 할 10진수를 입력해주세요. ")
user_input = int(input())
decimal = ''
while user_input is not 0:
    decimal = str(user_input % 2) + decimal
    user_input = int(user_input / 2)
print(decimal)
