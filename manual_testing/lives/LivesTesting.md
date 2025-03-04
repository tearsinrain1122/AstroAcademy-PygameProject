# Manual testing for the Lives feature

## Feature: Player (Astronaut) collision with Asteroid(s) causing the reduction of lives
- To make the game more competitive, the players lives should start at three and reduce at every collision with an Asteroid and then ending the game after three collisions
- [Code for testing lives](lives_test_screenshots/lives_code.png)

### Scenario: Player (Astronaut) with an Asteroid and lives reduce by 1
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player starts the game with 3 lives
- And the health bar is fully green
- And the asteroid(s) is moving toward the player
- When the asteroid reaches the player's position
- [Then the lives printed on screen reduce by 1](lives_test_screenshots/one_hit.png)
- And the number of lives remaining are printed in the terminal

### Scenario: Player (Astronaut) loses all lives due to collision with 3 Asteroids and the game ends
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player starts the game with 3 lives
- And the health bar is fully green
- And the asteroid(s) is moving toward the player
- When the player collides with an asteroid 3 times 
- [Then the number of lives printed in the terminal are 0](lives_test_screenshots/three_hits.png)
- And 'Game Over' is printed on the screen

### Scenario: Player (Astronaut) does not collide with any Asteroids, losing no lives
-  Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player starts the game with 3 lives
- And the health bar is fully green
- And the asteroid(s) is not moving toward the player, or the player moves away from the Asteroid(s)
- When the player does not collide with an asteroid
- Then no lives are lost, remaning the same