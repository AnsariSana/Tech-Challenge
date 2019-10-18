import random
def strategy(player_number_list):					#strategy function to choose number using
									#this strategy from computer's side.
	#print(player_number_list)
	if not player_number_list:					#Initially when there is no previous input from
		return random.randrange(1,3)				#opponent side then the smallest possible number will be returned.
	else:
			if player_number_list[-1] >= 3:			#If last element entered by the user is 3 or greater then
									#that then return smallest possible number
				player_number_list.pop()			#pop the top most element to check if further opponent
													#may use only smallest numbers
				return random.choice([1,3,4])		#here choice method is used because if it return
													#2 and opponent will enter 3 then opponent will gain 2 points.

			elif len(set(player_number_list) - {1,2}) == 0:		#If opponent continuously trying to use either 1
				return random.randrange(2,4)					#or 2 or 1,2 then return 2,3 

				
			else:
				return random.randrange(1,3)					#If neither of the case then return smallest possible number




if __name__ == '__main__':										#__main__ implies that the module is being run standalone and not imported
	player_point = 0
	my_point = 0
	player_number_list = []
	while player_point < 5 and my_point < 5:					#Game will be continued till either player_point < 5 and 
																#computer point < 5.
		player_number = int(input("Enter any number: "))
		my_number = strategy(player_number_list)
		player_number_list.append(player_number)

		print("Your Number: ",player_number)
		print("Computer Number: ",my_number)
		
		if player_number +1 == my_number:						#If opponent's number is only lower by 1 than
			my_point += 2										#computer's then computer will get 2 points.


		elif player_number+1 < my_number:						#If opponent's number is lower than computer's
			player_point += 1									#then opponent will get 1 point.


		elif my_number+1 < player_number:						#If computer's number is lower than opponent then
			my_point += 1										#computer will get 1 point.


		elif my_number+1 == player_number:						#If computer's number is only lower by 1 then
			player_point += 2									#opponent will get 2 points.
		
		print("Your Points",player_point)
		print("Computer Points",my_point)

	if my_point > player_point:
		print("Computer Strategy Won")
	else:
		print("You Won")

