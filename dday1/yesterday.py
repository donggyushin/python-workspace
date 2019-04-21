f = open("yesterday.txt", 'r')
yesterday_lyric = f.readlines()
f.close()
contents = ""
for line in yesterday_lyric:
    contents = contents + line

number_of_yesterday = contents.lower().count('yesterday')
print(number_of_yesterday)
