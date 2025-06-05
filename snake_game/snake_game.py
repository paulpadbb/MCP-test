#!/usr/bin/env python3
"""
Snake Game Implementation
A classic snake game built with pygame.

Controls:
- Arrow keys or WASD to move
- SPACE to pause/unpause
- R to restart when game over
- ESC to quit

Features:
- Score tracking
- High score persistence
- Smooth gameplay
- Sound effects
- Game over screen
"""

import pygame
import random
import json
import os
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple

# Initialize Pygame
pygame.init()
pygame.mixer.init()

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

@dataclass
class GameConfig:
    """Game configuration settings"""
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    GRID_SIZE: int = 20
    FPS: int = 10
    
    # Colors
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    YELLOW: Tuple[int, int, int] = (255, 255, 0)
    PURPLE: Tuple[int, int, int] = (128, 0, 128)
    
    # Game settings
    INITIAL_SPEED: int = 10
    SPEED_INCREASE: float = 0.5
    HIGH_SCORE_FILE: str = "high_score.json"

class Food:
    """Food class for the snake game"""
    
    def __init__(self, config: GameConfig):
        self.config = config
        self.position = self._generate_position()
        self.color = config.RED
    
    def _generate_position(self) -> Tuple[int, int]:
        """Generate a random position for food"""
        x = random.randint(0, (self.config.WINDOW_WIDTH - self.config.GRID_SIZE) // self.config.GRID_SIZE) * self.config.GRID_SIZE
        y = random.randint(0, (self.config.WINDOW_HEIGHT - self.config.GRID_SIZE) // self.config.GRID_SIZE) * self.config.GRID_SIZE
        return (x, y)
    
    def respawn(self, snake_body: List[Tuple[int, int]]):
        """Respawn food in a position not occupied by snake"""
        while True:
            self.position = self._generate_position()
            if self.position not in snake_body:
                break
    
    def draw(self, screen):
        """Draw the food on screen"""
        pygame.draw.rect(screen, self.color, 
                        (self.position[0], self.position[1], 
                         self.config.GRID_SIZE, self.config.GRID_SIZE))

class Snake:
    """Snake class for the game"""
    
    def __init__(self, config: GameConfig):
        self.config = config
        self.body = [(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.grow_flag = False
    
    def move(self):
        """Move the snake"""
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        
        new_head = (head_x + dx * self.config.GRID_SIZE, 
                   head_y + dy * self.config.GRID_SIZE)
        
        self.body.insert(0, new_head)
        
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
    
    def grow(self):
        """Mark snake for growth"""
        self.grow_flag = True
    
    def check_collision(self) -> bool:
        """Check if snake collided with walls or itself"""
        head_x, head_y = self.body[0]
        
        # Wall collision
        if (head_x < 0 or head_x >= self.config.WINDOW_WIDTH or
            head_y < 0 or head_y >= self.config.WINDOW_HEIGHT):
            return True
        
        # Self collision
        if self.body[0] in self.body[1:]:
            return True
        
        return False
    
    def change_direction(self, new_direction: Direction):
        """Change snake direction (prevent reversing)"""
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
    
    def draw(self, screen):
        """Draw the snake on screen"""
        for i, segment in enumerate(self.body):
            color = self.config.GREEN if i == 0 else self.config.BLUE
            pygame.draw.rect(screen, color,
                           (segment[0], segment[1], 
                            self.config.GRID_SIZE, self.config.GRID_SIZE))
            
            # Add border to segments
            pygame.draw.rect(screen, self.config.WHITE,
                           (segment[0], segment[1], 
                            self.config.GRID_SIZE, self.config.GRID_SIZE), 1)

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"

class SnakeGame:
    """Main Snake Game class"""
    
    def __init__(self):
        self.config = GameConfig()
        self.screen = pygame.display.set_mode((self.config.WINDOW_WIDTH, self.config.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game - Score: 0")
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.snake = Snake(self.config)
        self.food = Food(self.config)
        
        # Game state
        self.state = GameState.PLAYING
        self.score = 0
        self.high_score = self._load_high_score()
        self.running = True
        
        # Fonts
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
    
    def _load_high_score(self) -> int:
        """Load high score from file"""
        try:
            if os.path.exists(self.config.HIGH_SCORE_FILE):
                with open(self.config.HIGH_SCORE_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except (json.JSONDecodeError, IOError):
            pass
        return 0
    
    def _save_high_score(self):
        """Save high score to file"""
        try:
            with open(self.config.HIGH_SCORE_FILE, 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except IOError:
            pass
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if self.state == GameState.PLAYING:
                    self._handle_playing_keys(event.key)
                elif self.state == GameState.PAUSED:
                    if event.key == pygame.K_SPACE:
                        self.state = GameState.PLAYING
                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        self._restart_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
    
    def _handle_playing_keys(self, key):
        """Handle keys during gameplay"""
        if key in (pygame.K_UP, pygame.K_w):
            self.snake.change_direction(Direction.UP)
        elif key in (pygame.K_DOWN, pygame.K_s):
            self.snake.change_direction(Direction.DOWN)
        elif key in (pygame.K_LEFT, pygame.K_a):
            self.snake.change_direction(Direction.LEFT)
        elif key in (pygame.K_RIGHT, pygame.K_d):
            self.snake.change_direction(Direction.RIGHT)
        elif key == pygame.K_SPACE:
            self.state = GameState.PAUSED
        elif key == pygame.K_ESCAPE:
            self.running = False
    
    def update(self):
        """Update game logic"""
        if self.state != GameState.PLAYING:
            return
        
        self.snake.move()
        
        # Check food collision
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn(self.snake.body)
            self.score += 10
            
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
                self._save_high_score()
            
            # Update window title
            pygame.display.set_caption(f"Snake Game - Score: {self.score} | High Score: {self.high_score}")
        
        # Check collisions
        if self.snake.check_collision():
            self.state = GameState.GAME_OVER
    
    def draw(self):
        """Draw everything on screen"""
        self.screen.fill(self.config.BLACK)
        
        if self.state == GameState.PLAYING:
            self._draw_game()
        elif self.state == GameState.PAUSED:
            self._draw_game()
            self._draw_pause_screen()
        elif self.state == GameState.GAME_OVER:
            self._draw_game_over()
        
        pygame.display.flip()
    
    def _draw_game(self):
        """Draw the main game elements"""
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Draw score
        score_text = self.font_small.render(f"Score: {self.score}", True, self.config.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, self.config.YELLOW)
        self.screen.blit(high_score_text, (10, 35))
    
    def _draw_pause_screen(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((self.config.WINDOW_WIDTH, self.config.WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(self.config.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_large.render("PAUSED", True, self.config.WHITE)
        pause_rect = pause_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2))
        self.screen.blit(pause_text, pause_rect)
        
        continue_text = self.font_medium.render("Press SPACE to continue", True, self.config.WHITE)
        continue_rect = continue_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(continue_text, continue_rect)
    
    def _draw_game_over(self):
        """Draw game over screen"""
        self.screen.fill(self.config.BLACK)
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, self.config.RED)
        game_over_rect = game_over_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 - 100))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = self.font_medium.render(f"Final Score: {self.score}", True, self.config.WHITE)
        score_rect = score_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 - 50))
        self.screen.blit(score_text, score_rect)
        
        # High score
        if self.score == self.high_score and self.score > 0:
            new_record_text = self.font_medium.render("NEW HIGH SCORE!", True, self.config.YELLOW)
            new_record_rect = new_record_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 - 20))
            self.screen.blit(new_record_text, new_record_rect)
        else:
            high_score_text = self.font_medium.render(f"High Score: {self.high_score}", True, self.config.YELLOW)
            high_score_rect = high_score_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 - 20))
            self.screen.blit(high_score_text, high_score_rect)
        
        # Instructions
        restart_text = self.font_small.render("Press R to restart", True, self.config.WHITE)
        restart_rect = restart_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)
        
        quit_text = self.font_small.render("Press ESC to quit", True, self.config.WHITE)
        quit_rect = quit_text.get_rect(center=(self.config.WINDOW_WIDTH // 2, self.config.WINDOW_HEIGHT // 2 + 75))
        self.screen.blit(quit_text, quit_rect)
    
    def _restart_game(self):
        """Restart the game"""
        self.snake = Snake(self.config)
        self.food = Food(self.config)
        self.score = 0
        self.state = GameState.PLAYING
        pygame.display.set_caption(f"Snake Game - Score: {self.score} | High Score: {self.high_score}")
    
    def run(self):
        """Main game loop"""
        print("Starting Snake Game!")
        print("Controls:")
        print("- Arrow keys or WASD to move")
        print("- SPACE to pause/unpause")
        print("- R to restart when game over")
        print("- ESC to quit")
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.config.FPS)
        
        pygame.quit()
        print(f"Game ended. Final score: {self.score}")
        print(f"High score: {self.high_score}")

def main():
    """Main function to run the game"""
    try:
        game = SnakeGame()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        pygame.quit()

if __name__ == "__main__":
    main()
