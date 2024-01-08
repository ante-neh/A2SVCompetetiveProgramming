Biniyam is organizing a chess tournament at A2SV. He has a list of 2n
 players in the tournament and each chess player has a rating. Being a high rated player himself, he knows that if the difference in rating between two players is above k
, it's impossible for the lower rated player to win.

The tournament is structured as a single-elimination bracket: players will compete in pairs until one winner remains. In the first round, player 1 will play against player 2, player 3 against player 4 and so on. For the second round, the winner of player 1 and player 2 will play against the winner of player 3 and player 4 and so on.

Given the list of players' ratings, Biniyam wants to determine which players have a chance of winning the tournament.

Input
The first line contains two integers n
 (1≤n≤18)
 and k
 (10≤k≤1000)
, the number of rounds and the maximum difference where the lower player can win a match. The next line will contain 2n
 integers a
, where ai
 (100≤ai≤2500)
 is the rating of the i
-th player.

Output
Print a space separated list of players that could win the tournament sorted by their index.

Examples
input
2 400
1000 200 400 600
output
1 4
input
2 400
1000 600 200 400
output
1 2 3 4
Note
For the first example, in the first round, the second player (rated 200) can not win because the difference between them and the opponent is more than k. But both the 400 rated player and the 600 rated player have a possibility of winning. In the second round, the 400 rated player has no chance to win against the 1000 rated player and will therefore cannot possibly win the tournament.