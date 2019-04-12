string = 'a:b:c:d'
convertedString = string.replace(":", "#")
print(convertedString)
convertedString2 = "#".join(string.split(":"))
print(convertedString2)
