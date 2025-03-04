# Manual Testing for Astronaut Interaction with the Screen Edges

## Feature: Player (Astronaut) interaction with Screen Edges
- To ensure the player (Astronaut) stays within the game boundaries, the game should detect  and stop the player moving off the screen

### Scenario: Player (Astronaut) hits the top edge of the screen
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player is moving upward
- And the player is at the top edge of the screen
- When the player tries to move further upward
- [Then this is detected and "Hit the top edge!" is printed in the terminal](edge_test_screenshots/top.png) 
- And the player cannot move further upward

### Scenario: Player (Astronaut) hits the bottom edge of the screen
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player is moving downward or starting the game (default position)
- And the player is at the bottom edge of the screen
- When the player tries to move further downward
- [Then this is detected and "Hit the top bottom!" is printed in the terminal](edge_test_screenshots/bottom.png) 
- And the player cannot move further downward

### Scenario: Player (Astronaut) hits the left edge of the screen
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player is moving left
- And the player is at the left edge of the screen
- When the player tries to move further left
- [Then this is detected and "Hit the left edge!" is printed in the terminal](edge_test_screenshots/left.png) 
- And the player cannot move further left

### Scenario: Player (Astronaut) hits the right edge of the screen
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player is moving right
- And the player is at the right edge of the screen
- When the player tries to move further right
- [Then this is detected and "Hit the right edge!" is printed in the terminal](edge_test_screenshots/right.png) 
- And the player cannot move further right