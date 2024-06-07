# TurtleCrossingGame

![Turtle Crossing Game Demo](demo.gif)

This Turtle Crossing game is a simple arcade-style game implemented in Python using the Turtle module. The game features a turtle crossing a busy road while avoiding oncoming cars.

## Table of Contents

- [Files](#files)
- [How to Play](#how-to-play)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)

## Files

1. **main.py**: Contains the main game loop and initializes the game window. It manages player movement, car creation, collision detection, and level progression.

2. **car_manager.py**: Defines the CarManager class responsible for managing the cars in the game. It creates cars at random intervals, moves them across the screen, and increases their speed as the game progresses.

3. **player.py**: Represents the player (turtle) in the game. It handles player movement and checks if the player has reached the top edge, indicating successful crossing.

4. **scoreboard.py**: Manages the scoreboard display and level progression. It updates the level display and handles game over conditions.

## How to Play

- Use the up arrow key to move the turtle upwards.
- Avoid colliding with oncoming cars while crossing the road.
- Reach the top edge to advance to the next level.
- The game ends if the turtle collides with a car.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/turtle-crossing-game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd turtle-crossing-game
   ```

3. Run the game:

   ```bash
   python main.py
   ```

## Dependencies

- Python 3.x
- Turtle module
