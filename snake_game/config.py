#!/usr/bin/env python3
"""
Configuration file for Snake Game
This file contains all the configurable settings for the game.
"""

from dataclasses import dataclass
from typing import Tuple

@dataclass
class GameSettings:
    """Main game configuration class"""
    
    # Window settings
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    WINDOW_TITLE: str = "Snake Game"
    
    # Grid settings
    GRID_SIZE: int = 20
    GRID_WIDTH: int = WINDOW_WIDTH // GRID_SIZE
    GRID_HEIGHT: int = WINDOW_HEIGHT // GRID_SIZE
    
    # Game timing
    FPS: int = 10
    INITIAL_SPEED: int = 10
    SPEED_INCREASE_RATE: float = 0.5
    
    # Scoring
    POINTS_PER_FOOD: int = 10
    BONUS_THRESHOLD: int = 100  # Points needed for speed increase
    
    # Files
    HIGH_SCORE_FILE: str = "high_score.json"
    SETTINGS_FILE: str = "game_settings.json"
    
    # Colors (RGB tuples)
    COLOR_BLACK: Tuple[int, int, int] = (0, 0, 0)
    COLOR_WHITE: Tuple[int, int, int] = (255, 255, 255)
    COLOR_GREEN: Tuple[int, int, int] = (0, 255, 0)
    COLOR_DARK_GREEN: Tuple[int, int, int] = (0, 200, 0)
    COLOR_RED: Tuple[int, int, int] = (255, 0, 0)
    COLOR_BLUE: Tuple[int, int, int] = (0, 100, 255)
    COLOR_YELLOW: Tuple[int, int, int] = (255, 255, 0)
    COLOR_PURPLE: Tuple[int, int, int] = (128, 0, 128)
    COLOR_ORANGE: Tuple[int, int, int] = (255, 165, 0)
    COLOR_GRAY: Tuple[int, int, int] = (128, 128, 128)
    
    # Theme colors
    BACKGROUND_COLOR: Tuple[int, int, int] = COLOR_BLACK
    SNAKE_HEAD_COLOR: Tuple[int, int, int] = COLOR_GREEN
    SNAKE_BODY_COLOR: Tuple[int, int, int] = COLOR_BLUE
    FOOD_COLOR: Tuple[int, int, int] = COLOR_RED
    TEXT_COLOR: Tuple[int, int, int] = COLOR_WHITE
    SCORE_COLOR: Tuple[int, int, int] = COLOR_YELLOW
    BORDER_COLOR: Tuple[int, int, int] = COLOR_WHITE
    
    # Sound settings
    ENABLE_SOUND: bool = True
    MASTER_VOLUME: float = 0.7
    
    # Game mechanics
    ALLOW_REVERSE: bool = False  # Allow snake to reverse direction
    WRAP_AROUND: bool = False    # Allow snake to wrap around screen edges
    SHOW_GRID: bool = False      # Show grid lines
    
@dataclass
class DifficultySettings:
    """Difficulty level configurations"""
    
    # Easy mode
    EASY_FPS: int = 8
    EASY_SPEED_INCREASE: float = 0.3
    
    # Normal mode (default)
    NORMAL_FPS: int = 10
    NORMAL_SPEED_INCREASE: float = 0.5
    
    # Hard mode
    HARD_FPS: int = 15
    HARD_SPEED_INCREASE: float = 0.8
    
    # Expert mode
    EXPERT_FPS: int = 20
    EXPERT_SPEED_INCREASE: float = 1.0

@dataclass
class KeyBindings:
    """Configurable key bindings for the game"""
    
    # Movement keys
    MOVE_UP: list = None
    MOVE_DOWN: list = None
    MOVE_LEFT: list = None
    MOVE_RIGHT: list = None
    
    # Control keys
    PAUSE: list = None
    RESTART: list = None
    QUIT: list = None
    
    def __post_init__(self):
        # Initialize default key bindings
        import pygame
        
        self.MOVE_UP = [pygame.K_UP, pygame.K_w]
        self.MOVE_DOWN = [pygame.K_DOWN, pygame.K_s]
        self.MOVE_LEFT = [pygame.K_LEFT, pygame.K_a]
        self.MOVE_RIGHT = [pygame.K_RIGHT, pygame.K_d]
        
        self.PAUSE = [pygame.K_SPACE, pygame.K_p]
        self.RESTART = [pygame.K_r]
        self.QUIT = [pygame.K_ESCAPE, pygame.K_q]

