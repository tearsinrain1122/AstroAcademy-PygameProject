# Manual Testing for Astronaut Movement

### Scenario: Player (Astronaut) moves up when the up key is pressed
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- When the up key is pressed
- [Then "moving up' is printed in the terminal](screenshots_move/up/up_screenshots.md)
- And the player moves up by one unit

### Scenario: Player (Astronaut) moves down when the down key is pressed
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- When the down key is pressed
- [Then "moving down" is printed in the terminal](screenshots_move/down/down_screenshots.md)
- And the player moves down by one unit

### Scenario: Player (Astronaut) moves left when the left key is pressed 
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- When the left key is pressed 
- [Then "moving left" is printed in the terminal](screenshots_move/left/left_screenshots.md)
- And the player moves left by one unit

### Scenario: Player (Astronaut) moves right when the right key is pressed
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- When the right key is pressed
- [Then "moving right" is printed in the terminal](screenshots_move/right/right_screenshots.md)
- And the player moves right by one unit

### Scenario: Player (Astronaut) does not move without keys being pressed
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- When no key is pressed 
- Then the player remains in the same position
- And nothing is printed in the terminal
