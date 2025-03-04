## Manual Testing for Timer feature

### Scenario: As the user plays the game
- Given the user has pressed enter to start the game
- When the timer shows in the top right corner
- And lives > 0
- [Then the timer should increase](screenshots/timer_increase.png)

### Scenario: If the user loses the game
- Given the user has pressed enter to start the game
- When the user collides with 3 asteroids
- And lives = 0
- [Then the Game Over screen should appear with the user's recorded time](screenshots/show_in_game_over.png)
