# TetrisProject
## Universidad Central del Ecuador
### Programación I
#### Members
* Diego Iza
* Mateo Safla 

## Tetris in Python 🎮

<div align="center">
  <img src="https://github.com/user-attachments/assets/daa1754f-906d-4715-b8a1-cba2ec6cd344" alt="Tetris" width="300">
</div>

#### Description 📜
Welcome to Tetris in Python! This project is an implementation of the classic Tetris game using Python and Pygame. Below, you will find all the project information.

#### Game Overview🕹️
Tetris is a tile-matching puzzle video game originally designed and programmed by Alexey Pajitnov. The game has been ported in countless versions and this project aims to bring the classic Tetris experience to life using Python and the Pygame library.

In this version of Tetris, the player controls pieces called "tetrominoes," which are shapes made up of four square blocks each. These pieces fall across the playing field and the player must move and rotate them to fit them into complete rows. When a row is completed, it disappears and the player earns points. The game can be sped up by making it more difficult.

### Functional Requirements 🎯

#### Game Start 🚀

- The game must start with a main menu allowing the user to start a new game, view the high score, or exit the game.

#### Main Menu 🏠

- There must be an option to start a new game.
- There must be an option to view the high score.
- There must be an option to exit the game.

#### User Interface 🖥️

- The game must display the current score on the screen during the game.
- There must be a clear visualization of the game board with pieces (tetrominoes) and empty spaces.

#### Game Controls ⌨️

- The user must be able to move pieces left, right, and down.
- The user must be able to rotate pieces.
- The user must be able to pause and resume the game.

#### Scoring 🏆

- The game must calculate and display the score based on completed lines.
- There must be a system to save the highest score achieved and display it on the main menu.

#### Game Pause ⏸️

- The game must allow pausing and resuming without losing the current state.
- During the pause, the game must show a screen indicating that it is paused.

#### Game Over 💔

- The game must end when pieces can no longer be placed on the board.
- At the end of the game, it must display the final score and allow the user to return to the main menu.

#### Levels and Difficulty ⚙️

- The game may increase difficulty by speeding up the falling pieces as more lines are cleared.

#### Piece Generation 🎲

- The game must continuously generate random pieces (tetrominoes).

#### Collision Detection 🚧

- The game must detect and handle collisions between pieces and the board edges or between pieces.

#### Line Clearing 🧹

- The game must clear complete lines when they are fully filled and adjust the remaining pieces on the board.

### Non-Functional Requirements ⚙️

#### Performance 🚀

- The game must run smoothly without significant delays or performance drops, ensuring a responsive experience during gameplay.

#### Usability 🌟

- The interface must be intuitive and user-friendly, allowing players to easily understand controls and game mechanics.
- Menus and options should be clearly labeled and accessible.

#### Portability 🌍

- The game should be compatible with multiple operating systems that support Python, including Windows, macOS, and Linux.

#### Scalability 🔧

- The codebase should be modular and extensible, making it easy to add new features or make improvements in the future without major overhauls.

#### Aesthetics 🎨

- The game should have a clear and visually appealing design, ensuring that the game board and pieces are easy to distinguish and interact with.

#### Documentation 📚

- The code must be well-documented, including comments and explanations, to facilitate understanding and maintenance by other developers.
- User documentation should be provided to guide players on how to play the game and use its features.

#### Reliability 🔒

- The game should handle errors gracefully and not crash unexpectedly.
- It must ensure data integrity, such as saving high scores correctly.

#### Testing 🧪

- The game must be thoroughly tested to identify and fix bugs, including functional tests (e.g., controls and scoring) and usability tests (e.g., user interface and experience).

#### Security 🔐

- The game should protect user data, especially if there are features for saving high scores or user profiles.

### Requirements 📋

- **Python 3.x**
- **Pygame**

### Features ✨

- **Classic Tetris Game**: Includes traditional Tetris features such as falling pieces, piece rotation, and line clearing.
- **Intuitive User Interface**: Designed with Pygame for a user-friendly experience.
- **Pause and Resume**: Players can pause and resume the game.
- **Scoring System**: Keeps track of the player's score.

### Game 🎮
<div align="center">
  <img src="https://github.com/user-attachments/assets/a51e6280-23d6-4072-be82-3f8371f109c7" width="300" />
  <img src="https://github.com/user-attachments/assets/3ac3d8d3-fe13-4d2b-9f7b-52d3c89b62dd" width="300" />
  <img src="https://github.com/user-attachments/assets/b5ccbdf7-9b4c-495d-b63a-5484956e26f9" width="300" />
</div>

### Installation 🛠️

1. **Clone the repository**:
   ```sh
   git clone https://github.com/mateo1011s/TetrisProject.git
   cd TetrisProject
2. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt

### Usage
1. **Run the main game file**:
   ```sh
    python main.py

### Game Controls

- **Left Arrow**: Move the piece left.
- **Right Arrow**: Move the piece right.
- **Down Arrow**: Accelerate the piece's fall.
- **Up Arrow**: Rotate the piece.
- **ctrl**: Pause/Resume the game.
  


