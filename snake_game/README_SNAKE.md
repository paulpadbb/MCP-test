# 🐍 Snake Game

A classic Snake game implementation built with Python and Pygame.

## 🎮 Features

- **Classic Gameplay**: Navigate the snake to eat food and grow longer
- **Score Tracking**: Keep track of your current score and high score
- **Persistent High Score**: High scores are saved between game sessions
- **Smooth Controls**: Responsive controls with WASD or arrow keys
- **Pause Functionality**: Pause and resume the game anytime
- **Game Over Screen**: Clear game over state with restart option
- **Collision Detection**: Wall and self-collision detection
- **Visual Feedback**: Colorful graphics with distinct snake head and body

## 🕹️ Controls

| Key | Action |
|-----|--------|
| Arrow Keys / WASD | Move the snake |
| SPACE | Pause/Unpause game |
| R | Restart game (when game over) |
| ESC | Quit game |

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/paulpadbb/MCP-test.git
   cd MCP-test/snake_game
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**:
   ```bash
   python snake_game.py
   ```

## 🎯 How to Play

1. **Objective**: Control the snake to eat red food items
2. **Growth**: Each food item consumed makes the snake grow longer
3. **Scoring**: Earn 10 points for each food item eaten
4. **Avoid**: Don't hit the walls or the snake's own body
5. **High Score**: Try to beat your personal best!

## 🛠️ Technical Details

### Project Structure
```
snake_game/
├── snake_game.py      # Main game implementation
├── requirements.txt   # Python dependencies
└── README_SNAKE.md   # This documentation
```

### Key Components

- **Snake Class**: Handles snake movement, growth, and collision detection
- **Food Class**: Manages food positioning and rendering
- **GameConfig**: Centralized configuration for colors, sizes, and game settings
- **Game States**: Menu, Playing, Paused, and Game Over states
- **High Score Persistence**: Saves high scores to `high_score.json`

### Configuration

The game can be easily customized by modifying the `GameConfig` class:

- **Window Size**: 800x600 pixels (default)
- **Grid Size**: 20 pixels per grid cell
- **FPS**: 10 frames per second
- **Colors**: Customizable color scheme
- **Speed**: Adjustable game speed

## 🎨 Customization

You can easily customize the game by modifying the `GameConfig` class in `snake_game.py`:

```python
@dataclass
class GameConfig:
    WINDOW_WIDTH: int = 800        # Game window width
    WINDOW_HEIGHT: int = 600       # Game window height
    GRID_SIZE: int = 20           # Size of each grid cell
    FPS: int = 10                 # Game speed (frames per second)
    
    # Colors (RGB values)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)  # Snake body
    RED: Tuple[int, int, int] = (255, 0, 0)    # Food
    # ... more colors
```

## 🐛 Troubleshooting

### Common Issues

1. **Pygame not found**:
   ```bash
   pip install pygame
   ```

2. **Permission errors on high score file**:
   - Make sure the game directory is writable
   - The game will work without high score persistence if file operations fail

3. **Game runs too fast/slow**:
   - Modify the `FPS` value in `GameConfig`
   - Higher values = faster game, lower values = slower game

4. **Window doesn't appear**:
   - Check if you have a display available
   - Try running in a different environment

## 🎮 Game Screenshots

*Game in progress:*
- Green square with white border: Snake head
- Blue squares with white border: Snake body
- Red square: Food item
- Score and high score displayed in top-left corner

*Game Over screen:*
- Final score display
- High score tracking
- Restart and quit options

## 🚀 Future Enhancements

Potential improvements for future versions:

- [ ] Sound effects and background music
- [ ] Multiple difficulty levels
- [ ] Power-ups and special food items
- [ ] Multiplayer support
- [ ] Different game modes (time trial, survival, etc.)
- [ ] Improved graphics and animations
- [ ] Mobile touch controls
- [ ] Online leaderboards

## 🤝 Contributing

This is part of the MCP-test repository demonstrating the Notion + Cursor AI workflow. Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📄 License

This project is part of the MCP-test repository. See the main repository for license information.

## 🎉 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Created as part of the Notion + Cursor AI workflow demonstration
- Classic Snake game concept

---

**Enjoy playing Snake! 🐍🎮**
