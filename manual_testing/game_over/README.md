## Manual testing for Game Over feature

### Scenario: If the user's lives = 0
- Given the user has pressed enter to start the game
- When the user collides with 3 asteroids
- And lives = 0
- [Then the Game Over screen should appear](screenshots/game_over_screen.png)

### Scenario: If the user's lives > 0
- Given the user has pressed enter to start the game
- When the user collides with 3 asteroids
- And lives > 0
- [Then the Game Over screen should not appear](screenshots/not_game_over.png)