def get_default_settings() -> GameSettings:
    """Get default game settings"""
    return GameSettings()

def get_difficulty_settings(difficulty: str = "normal") -> DifficultySettings:
    """Get settings for specified difficulty level"""
    settings = DifficultySettings()
    
    if difficulty.lower() == "easy":
        return DifficultySettings(
            EASY_FPS=settings.EASY_FPS,
            NORMAL_FPS=settings.EASY_FPS,
            HARD_FPS=settings.EASY_FPS,
            EXPERT_FPS=settings.EASY_FPS,
            EASY_SPEED_INCREASE=settings.EASY_SPEED_INCREASE,
            NORMAL_SPEED_INCREASE=settings.EASY_SPEED_INCREASE,
            HARD_SPEED_INCREASE=settings.EASY_SPEED_INCREASE,
            EXPERT_SPEED_INCREASE=settings.EASY_SPEED_INCREASE
        )
    elif difficulty.lower() == "hard":
        return DifficultySettings(
            EASY_FPS=settings.HARD_FPS,
            NORMAL_FPS=settings.HARD_FPS,
            HARD_FPS=settings.HARD_FPS,
            EXPERT_FPS=settings.HARD_FPS,
            EASY_SPEED_INCREASE=settings.HARD_SPEED_INCREASE,
            NORMAL_SPEED_INCREASE=settings.HARD_SPEED_INCREASE,
            HARD_SPEED_INCREASE=settings.HARD_SPEED_INCREASE,
            EXPERT_SPEED_INCREASE=settings.HARD_SPEED_INCREASE
        )
    elif difficulty.lower() == "expert":
        return DifficultySettings(
            EASY_FPS=settings.EXPERT_FPS,
            NORMAL_FPS=settings.EXPERT_FPS,
            HARD_FPS=settings.EXPERT_FPS,
            EXPERT_FPS=settings.EXPERT_FPS,
            EASY_SPEED_INCREASE=settings.EXPERT_SPEED_INCREASE,
            NORMAL_SPEED_INCREASE=settings.EXPERT_SPEED_INCREASE,
            HARD_SPEED_INCREASE=settings.EXPERT_SPEED_INCREASE,
            EXPERT_SPEED_INCREASE=settings.EXPERT_SPEED_INCREASE
        )
    
    # Default to normal
    return settings

def get_key_bindings() -> KeyBindings:
    """Get default key bindings"""
    return KeyBindings()

# Color themes
COLOR_THEMES = {
    "classic": {
        "background": (0, 0, 0),
        "snake_head": (0, 255, 0),
        "snake_body": (0, 100, 255),
        "food": (255, 0, 0),
        "text": (255, 255, 255),
        "score": (255, 255, 0)
    },
    "dark": {
        "background": (20, 20, 20),
        "snake_head": (100, 255, 100),
        "snake_body": (50, 150, 255),
        "food": (255, 100, 100),
        "text": (200, 200, 200),
        "score": (255, 200, 0)
    },
    "neon": {
        "background": (0, 0, 40),
        "snake_head": (0, 255, 255),
        "snake_body": (255, 0, 255),
        "food": (255, 255, 0),
        "text": (255, 255, 255),
        "score": (0, 255, 0)
    },
    "retro": {
        "background": (50, 50, 0),
        "snake_head": (0, 200, 0),
        "snake_body": (0, 150, 0),
        "food": (200, 200, 0),
        "text": (255, 255, 255),
        "score": (255, 255, 0)
    }
}

def apply_theme(settings: GameSettings, theme_name: str = "classic") -> GameSettings:
    """Apply a color theme to game settings"""
    if theme_name not in COLOR_THEMES:
        theme_name = "classic"
    
    theme = COLOR_THEMES[theme_name]
    
    settings.BACKGROUND_COLOR = theme["background"]
    settings.SNAKE_HEAD_COLOR = theme["snake_head"]
    settings.SNAKE_BODY_COLOR = theme["snake_body"]
    settings.FOOD_COLOR = theme["food"]
    settings.TEXT_COLOR = theme["text"]
    settings.SCORE_COLOR = theme["score"]
    
    return settings
