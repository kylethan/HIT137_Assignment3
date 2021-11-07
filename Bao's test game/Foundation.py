#Import Libraries
import pygame
from pygame.locals import*
import sys
import random
from tkinter import filedialog
from tkinter import *

#Game Options
font_used = "arial"
num = 1

#Game Resources
# Run animation for the RIGHT for three characters
#Char 1
run_ani_R = [pygame.image.load(f"Knight_0{num}__IDLE_000.png"), pygame.image.load(f"Knight_0{num}__RUN_000.png"), pygame.image.load(f"Knight_0{num}__RUN_001.png"),
             pygame.image.load(f"Knight_0{num}__RUN_002.png"), pygame.image.load(f"Knight_0{num}__RUN_003.png"), pygame.image.load(f"Knight_0{num}__RUN_004.png"),
             pygame.image.load(f"Knight_0{num}__RUN_005.png"), pygame.image.load(f"Knight_0{num}__RUN_006.png"),
             pygame.image.load(f"Knight_0{num}__RUN_007.png"), pygame.image.load(f"Knight_0{num}__RUN_008.png"),
             pygame.image.load(f"Knight_0{num}__RUN_009.png")]
#Resize the image
run_ani_R_scaled = []
for i in run_ani_R:
    k = pygame.transform.scale(i, (450, 250))
    run_ani_R_scaled.append(k)

# Run animation for the LEFT
run_ani_L = [pygame.image.load("Knight_01__IDLE_000_L.png"), pygame.image.load("Knight_01__RUN_000_L.png"), pygame.image.load("Knight_01__RUN_001_L.png"),
             pygame.image.load("Knight_01__RUN_002_L.png"), pygame.image.load("Knight_01__RUN_003_L.png"), pygame.image.load("Knight_01__RUN_004_L.png"),
             pygame.image.load("Knight_01__RUN_005_L.png"), pygame.image.load("Knight_01__RUN_006_L.png"),
             pygame.image.load("Knight_01__RUN_007_L.png"), pygame.image.load("Knight_01__RUN_008_L.png"),
             pygame.image.load("Knight_01__RUN_009_L.png")]
#Resize the image
run_ani_L_scaled = []
for i in run_ani_L:
    k = pygame.transform.scale(i, (450, 250))
    run_ani_L_scaled.append(k)

# Attack animation for the RIGHT
attack_ani_R = [pygame.image.load("Knight_01__IDLE_000.png"), pygame.image.load("Knight_01__ATTACK_000.png"),
                pygame.image.load("Knight_01__ATTACK_001.png"), pygame.image.load("Knight_01__ATTACK_002.png"),
                pygame.image.load("Knight_01__ATTACK_003.png"), pygame.image.load("Knight_01__ATTACK_004.png"),
                pygame.image.load("Knight_01__ATTACK_005.png"), pygame.image.load("Knight_01__ATTACK_006.png"),
                pygame.image.load("Knight_01__ATTACK_007.png"), pygame.image.load("Knight_01__ATTACK_008.png"),
                pygame.image.load("Knight_01__ATTACK_009.png"), pygame.image.load("Knight_01__IDLE_000.png")]

#Resize the image
attack_ani_R_scaled = []
for i in attack_ani_R:
    k = pygame.transform.scale(i, (450, 250))
    attack_ani_R_scaled.append(k)

# Attack animation for the LEFT
attack_ani_L = [pygame.image.load("Knight_01__IDLE_000_L.png"), pygame.image.load("Knight_01__ATTACK_000_L.png"),
                pygame.image.load("Knight_01__ATTACK_001_L.png"), pygame.image.load("Knight_01__ATTACK_002_L.png"),
                pygame.image.load("Knight_01__ATTACK_003_L.png"), pygame.image.load("Knight_01__ATTACK_004_L.png"),
                pygame.image.load("Knight_01__ATTACK_005_L.png"), pygame.image.load("Knight_01__ATTACK_006_L.png"),
                pygame.image.load("Knight_01__ATTACK_007_L.png"), pygame.image.load("Knight_01__ATTACK_008_L.png"),
                pygame.image.load("Knight_01__ATTACK_009_L.png"), pygame.image.load("Knight_01__IDLE_000_L.png")]
#Resize the image
attack_ani_L_scaled = []
for i in attack_ani_L:
    k = pygame.transform.scale(i, (450, 250))
    attack_ani_L_scaled.append(k)

# Jump animation for the right jump up
jump_ani_up = [pygame.image.load("Knight_01__JUMP_007.png"), pygame.image.load("Knight_01__JUMP_008.png"), pygame.image.load("Knight_01__JUMP_009.png")]
#Resize the image
jump_ani_up_scaled = []
for i in jump_ani_up:
    k = pygame.transform.scale(i, (450, 250))
    jump_ani_up_scaled.append(k)

