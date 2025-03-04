## Manual testing for High Score feature

### Scenario: If the user scores > than the longest time in the middle
- Given the user has pressed enter to start the game
- [When the time in the top right is higher than the time in the middle](screenshots/higher_than_middle.png)
- And lives = 0
- And the Game Over screen appears
- And the user presses the enter key to restart the game
- [Then the new high score should replace the previous one and be static in the top middle of the screen](screenshots/new_score_top_middle.png)

### Scenario: If the user scores < than the longest time in the middle
- Given the user has pressed enter to start the game
- [When the time in the top right is lower than the time in the middle](screenshots/lower_than_middle.png)
- And lives = 0
- And the Game Over screen appears
- And the user presses the enter key to restart the game
- [The current high score should remain and be static in the top middle of the screen](screenshots/current_top_middle.png)