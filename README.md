
# Question

A basket has ‘n’ fruits of two types - apples and oranges. They decide to play a game. The
game is played in multiple rounds until one of the fruit types wins (either apple or orange). In
each round, every ‘eligible’ fruit gets to perform one of the two actions.

# Action1:
 Disqualify one member of another fruit type from the game, so that they cannot perform any
action in the current round or any subsequent rounds. (Disqualified fruit becomes ‘ineligible’
and cannot perform any actions)

# Action2:
  If all members of another fruit type are disqualified(ineligible), declare his fruit type as the winner
of the game.

# 
Every round begins with fruits performing actions in the given order, and every fruit chooses
the action best for his fruit type, predict which fruit type will be the winner!. Time complexity
O(n) and space complexity O(n)

Input: A string s of length ‘n’ representing order in which ‘n’ fruits can perform an action in
every round. (‘A’: apple, ‘O’: orange) Output: Winner type: string (either “apple” or “orange”)

# Example 1:
Input: s= “AO” (here n=2)

Output: “apple”

Explanation:
In round1, fruits start performing actions in the given order (left to right).

First, ‘A’ will choose Action1 and disqualify ‘O’ from the game.

Now second ‘O’ is permanently disqualified and cannot perform any actions. 

Round 1 ends.

In round 2: ‘A’ will choose Action2 as he’s the only ‘eligible’ member in the basket as ‘O’ was disqualified
in the previous round. Hence the winner fruit type is “apple”.

# Example 2:
Input: s= “AOO” (here n=3)
Output: “orange”

First fruit, ‘A’ will choose Action1 and disqualify second ‘O’from the game.

Now second ‘O’ is permanently disqualified and cannot perform any actions, so it is skipped.

Next, 3rd fruit ‘O’ will choose Action1 anddisqualify first fruit ‘A’. Round 1 ends.

In round 2: Now both first ‘A’ and second ‘O’ are disqualified after round1, the only eligible fruit left is third ‘O’,
so he will choose Action2 and declare fruit type “orange” as the winner.

