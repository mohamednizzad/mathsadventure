import pygame
import sys
from levels import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        # Load fonts - try to use more playful fonts if available
        try:
            self.font = pygame.font.SysFont('Comic Sans MS', 32)
            self.small_font = pygame.font.SysFont('Comic Sans MS', 24)
            self.title_font = pygame.font.SysFont('Comic Sans MS', 48)
        except:
            self.font = pygame.font.SysFont('Arial', 32)
            self.small_font = pygame.font.SysFont('Arial', 24)
            self.title_font = pygame.font.SysFont('Arial', 48)
        
        # Enhanced color palette
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (76, 175, 80)
        self.RED = (244, 67, 54)
        self.BLUE = (33, 150, 243)
        self.PURPLE = (156, 39, 176)
        self.BACKGROUND_TOP = (179, 229, 252)  # Light blue
        self.BACKGROUND_BOTTOM = (255, 255, 255)
        self.GOLD = (255, 193, 7)
        
        # Game state
        self.current_grade = 1
        self.score = 0
        self.lives = 3
        self.answer_input = ""
        self.feedback = ""
        self.feedback_color = self.BLACK
        self.feedback_scale = 1.0  # For animation
        
        # Load heart image for lives or create a heart shape
        self.heart_points = [
            (0, -4), (2, -2), (4, -4), (4, -2), (2, 4), (0, 2),
            (-2, 4), (-4, -2), (-4, -4), (-2, -2)
        ]
        self.heart_points = [(x * 3 + 20, y * 3 + 80) for x, y in self.heart_points]
        
        # Initialize first problem
        self.new_problem()
    
    def new_problem(self):
        """Generate a new math problem based on current grade"""
        self.problem = generate_problem(self.current_grade)
        self.answer_input = ""
        self.feedback = ""
    
    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.answer_input:
                    self.check_answer()
                elif event.key == pygame.K_BACKSPACE:
                    self.answer_input = self.answer_input[:-1]
                elif event.unicode.isnumeric() or event.unicode == '-':
                    self.answer_input += event.unicode
    
    def check_answer(self):
        """Check if the provided answer is correct"""
        try:
            user_answer = int(self.answer_input)
            if user_answer == self.problem.answer:
                self.score += 10 * self.current_grade
                self.feedback = "Correct!"
                self.feedback_color = self.GREEN
                self.feedback_scale = 1.5  # Start larger for "pop" effect
                
                # Increase grade if score threshold reached
                if self.score >= self.current_grade * 100 and self.current_grade < 5:
                    self.current_grade += 1
                    self.feedback = f"Level Up! Now at Grade {self.current_grade}"
                    self.feedback_color = self.GOLD
                    self.feedback_scale = 2.0  # Even bigger for level up
            else:
                self.lives -= 1
                self.feedback = "Wrong answer!"
                self.feedback_color = self.RED
                self.feedback_scale = 1.3  # Slightly larger for wrong answer
                
                if self.lives <= 0:
                    self.game_over()
            
            # Draw one frame with the current feedback
            self.draw()
            pygame.display.flip()
            pygame.time.wait(500)  # Show feedback for half a second
            
            self.new_problem()
            
        except ValueError:
            self.feedback = "Please enter a valid number"
            self.feedback_color = self.RED
            self.feedback_scale = 1.2
    
    def game_over(self):
        """Handle game over state"""
        waiting = True
        alpha = 0
        fade_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        fade_surface.fill(self.BLACK)
        
        while alpha < 128:  # Fade to semi-transparent black
            self.draw()  # Draw the game screen underneath
            fade_surface.set_alpha(alpha)
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            alpha += 2
            pygame.time.wait(5)
        
        # Create game over panel
        panel_width = 400
        panel_height = 300
        panel_x = (self.screen.get_width() - panel_width) // 2
        panel_y = (self.screen.get_height() - panel_height) // 2
        
        while waiting:
            # Draw the base game screen and fade overlay
            self.draw()
            fade_surface.set_alpha(128)
            self.screen.blit(fade_surface, (0, 0))
            
            # Draw game over panel
            pygame.draw.rect(self.screen, self.WHITE, 
                           (panel_x, panel_y, panel_width, panel_height))
            pygame.draw.rect(self.screen, self.BLUE, 
                           (panel_x, panel_y, panel_width, panel_height), 4)
            
            # Draw game over text
            game_over_text = self.title_font.render("Game Over!", True, self.RED)
            score_text = self.font.render(f"Final Score: {self.score}", True, self.BLACK)
            grade_text = self.font.render(f"Reached Grade: {self.current_grade}", True, self.BLUE)
            restart_text = self.small_font.render("Press R to restart or Q to quit", True, self.PURPLE)
            
            # Center all text in the panel
            self.screen.blit(game_over_text, 
                           game_over_text.get_rect(centerx=panel_x + panel_width // 2, 
                                                 top=panel_y + 40))
            self.screen.blit(score_text, 
                           score_text.get_rect(centerx=panel_x + panel_width // 2, 
                                             top=panel_y + 120))
            self.screen.blit(grade_text, 
                           grade_text.get_rect(centerx=panel_x + panel_width // 2, 
                                             top=panel_y + 170))
            self.screen.blit(restart_text, 
                           restart_text.get_rect(centerx=panel_x + panel_width // 2, 
                                               top=panel_y + 220))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__(self.screen)
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
    
    def update(self):
        """Update game state"""
        self.clock.tick(60)
    
    def draw_gradient_background(self):
        """Draw a gradient background"""
        height = self.screen.get_height()
        for i in range(height):
            progress = i / height
            color = [int(self.BACKGROUND_TOP[j] * (1 - progress) + self.BACKGROUND_BOTTOM[j] * progress) 
                    for j in range(3)]
            pygame.draw.line(self.screen, color, (0, i), (self.screen.get_width(), i))
    
    def draw_heart(self, x, y, filled=True):
        """Draw a heart shape at the specified position"""
        points = [(px + x - 20, py - 80 + y) for px, py in self.heart_points]
        if filled:
            pygame.draw.polygon(self.screen, self.RED, points)
        pygame.draw.polygon(self.screen, (200, 0, 0), points, 2)
    
    def draw(self):
        """Draw the game screen"""
        # Draw gradient background
        self.draw_gradient_background()
        
        # Draw decorative header
        pygame.draw.rect(self.screen, self.BLUE, (0, 0, self.screen.get_width(), 120))
        pygame.draw.rect(self.screen, self.PURPLE, (0, 115, self.screen.get_width(), 10))
        
        # Draw grade and score with enhanced styling
        grade_text = self.small_font.render(f"Grade: {self.current_grade}", True, self.WHITE)
        score_text = self.small_font.render(f"Score: {self.score}", True, self.WHITE)
        
        self.screen.blit(grade_text, (20, 20))
        self.screen.blit(score_text, (20, 50))
        
        # Draw lives as hearts
        for i in range(3):
            self.draw_heart(60 + i * 30, 80, i < self.lives)
        
        # Draw problem with a background panel
        panel_rect = pygame.Rect(250, 150, 300, 250)
        pygame.draw.rect(self.screen, self.WHITE, panel_rect)
        pygame.draw.rect(self.screen, self.BLUE, panel_rect, 3)
        
        # Draw problem text
        problem_text = self.font.render(str(self.problem), True, self.BLACK)
        problem_rect = problem_text.get_rect(centerx=panel_rect.centerx, top=panel_rect.top + 30)
        self.screen.blit(problem_text, problem_rect)
        
        # Draw answer input with a box
        input_rect = pygame.Rect(panel_rect.left + 20, problem_rect.bottom + 20, 
                               panel_rect.width - 40, 40)
        pygame.draw.rect(self.screen, self.WHITE, input_rect)
        pygame.draw.rect(self.screen, self.BLACK, input_rect, 2)
        
        answer_text = self.font.render(f"Answer: {self.answer_input}", True, self.BLACK)
        answer_rect = answer_text.get_rect(centerx=input_rect.centerx, centery=input_rect.centery)
        self.screen.blit(answer_text, answer_rect)
        
        # Draw feedback with animation
        if self.feedback:
            feedback_text = self.font.render(self.feedback, True, self.feedback_color)
            feedback_rect = feedback_text.get_rect(centerx=panel_rect.centerx, 
                                                 top=input_rect.bottom + 20)
            
            # Apply scale animation
            scaled_surface = pygame.transform.scale(
                feedback_text,
                (int(feedback_text.get_width() * self.feedback_scale),
                 int(feedback_text.get_height() * self.feedback_scale))
            )
            scaled_rect = scaled_surface.get_rect(center=feedback_rect.center)
            self.screen.blit(scaled_surface, scaled_rect)
            
            # Update scale for animation
            target_scale = 1.0
            self.feedback_scale += (target_scale - self.feedback_scale) * 0.1
            if abs(self.feedback_scale - target_scale) < 0.01:
                self.feedback_scale = target_scale