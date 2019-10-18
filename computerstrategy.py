import random
def strategy(player_number_list):
	temp = []
	if not player_number_list:
		return random.randrange(1,3)				#Initially when there is no previous input from  
	else:                                           		#opponent side then the smallest possible number will be returned
		for i in player_number_list:         

			if i == 3:
				temp.append(random.randrange(3,5))	#if opponent entered 3 then there is probablity
										#that either he will enter 2 or 3 then if computer's
													#choice is either 3 or 4 then computer will get 2 point 
													#but at worst case opponent will get 1 point	
			
			elif i == 1 or i ==2:					
				temp.append(random.randrange(3,4))	#if opponent continuously trying to choose least number
													#then either he will choose 3 or continue with 1 or 2 then 
													#if computer's number will be 3 and player's number is 2 then
													#computer will get 2 point and if same number then no point
			
			else:
				temp.append(random.randrange(1,3))	#if neither of the above case and opponent choose
													#any greater number then least possible values will be return

	#print(set(temp))
	return random.choice(list(set(temp)))			



if __name__ == '__main__':
	player_point = 0
	my_point = 0
	player_number_list = []
	while player_point < 5 and my_point < 5:
		player_number = int(input("Enter any number: "))
		my_number = strategy(player_number_list)
		player_number_list.append(player_number)

		print("Your Number: ",player_number)
		print("Computer Number: ",my_number)
		
		if player_number +1 == my_number:
			my_point += 2
		elif player_number+1 < my_number:
			player_point += 1
		elif my_number+1 < player_number:
			my_point += 1
		elif my_number+1 == player_number:
			player_point += 2
		
		print("Your Point",player_point)
		print("Computer Point",my_point)

	if my_point > player_point:
		print("Computer Strategy Won")
	else:
		print("You Won")

