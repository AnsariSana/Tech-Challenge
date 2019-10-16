import random
def strategy(player_number_list):
	temp = []
	#print("in function")
	#print(player_number_list)
	if not player_number_list:
		return random.randrange(1,3)
	else:
		for i in player_number_list:
			if i == 3:
				temp.append(random.randrange(3,5))
			elif i == 1 or i ==2:
				temp.append(random.randrange(3,4))
			else:
				temp.append(random.randrange(1,3))

	#print(set(temp))
	return random.choice(list(set(temp)))



if __name__ == '__main__':
	player_point = 0
	my_point = 0
	player_number_list = []
	while player_point < 5 and my_point < 5:
		player_number = int(input("Enter any number"))
		my_number = strategy(player_number_list)
		player_number_list.append(player_number)

		print("player_number",player_number)
		print("my_number",my_number)
		
		if player_number +1 == my_number:
			my_point += 2
		elif player_number+1 < my_number:
			player_point += 1
		elif my_number+1 < player_number:
			my_point += 1
		elif my_number+1 == player_number:
			player_point += 2
		
		print("player_point",player_point)
		print("my_point",my_point)

	if my_point > player_point:
		print("My strategy wins")
	else:
		print("You win")

