# Tech-Challenge
Number Game Script
As game is based on guessing the next number of opponent player and strategy should return the number which will make strategy to won
at most times.
case 1. If no previous input of opponent then return least possible number either 1 or 2 because opponent will most likely
        to choose least number.

case 2. If opponent entered 3 then there is probablity that either he will enter 1,2 or 3 then if computer's choice is either 3         or 4 then computer will get 2 point if opponent choose 2 or 3 respecctively.But at worst case if opponent choose 1
        then opponent will get 1 point.
        
case 3. If opponent continuously choosing 1 or 2 so that he will win then computer will return 3 if number is 2 either computer         will get 2 point or 0 and if opponent choose 1 again then computer will either return 2 or 3 so that at worst case 
        opponent will get 1 point.
        
case 4. If opponent choose any greater number then return least possible number to earn point.

temp list contains most probable values to be return among them 1 will be choosen.
