# Tech-Challenge
Number Game Script

The Challenge:

There are two players.
Each player writes a number, hidden from the other player. It can be any integer 1 or greater.
The players reveal their numbers.
Whoever chose the lower number gets 1 point, unless the lower number is lower by only 1, then the player with the higher number gets 2 points.
If they both chose the same number, neither player gets a point.
This repeats, and the game ends when one player has 5 points.
 

The challenge is to write a script to play this game. Knowing the rules and all your opponent’s previous numbers, can you program a strategy? (And, no - return random.randint(1, 3) is not a strategy.) You should really try playing this first with your friends - you’ll see there’s a deep human element to predicting your opponent’s choice.

Solution:

As game is based on guessing the next number of opponent player and strategy should return the number which will make strategy to won at most times.

case 1. If no previous input of opponent then return least possible number either 1 or 2 because opponent will most likely
        to choose least number.

case 2. If opponent entered 3 then there is probablity that either he will enter 1,2 or 3 then if computer's choice is either 3         or 4 then computer will get 2 point if opponent choose 2 or 3 respecctively.But at worst case if opponent choose 1
        then opponent will get 1 point.
        
case 3. If opponent continuously choosing 1 or 2 so that he will win then computer will return 3 if number is 2 either computer         will get 2 point or 0 and if opponent choose 1 again then computer will either return 2 or 3 so that at worst case 
        opponent will get 1 point.
        
case 4. If opponent choose any greater number then return least possible number to earn point.

temp list contains most probable values to be return among them 1 will be choosen.
