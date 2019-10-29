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
strategy is about choosing between i-2 or i+1 where i will be likely to choosen by opponent where i > 2.

case 1. If no previous input of opponent then return least possible number either 1 or 2 because opponent will most likely
        to choose least number.

case 2. If opponent choose 3 or greater number then return least possible number and pop greater number so that if opponent
        choose smaller numbers or either only 1 or 2 or 1,2 in pattern to win.So to check that pattern pop greater elements.
        
case 3. If opponent continuously trying to choose 1 or 2 to increase chances of win then either return 2 or 3 respectively then 
        computer will get 2 points or at worst case opponent will get 2 points if it chooses 3.
        
case 4. If neither of the case then return smallest possible number.

