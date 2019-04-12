# The pin number of Hong Gil Dong is 881120-1068234
pinNumber = '881120-1068234'
ListPinNumber = pinNumber.split('-')
print(ListPinNumber)
FRONT = ListPinNumber[0]
BACK = ListPinNumber[1]
print("YEAR ", FRONT)
print("BACK ", BACK)
GENDER = BACK[0:1]
print(GENDER)
