while True:
	print("which number do you want to calculate?(Press 0 to quit program)")
	whichNumber=int(input())
	if whichNumber is 0: break
	print('calculate ',whichNumber)
	for i in range(1,10):
		print(whichNumber,'x',i,'=',whichNumber*i)
print('Program Done')
