import pytest
import pygame
from src.game import Game

@pytest.fixture
def game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return Game(screen)

def test_game_initialization(game):
    assert game.current_grade == 1
    assert game.score == 0
    assert game.lives == 3
    assert game.answer_input == ""
    assert game.feedback == ""
    assert game.feedback_scale == 1.0  # Test new feedback scale initialization

def test_correct_answer(game):
    initial_score = game.score
    game.problem.answer = 42
    game.answer_input = "42"
    game.check_answer()
    assert game.score > initial_score
    assert game.feedback == "Correct!"
    assert game.feedback_color == game.GREEN
    assert game.feedback_scale == 1.5  # Test feedback animation scale

def test_wrong_answer(game):
    initial_lives = game.lives
    game.problem.answer = 42
    game.answer_input = "24"
    game.check_answer()
    assert game.lives == initial_lives - 1
    assert game.feedback == "Wrong answer!"
    assert game.feedback_color == game.RED
    assert game.feedback_scale == 1.3  # Test feedback animation scale

def test_invalid_answer(game):
    game.answer_input = "abc"
    game.check_answer()
    assert game.feedback == "Please enter a valid number"
    assert game.feedback_color == game.RED
    assert game.feedback_scale == 1.2  # Test feedback animation scale

def test_grade_progression(game):
    # Set score just below threshold for level up
    game.score = 99
    game.current_grade = 1
    game.problem.answer = 42
    game.answer_input = "42"
    game.check_answer()
    assert game.current_grade == 2
    assert game.feedback == "Level Up! Now at Grade 2"
    assert game.feedback_color == game.GOLD  # Test gold color for level up
    assert game.feedback_scale == 2.0  # Test larger scale for level up

def test_game_over(game):
    game.lives = 1
    game.problem.answer = 42
    game.answer_input = "24"
    game.check_answer()
    assert game.lives == 0

def test_ui_colors(game):
    # Test that all required colors are defined
    assert hasattr(game, 'WHITE')
    assert hasattr(game, 'BLACK')
    assert hasattr(game, 'GREEN')
    assert hasattr(game, 'RED')
    assert hasattr(game, 'BLUE')
    assert hasattr(game, 'PURPLE')
    assert hasattr(game, 'GOLD')
    assert hasattr(game, 'BACKGROUND_TOP')
    assert hasattr(game, 'BACKGROUND_BOTTOM')

def test_heart_shape(game):
    # Test that heart points are properly initialized
    assert hasattr(game, 'heart_points')
    assert len(game.heart_points) > 0
    # Test that points are properly transformed
    assert all(isinstance(point, tuple) and len(point) == 2 for point in game.heart_points)