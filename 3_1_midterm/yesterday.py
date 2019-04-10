# Counting program that counts how many 'yesterday' are in the lyrics of yesterday of beatles
WORD_TO_FIND = 'YESTERDAY'
f = open("yesterday.txt", 'r')
yesterday_lyric = f.readlines()
f.close

contents = ""
for line in yesterday_lyric:
    contents = contents+line.strip()+"\n"

n_of_yesterday = contents.upper().count(WORD_TO_FIND)
print("Number of a word 'Yesterday' is ", n_of_yesterday)
