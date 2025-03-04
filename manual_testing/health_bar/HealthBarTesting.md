# Manual Testing for Health Bar

## Feature: Player (Astronaut) collision with Asteroid(s) causing reduction of the health within the health bar
- To make the game challenging, the players health bar should reduce with each collision with an asteroid and then ending the game after three collisions. 
- [Code for testing health bar](health_bar_tests/health_code.png)

### Scenario: Player (Astronaut) collides with and Asteroid and health bar reduces
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player starts the game with 3 lives
- And the health bar is fully green
- And the asteroid(s) is moving toward the player
- When the asteroid reaches the player's position
- [Then the green in the health bar is reduced](health_bar_tests/loss_1.png)
- And "health bar reduced" is printed in the terminal
- And the player has 2 lives remaning

### Scenario: Player (Astronaut) loses all lives due to collision with Asteriods and the game ends
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player starts the game with 3 lives
- And the health bar is fully green
- And the asteroid(s) is moving toward the player
- When the player collides with an asteroid 3 times
- [Then "health bar reduced' is printed 3 times in the terminal](health_bar_tests/health_bar1.png)
- And all the green in the health bar is gone 
- And "Game Over" is on the screen

