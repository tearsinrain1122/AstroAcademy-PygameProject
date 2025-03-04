# Manual testing for Asteroid Collision

## Feature: Player (Astronaut) Collision with Asteroids
- To ensure the game reacts correctly to collisions, the player loses a life when hit by an asteroid and 'hit' is printed in the terminal.

### Scenario: Player (Astronaut) collides with an Asteroid
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the asteroid(s) is moving toward the player
- When the asteroid reaches the player's position
- [Then "hit" is printed in the terminal](collision_screenshots.md)

### Scenario: Player (Astronaut) does not collide with an Asteroid
- Given the user has successfully loaded the game, entered their name and pressed enter to start
- And the player moves away from the Asteroid(s)
- When the asteroid does not reach the player's position
- Then "hit" is not printed in the terminal

