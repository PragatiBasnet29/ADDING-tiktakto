# Tic-Tac-Toe Game with AI

A simple Tic-Tac-Toe game built in Python using a graphical interface (`tkinter`) and an unbeatable AI opponent powered by the **Minimax algorithm**. This project is a great way to learn about basic GUI programming in Python and how the Minimax algorithm can be used in game development.

## Screenshot

![Tic-Tac-Toe Game Screenshot](screenshot.png)

## Features

- **Graphical User Interface**: Play the game on a 3x3 grid with an intuitive interface using `tkinter`.
- **Unbeatable AI**: The AI opponent uses the Minimax algorithm, ensuring it always makes the best possible move.
- **Automatic Win Detection**: The game detects when a player has won or if the game ends in a tie, displaying a message to announce the result.
- **Easy-to-Reset Game**: After each game, the board can be reset for a new game session.

## How to Play

- **Player Symbol**: The human player always plays as `X`, while the AI is `O`.
- **Turn Order**: The human player goes first.
- **Win Condition**: Get three of your marks (either `X` or `O`) in a row, column, or diagonal.
- **Unbeatable AI**: The AI uses Minimax, making it impossible to defeat. Try for a tie!

## Installation

This project only requires **Python 3.x** and the standard `tkinter` library. To set up, follow these steps:

1. **Install Python 3.x** (if not already installed). Download it from [Python's official website](https://www.python.org/).
2. **Install tkinter**:
   - On Debian/Ubuntu: `sudo apt-get install python3-tk`
   - For Windows and macOS: `tkinter` usually comes bundled with Python, so no additional installation is required.
3. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   ```

## Running the Game

Run the following command in the project directory:

```bash
python tic_tac_toe.py
```

This will open the game window where you can start playing Tic-Tac-Toe against the AI.

## Code Structure

- **minimax()**: Implements the Minimax algorithm to choose the optimal move for the AI.
- **ai_move()**: Determines the AI's move based on Minimax output.
- **check_winner()**: Checks the board state to see if either player has won.
- **is_tie()**: Checks if the board is full without a winner, resulting in a tie.
- **button_click()**: Handles player moves and updates the game state.
- **reset_board()**: Resets the board for a new game session.

## Technologies Used

- **Python**: The core programming language for the game logic.
- **tkinter**: Python’s standard GUI library for creating the user interface.

## Future Improvements

- Add a scoring system to track wins, losses, and ties across multiple games.
- Implement difficulty levels by adjusting the AI's move choices.
- Add a start menu with options for single-player and two-player modes.

## License

This project is open-source under the MIT License. You are free to use, modify, and distribute this code.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
