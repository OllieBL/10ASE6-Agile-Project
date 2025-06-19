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
![Alt text](Images%20and%20other%20files/Documentation%20images/Storyboard.png)

#### __Data Flow Diagrams__

##### __Level 0 Data Flow Diagram__
![Alt text](Images%20and%20other%20files/Documentation%20images/Level%200%20Data%20Flow%20Diagram.png)

##### __Level 1 Data Flow Diagram__
![Alt text](Images%20and%20other%20files/Documentation%20images/Level%201%20Data%20Flow%20Diagram.png)

#### __GANTT Chart__


### __Review__
1. My code fulfills some of the requirements, however there are many that will be fulfilled later. For instance, only the board is currently in existance, because I would like to program effectively from the beginning, I am unable to create a rudimentary UI without programming a large amount of the functionality in the code. The map, all combat features, as well as all art is not present in the build currently, as it is difficult to create a UI how I would like, due to the large amount of screens that I would like to put in the game
1. The program does not allow most of the parts of the usecase provided, due to only one section of the code being completed
1. The code has fairly functional structure which is also quite intuitive to understand, however there is very little comments on the code, only a few objects have explanations
1. The next improvements are to create a menu screen, and implement a map for the player to use

## __Sprint 2__

### __Design__

#### __Structure Chart__
![Alt text](Images%20and%20other%20files/Documentation%20images/Screenshot%202025-06-11%20093929.png)

#### __Algorithms__

##### __Pseudocode__
```
    BEGIN main
        RunMenu
        RunMap
    END main

    BEGIN RunMenu
        runmenu = True
        WHILE runmenu is True
            clear page
            create title
            create start button
            IF start button is clicked THEN
                runmenu = False
            ENDIF
        ENDWHILE
    END RunMenu

    BEGIN RunMap
        runmap = True
        WHILE runmap is True
            clear screens
            create rooms
            create choice buttons
            arrange map
            IF choice button clicked THEN
                RunRoom
            ENDIF
            IF player has completed all rooms THEN
                runmap = False
            ENDIF
        ENDWHILE
    END RunMap

    BEGIN RunRoom
        runroom  = True
        WHILE runroom is True
            clear screen
            create tiles
            place combat objects on tiles
            create action buttons
            IF action button clicked THEN
                player performs action
                enemy performs action
            ENDIF
            IF player is dead OR all enemies are dead THEN
                runroom = False
            ENDIF
        ENDWHILE
    END RunRoom
```

#### __Flowcharts__
![Alt text](Images%20and%20other%20files/Documentation%20images/main%20flowchart.png)

![Alt text](Images%20and%20other%20files/Documentation%20images/runmenu%20flowchart.png)

![Alt text](Images%20and%20other%20files/Documentation%20images/runmap%20flowchart.png)

![Alt text](Images%20and%20other%20files/Documentation%20images/runroom%20flowchart.png)

### __Review__
1. There are several of the requirements that I made that my code fulfills, but several that it doesn't. The functional requirements that my code fulfills are the generation of the map, the branching points, grid movement in combat, and the map contains optional harder encounters for better rewards. The functional requirements that it doesn't fulfill is player death, attacks, and the final boss. The non-functional requirements that it meets are the easily visible changes in the map between games, and speed of the game, however it isn't very accessible yet, doesn't give information on choices before they are made, the game doesn't have any art, and the game doesn't have any accessibility options. Overall, the program as it is doesn't meet a large amount of requirements however most core requirements are met.
2. The program effectively performs the flow outlined in the usecase, the player is able to click the play button, the player can select what place on the map they want to enter, and the player can participate in combat. However, the actions in these steps are not particularely intuitive, and the combat does not function.
3. My code is fairly high quality, however lacks proper inline documentation, with few comments dictating the use of certain function. Despite this, the code is stuctured quite efficiently and in a fairly readable structure. In addition to this, the code is fairly maintainable, with proper use of functions and classes allowing for stand in sections for the code that is not yet completed.
4. In the next step my code needs to have the combat feature, and the art implemented. I also need to add more comments to my code to help with the readability of my code.

## __Sprint 3__

### __Design__

#### __Structure Chart__
![alt text](<Images and other files/Documentation images/Class Diagram.png>)

### __Review__
1. The game does not yet fully contain every requirement that I sepcified, however it contains many of them. the game generates a map that the player can move through, and the player can make choices in each point. The player gets rewards at the end of challenges to allows them to progress farther. Combat contains many of the features outlined, like movement, turns, and attacking. It also contains optional harder challenges. However, the player cannot yet die, the game doesn't reset, the player only has the two existing kinds of actions, and their is no final boss. In the non-functional requirements, the ui is mostly intuitive, the map is noticeably randomised, but the game contains no art, there is no feedback before the player makes an action, the game slows down noticeably when multiple enemies appear on-screen, and there are no accessibility options.
2. The program can effectively run the use-case, all different parts of the ui are functional and interconnected. There is still no feedback or input assistance during combat though, which may make it difficult to play
3. My code is well structured, fairly readable, and maintainable. All my code is organised in a fairly logical way, and the code is readable, there is comments in most of the program outlining how it works and what is does, and because of the structure of the code it is fairly easy to read what each section does anyway. The code is maintainable because of each of these two things contributing, allowing further developers to understand the code and what needs to be changed 
4. In the next stage of development I need to introduce the player dieing, and enemy damage. I also need to add further comments in my code

## __Sprint 4__

### __Design__
Only two improvements will be added to the code in this stage, the introduction of the death of the player and the further adding of comments in the code.
The way I will implement the death mechanic is through the player taking damage from enemies over time, then when they reach 0 hp, then the game resets and goes back to the menu

### __Review__
1. my code meets almost all functional requirements and several of the non-functional requirements specified at the beginning of the project. The functional requirements that I do meet include, map generation, branching paths, player death and reseting, rewards after challenges, combat, and being able to choose harder enemies. However, I missed adding additional forms of actions to use, and missed adding a boss battle at the end. The non-functional requirements that I did meet are readable ui, and randomised map, however it does not provide what the action will look like before it is taken, the game slows down at later levels, and it lacks accessibility options.
2. The program fulfills the use-case quite effectively, it can go through every step in the process without much difficulty, but the game doesn't reset if you win, and it is difficult to use in some scenarios
3. My code is fairly readable, well structured, and easy to maintain. The code is well structured, which contributes to the readability, because it is ordered in a way where all individual functions are well split out and distinguishable. The code is readable because of this, and there are comments thoughout most of the code, and it is maintainable because of the combination of these two parts

## __Evaluation__
1. The next steps I would take is adding art to the program, to make it nicer to use, improving the user input to make it more intuitive, and adding more strategic elements in the combat, like adding extra actions and harder enemies. These would all improve the user experience because the art would make it nicer to use, the improved user inputs would make it easier and more intuitive for the player, and the improved combat would make it better because extra challenge requires the player to put more thought into the game, and increase its longevity, though it may make it less fun for some people seeking a very simple experience.