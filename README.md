# tic-tac-toe
tic tac toe (1 agent game)


__INTRODUCTION__:
Tic tac toe is a 3 X 3 board game where user tries to make three continuous combinations of "X" or "0" either row wise,column wise or digonally to win this game. In my case here "X" is user and "0" is computer.I have used python programming language to make this game. 

__LIBRARIES USED__:
I have imported __random module__ which is pre-defined module in library.I have used __random.randint()__ function which is a built-in function already defined in random module. *This function takes two arguments, first argument is the start value and the second argument is the end value after which the integers between this range including arguments passed by us can be used.* 

__SOME CODE'S LINES EXPLAINATION:__
 
 __1.moves_available=[[1,1],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2],[3,3]]__:
This line is telling us the moves availabe in this game. Once the user uses one of the move that move is vanished from this list.
*FORMAT:[ROW,COLUMN]*

__2.if [row,column] in  moves_available:__
This line is used is so that the "X" user cannot use this move once the user has used this move.

__REFERENCE__:

I have studied about *random module* from this site[https://www.tutorialsteacher.com/python/random-module]

