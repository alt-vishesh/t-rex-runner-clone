#T-Rex Runner Clone
import pygame

import random

import sys



# Initialize Pygame

pygame.init()



# Game Constants

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 400

FPS = 60



# Colors (RGB)

WHITE = (247, 247, 247)

GREY = (83, 83, 83)

GREEN = (34, 139, 34)

GROUND_COLOR = (150, 150, 150)



# Setup Screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("T-Rex Runner Clone")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)



class Dino:

    def __init__(self):

        self.x = 50

        self.y = 300

        self.width = 40

        self.height = 50

        self.is_jumping = False

        self.jump_strength = 14

        self.gravity = 0.7

        self.velocity_y = 0

        self.ground_y = 300



    def jump(self):

        if not self.is_jumping:

            self.is_jumping = True

            self.velocity_y = -self.jump_strength



    def update(self):

        if self.is_jumping:

            self.y += self.velocity_y

            self.velocity_y += self.gravity

            

            # Check if landed

            if self.y >= self.ground_y:

                self.y = self.ground_y

                self.is_jumping = False

                self.velocity_y = 0



    def draw(self, surface):

        # Drawing the Dino as a sleek grey rectangle

        pygame.draw.rect(surface, GREY, (self.x, self.y, self.width, self.height))

        # Eye to give it a little personality

        pygame.draw.rect(surface, WHITE, (self.x + 25, self.y + 10, 5, 5))



    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)





class Cactus:

    def __init__(self, speed):

        self.x = SCREEN_WIDTH + random.randint(50, 300)

        self.width = random.choice([20, 30, 40])  # Varying widths

        self.height = random.randint(40, 70)       # Varying heights

        self.y = 350 - self.height

        self.speed = speed



    def update(self):

        self.x -= self.speed



    def draw(self, surface):

        # Drawing the cactus as a green rectangle

        pygame.draw.rect(surface, GREEN, (self.x, self.y, self.width, self.height))



    def get_rect(self):

        return pygame.Rect(self.x, self.y, self.width, self.height)





def main():

    dino = Dino()

    obstacles = []

    score = 0

    game_speed = 7

    spawn_timer = 0

    game_over = False



    while True:

        # 1. Event Handling

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:

                    if game_over:

                        # Restart the game

                        dino = Dino()

                        obstacles = []

                        score = 0

                        game_speed = 7

                        game_over = False

                    else:

                        dino.jump()



        if not game_over:

            # 2. Update Game Objects

            dino.update()

            

            # Increase difficulty over time

            game_speed += 0.002

            score += 1



            # Manage obstacles

            spawn_timer -= 1

            if len(obstacles) == 0 or (obstacles[-1].x < SCREEN_WIDTH - 300 and spawn_timer <= 0):

                if random.random() < 0.02: # Small randomness to spawning

                    obstacles.append(Cactus(game_speed))

                    spawn_timer = 40 # Prevent immediate overlapping



            for obstacle in obstacles[:]:

                obstacle.speed = game_speed # Keep speeds synchronized

                obstacle.update()

                

                # Check for collisions

                if dino.get_rect().colliderect(obstacle.get_rect()):

                    game_over = True



                # Remove off-screen obstacles

                if obstacle.x + obstacle.width < 0:

                    obstacles.remove(obstacle)



        # 3. Drawing Everything

        screen.fill(WHITE)

        

        # Draw Ground Line

        pygame.draw.line(screen, GROUND_COLOR, (0, 350), (SCREEN_WIDTH, 350), 3)



        # Draw Entities

        dino.draw(screen)

        for obstacle in obstacles:

            obstacle.draw(screen)



        # Draw UI text

        score_text = font.render(f"Score: {score // 5}", True, GREY)

        screen.blit(score_text, (SCREEN_WIDTH - 150, 20))



        if game_over:

            game_over_text = font.render("G A M E   O V E R", True, GREY)

            restart_text = font.render("Press SPACE to Restart", True, GREY)

            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30))

            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 10))



        pygame.display.flip()

        clock.tick(FPS)



if __name__ == "__main__":

    main()
