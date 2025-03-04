# Manual Testing for the exit button feature

## Feature: Exit button functionality
- To easily exit the game, the user can press the exit button to close the game
- [Exit button code - tested](exit_screenshots/code_exit.png)

### Scenario: Exit button closes the game
- [Given the user has successfully loaded the game, entered their name and pressed enter to start](exit_screenshots/exit.png)
- When the player presses the red exit button in the top left-hand corner of the screen
- Then the game closes 
- [And 'exit button pressed on screen' is printed in the terminal](exit_screenshots/pressed_button.png)
