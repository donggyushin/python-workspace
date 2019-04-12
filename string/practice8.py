# Write a code that mutiply 2 only to odd number of list.
numbers = [1, 2, 3, 4, 5]
convertedNumbers = []
for i in numbers:
    if(i % 2 == 1):
        convertedNumbers.append(i*2)
print(convertedNumbers)
