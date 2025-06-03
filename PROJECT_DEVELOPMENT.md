# __Project Development__

## __Sprint 1__

### __Requirements__

#### __Functional Requirements__
* The game should generate a map that marks the progression of the player through the game
* The map will consist of various branching points that the player chooses between throughout the game to go further
* In the case that the player dies at some point in the game, the game will reset and the player must start again
* After succeeding in various challenges, the player collects rewards that allow them to complete harder challenges
* In combat scenarios the player will be able to move around on a grid every turn they take
* In combat there will be enemy to attack the player that move at the same rate
* In combat the player will be able to attack the enemy on their turn
* The rewards that the player collects will allow them to make different actions on their turn, and make existing actions stronger
* The map will contain harder enemies that the player can choose on
* The game will finish with the player fighting a much harder enemy

#### __Non-Functional Requirements__
* The player should be able to easily tell what each action is on the ui
* The player should be able to see the effect of each action before they commit to it
* The map should appear different every time
* The game should react to the players choices almost as soon as the player makes them
* The game should be pixel-art based
* The game should have a couple accessibility options, like changing key functions and changing the display

### __Usecases__
__Actor:__ Player
__Preconditions:__ Software installed
__Main Flow:__
1. Player selects 'play' button to enter game on map
1. Player selects which location on map to enter
1. Player participates in combat
__Postconditions:__ Player has participated in game

### __Design__

#### __Storyboard__
![Alt text](Images%20and%20other%20files/Storyboard.png)

#### __Data Flow Diagrams__

##### __Level 0 Data Flow Diagram__
![Alt text](Images%20and%20other%20files/Level%200%20Data%20Flow%20Diagram.png)

##### __Level 1 Data Flow Diagram__
![Alt text](Images%20and%20other%20files/Level%201%20Data%20Flow%20Diagram.png)

#### __GANTT Chart__
![Alt text](Images%20and%20other%20files/Online%20Gantt%2020250520.png)

### __Review__
1. My code fulfills some of the requirements, however there are many that will be fulfilled later. For instance, only the board is currently in existance, because I would like to program effectively from the beginning, I am unable to create a rudimentary UI without programming a large amount of the functionality in the code. The map, all combat features, as well as all art is not present in the build currently, as it is difficult to create a UI how I would like, due to the large amount of screens that I would like to put in the game
1. The program does not allow most of the parts of the usecase provided, due to only one section of the code being completed
1. The code has fairly functional structure which is also quite intuitive to understand, however there is very little comments on the code, only a few objects have explanations
1. The next improvements are to create a menu screen, and implement a map for the player to use