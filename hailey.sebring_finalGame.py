import pygame
import random
import sys  # Import the sys module

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frog Adventure Game")

# Load assets
background_img = pygame.Surface((WIDTH, HEIGHT))
background_img.fill((34, 139, 34))  # Placeholder green background

frog_img = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(frog_img, (0, 255, 0), (25, 25), 25)  # Placeholder frog

fly_img = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.circle(fly_img, (255, 0, 0), (15, 15), 15)  # Placeholder fly

ribbet_sound = pygame.mixer.Sound("ribbet.wav")
bg_music = pygame.mixer.Sound("background_music.wav")

# Start background music
bg_music.play(-1)

# Define game states
INTRO, GAMEPLAY, PAUSE, QUIT = "intro", "gameplay", "pause", "quit"

# Define fonts
font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(frog_img, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.angle = 0
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        if keys[pygame.K_UP]:
            rad_angle = pygame.math.radians(self.angle)
            self.rect.x += int(5 * pygame.math.cos(rad_angle))
            self.rect.y -= int(5 * pygame.math.sin(rad_angle))

        self.rect.x %= WIDTH
        self.rect.y %= HEIGHT
        self.image = pygame.transform.rotate(frog_img, self.angle)

class Fly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(fly_img, (30, 30))
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.angle = random.randint(-45, 45)
        self.speed = 2

    def update(self):
        rad_angle = pygame.math.radians(self.angle)
        self.rect.x += int(self.speed * pygame.math.cos(rad_angle))
        self.rect.y -= int(self.speed * pygame.math.sin(rad_angle))
        
        self.rect.x %= WIDTH
        self.rect.y %= HEIGHT
        self.angle += random.randint(-45, 45)
        self.image = pygame.transform.rotate(fly_img, self.angle)

class Game:
    def __init__(self):
        self.state = INTRO
        self.frog = Frog()
        self.flies = pygame.sprite.Group([Fly() for _ in range(3)])
        self.all_sprites = pygame.sprite.Group([self.frog] + list(self.flies))
        self.score = 0
        self.time_left = 60

    def reset(self):
        self.__init__()

    def draw_intro(self):
        screen.fill(WHITE)
        title_text = font.render("Frog Adventure Game", True, (0, 0, 0))
        instructions_text = font.render("Press any key to start", True, (0, 0, 0))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))

    def draw_gameplay(self):
        screen.blit(background_img, (0, 0))
        self.all_sprites.draw(screen)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        timer_text = font.render(f"Time: {int(self.time_left)}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (WIDTH - 150, 10))

    def draw_pause(self):
        pause_text = font.render("Paused", True, WHITE)
        reset_text = font.render("Press R to Reset", True, WHITE)
        quit_text = font.render("Press Q to Quit", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(reset_text, (WIDTH // 2 - reset_text.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 50))

    def check_collisions(self):
        for fly in self.flies:
            if pygame.sprite.collide_rect(self.frog, fly):
                ribbet_sound.play()
                fly.rect.topleft = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
                fly.angle = random.randint(-45, 45)
                self.score += 1

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1 / 60
        else:
            self.state = PAUSE

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.state == INTRO and event.type == pygame.KEYDOWN:
                    self.state = GAMEPLAY
                if self.state == PAUSE:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.reset()
                            self.state = GAMEPLAY
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()

            keys = pygame.key.get_pressed()
            if self.state == GAMEPLAY:
                self.all_sprites.update(keys)
                self.check_collisions()
                self.update_timer()

            screen.fill(WHITE)
            if self.state == INTRO:
                self.draw_intro()
            elif self.state == GAMEPLAY:
                self.draw_gameplay()
            elif self.state == PAUSE:
                self.draw_pause()

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
