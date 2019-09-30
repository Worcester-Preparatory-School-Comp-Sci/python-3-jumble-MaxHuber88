import random
# MAX HUBER 9/30
print("Hi! Welcome to the Scrambler!\nEnter 0 to exit.") # welcome player, init variables
wordlist = ["dog","cat","fish","banana"]
scrambledword = ["","","","","","","","","","","","","","",""]
scramble = ""
playing = True
foundPlace= False
trying = True

while playing == True: #this while loop only ends when the player enters 0 to exit
	# reset variables each time new word is to be guessed
	scrambledword = ["","","","","","","","","","","","","","",""]
	scramble = ""
	foundPlace= False
	trying = True
	
	selected = wordlist[random.randint(0,len(wordlist) - 1)] #select a random word from the list
	for x in range(0,len(selected)): #scramble word
		foundPlace = False
		while foundPlace == False:
			i = random.randint(0,len(selected) - 1)
			if scrambledword[i] == "":
				scrambledword[i] = selected[x]
				foundPlace = True
	scramble = scrambledword[0]+scrambledword[1]+scrambledword[2]+scrambledword[3]+scrambledword[4]+scrambledword[5]+scrambledword[6]+scrambledword[7]+scrambledword[8]+scrambledword[9]+scrambledword[10]+scrambledword[11]+scrambledword[12]+scrambledword[13]+scrambledword[14]
	print(scramble) #print scrambled word
	
	while trying == True: #this loop only ends when player guesses correctly or enters 0 to exit
		guess = input("^  What is this word?" +"\n")
		if guess == selected:
			print("Yes! Try another one!")
			trying = False
		elif guess == "0":
			print("Exiting game...")
			trying = False
			playing = False
		else:
			print("No way! Try Again!")
			print(scramble)