# Jump animation for the left jump up
jump_ani_up_L = [pygame.image.load("Knight_01__JUMP_007_L.png"), pygame.image.load("Knight_01__JUMP_008_L.png"), pygame.image.load("Knight_01__JUMP_009_L.png")]
#Resize the image
jump_ani_up_L_scaled = []
for i in jump_ani_up_L:
    k = pygame.transform.scale(i, (450, 250))
    jump_ani_up_L_scaled.append(k)



#Start the game
pygame.init()
vec = pygame.math.Vector2
HEIGHT = 600
WIDTH = 900
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

#required class
class Game:
    def __init__(self):
        self.font_name = pygame.font.match_font(font_used)
        pygame.display.set_caption("Welcome to the World of Endless Fights")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #Add welcome background
        self.welcome_background = pygame.image.load("welcome_wallpaper.png")
        self.screen.blit(self.welcome_background, (0, 0))
    #Print text to the screen knowing attributes, including position
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    def welcome(self):
        self.draw_text("Armor and Earth", 60, "Black", WIDTH/2, HEIGHT/8)
        self.draw_text("Choose your Knight by Pressing 1, 2 or 3", 26, "Black", WIDTH/2, HEIGHT/2.7)
        pygame.display.flip()
        self.wait_for_press()

     #Press key to start playing and skip waiting screen
    def wait_for_press(self):
        self.waiting = True
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.waiting = False

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imgbg = pygame.image.load("map1background1.png")
        self.jumping = False

    def render(self):
        displaysurface.blit(self.imgbg, (0, 0))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imgground = pygame.image.load("map1ground.png")
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))

    def render(self):
        displaysurface.blit(self.imgground, (0, 500))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"Knight_0{num}__IDLE_000.png")
        self.image = pygame.transform.scale(self.image, (450, 250))
        self.rect = self.image.get_rect()
        # Position and direction
        self.vx = 0
        self.pos = vec((150, 580))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        # Movement
        self.jumping = False
        self.running = False
        self.move_frame = 0
        self.jump_frame = 0
        #Combat:
        self.attacking = False
        self.attack_frame = 0

    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        self.acc = vec(0, 0.5)

        # Check if running or walking to slow down or speed up
        if abs(self.vel.x) > 0.25:
            self.running = True
        else:
            self.running = False
        #Return pressed key
        key_pressed = pygame.key.get_pressed()

        #Increase the velocity according to the key pressed
        if key_pressed[K_LEFT]:
            self.acc.x = -ACC
        if key_pressed[K_RIGHT]:
            self.acc.x = ACC

        #Calculate velocity
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc #Update character's position

        # This causes character warping from one point of the screen to the other
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos  # Update rect with new pos

        # Move the character to the next frame if conditions are met
        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_ani_R_scaled[self.move_frame]
                self.direction = "RIGHT"
            else:
                self.image = run_ani_L_scaled[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

            # Returns to base frame if standing still and incorrect frame is showing
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_ani_R_scaled[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_ani_L_scaled[self.move_frame]

    def update(self):
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        if player.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
        # Return to base frame if at end of movement sequence, this equals the number of animation pictures
        if self.move_frame > 10:
            self.move_frame = 0
            return

    def attack(self):
        # If attack frame has reached end of sequence, return to base frame
        if self.attack_frame > 11:
            self.attack_frame = 0
            self.attacking = False

        # Check direction for correct animation to display
        if self.direction == "RIGHT":
            self.image = attack_ani_R_scaled[self.attack_frame]
        elif self.direction == "LEFT":
            self.image = attack_ani_L_scaled[self.attack_frame]

            # Update the current attack frame
        self.attack_frame += 1

    def jump(self):
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        if hits:
            self.vel.y = -15
        # If jump frame has reached end of sequence, return to base frame
        if self.jump_frame > 2:
            self.jump_frame = 0
            self.jumping = False
        # Check direction for correct animation to display
        if self.direction == "RIGHT":
            self.image = jump_ani_up_scaled[self.jump_frame]
        if self.direction == "LEFT":
            self.image = jump_ani_up_L_scaled[self.jump_frame]
        # Update the current attack frame
        self.jump_frame += 1

    def gravity_check(self):
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

game_start = Game()
background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
player = Player()
game_start.welcome()

while game_start.waiting == False:
    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

            # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
            if event.key == pygame.K_SPACE:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True

    #Render the map
    background.render()
    ground.render()
    player.update()
    if player.attacking == True:
        player.attack()
    player.move()
    displaysurface.blit(player.image, player.rect)
    pygame.display.update()
    FPS_CLOCK.tick(FPS)
    player.gravity_check()

