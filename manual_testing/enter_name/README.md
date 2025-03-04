## Manual testing for Enter Name feature

### Scenario: If the user enters a name
- Given the user has successfully loaded the game
- [When the user follows the prompt to type their name](screenshots/enter_name.png)
- And presses enter to start the game
- And lives = 0
- [Then the name the user entered should appear on the game over screen](screenshots/enter_name_game_over.png)

### Scenario: If the user does not enter a name
- Given the user has successfully loaded the game
- [When the user does not enter their name](screenshots/no_name.png)
- And presses enter to start the game
- And lives = 0
- [Then the default name should appear on the game over screen](screenshots/no_name_game_over.png)