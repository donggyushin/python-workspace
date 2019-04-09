print('input number')
decimal = int(input())
binary = ''
while decimal >= 1:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
print(binary)
