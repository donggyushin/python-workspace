while True:
    print("구구단 몇 단을 계산할까요? (1~9)")
    user_input = int(input())
    if user_input is 0:
        break
    for i in range(10):
        print(user_input, "x", i, "=", user_input*i)
