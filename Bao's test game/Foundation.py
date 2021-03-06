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
#Game_Parameters
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

#Welcome_to_the_game
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
        global num
        self.waiting = True
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        num = 1
                        self.waiting = False
                    elif event.key == pygame.K_2:
                        num = 2
                        self.waiting = False
                    elif event.key == pygame.K_3:
                        num = 3
                        self.waiting = False

game_start = Game()
game_start.welcome()

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
run_ani_L = [pygame.image.load(f"Knight_0{num}__IDLE_000_L.png"), pygame.image.load(f"Knight_0{num}__RUN_000_L.png"), pygame.image.load(f"Knight_0{num}__RUN_001_L.png"),
             pygame.image.load(f"Knight_0{num}__RUN_002_L.png"), pygame.image.load(f"Knight_0{num}__RUN_003_L.png"), pygame.image.load(f"Knight_0{num}__RUN_004_L.png"),
             pygame.image.load(f"Knight_0{num}__RUN_005_L.png"), pygame.image.load(f"Knight_0{num}__RUN_006_L.png"),
             pygame.image.load(f"Knight_0{num}__RUN_007_L.png"), pygame.image.load(f"Knight_0{num}__RUN_008_L.png"),
             pygame.image.load(f"Knight_0{num}__RUN_009_L.png")]
#Resize the image
run_ani_L_scaled = []
for i in run_ani_L:
    k = pygame.transform.scale(i, (450, 250))
    run_ani_L_scaled.append(k)

# Attack animation for the RIGHT
attack_ani_R = [pygame.image.load(f"Knight_0{num}__IDLE_000.png"), pygame.image.load(f"Knight_0{num}__ATTACK_000.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_001.png"), pygame.image.load(f"Knight_0{num}__ATTACK_002.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_003.png"), pygame.image.load(f"Knight_0{num}__ATTACK_004.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_005.png"), pygame.image.load(f"Knight_0{num}__ATTACK_006.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_007.png"), pygame.image.load(f"Knight_0{num}__ATTACK_008.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_009.png"), pygame.image.load(f"Knight_0{num}__IDLE_000.png")]

#Resize the image
attack_ani_R_scaled = []
for i in attack_ani_R:
    k = pygame.transform.scale(i, (450, 250))
    attack_ani_R_scaled.append(k)

# Attack animation for the LEFT
attack_ani_L = [pygame.image.load(f"Knight_0{num}__IDLE_000_L.png"), pygame.image.load(f"Knight_0{num}__ATTACK_000_L.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_001_L.png"), pygame.image.load(f"Knight_0{num}__ATTACK_002_L.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_003_L.png"), pygame.image.load(f"Knight_0{num}__ATTACK_004_L.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_005_L.png"), pygame.image.load(f"Knight_0{num}__ATTACK_006_L.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_007_L.png"), pygame.image.load(f"Knight_0{num}__ATTACK_008_L.png"),
                pygame.image.load(f"Knight_0{num}__ATTACK_009_L.png"), pygame.image.load(f"Knight_0{num}__IDLE_000_L.png")]
#Resize the image
attack_ani_L_scaled = []
for i in attack_ani_L:
    k = pygame.transform.scale(i, (450, 250))
    attack_ani_L_scaled.append(k)

# Jump animation for the right jump up
jump_ani_up = [pygame.image.load(f"Knight_0{num}__JUMP_007.png"), pygame.image.load(f"Knight_0{num}__JUMP_008.png"), pygame.image.load(f"Knight_0{num}__JUMP_009.png")]
#Resize the image
jump_ani_up_scaled = []
for i in jump_ani_up:
    k = pygame.transform.scale(i, (450, 250))
    jump_ani_up_scaled.append(k)

# Jump animation for the left jump up
jump_ani_up_L = [pygame.image.load(f"Knight_0{num}__JUMP_007_L.png"), pygame.image.load(f"Knight_0{num}__JUMP_008_L.png"), pygame.image.load(f"Knight_0{num}__JUMP_009_L.png")]
#Resize the image
jump_ani_up_L_scaled = []
for i in jump_ani_up_L:
    k = pygame.transform.scale(i, (450, 250))
    jump_ani_up_L_scaled.append(k)

#Game_play class
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
        self.cooldown = False
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

    def player_hit(self):
        if self.cooldown == False:      
            self.cooldown = True # Enable the cooldown
            pygame.time.set_timer(hit_cooldown, 1000) # Resets cooldown in 1 second
            
            print("hit")
            pygame.display.update()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()     
        self.pos = vec(0,0)
        self.vel = vec(0,0)

        self.direction = random.randint(0,1) # 0 for Right, 1 for Left
        self.vel.x = random.randint(2,6) / 2  # Randomized velocity of the generated enemy 

        # Sets the intial position of the enemy
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 440
        if self.direction == 1:
            self.pos.x = 500
            self.pos.y = 440
    
    def move(self):
        
        # Causes the enemy to change directions upon reaching the end of screen    
        if self.pos.x >= (WIDTH-20):
                self.direction = 1
        elif self.pos.x <= 0:
                self.direction = 0

        # Updates position with new values     
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
 
        self.rect.center = self.pos # Updates rect

    def update(self):
      # Checks for collision with the Player
      hits = pygame.sprite.spritecollide(self, Playergroup, False)
 
      # Activates upon either of the two expressions being true
      if hits and player.attacking == True:
            self.kill()
            #print("Enemy killed")
 
      # If collision has occured and player not attacking, call "hit" function            
      elif hits and player.attacking == False:
            player.player_hit()

    def render(self):
        # Displayed the enemy on screen
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))

class Castle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hide = False
        self.image = pygame.image.load("castle.png")

    def update(self):
        if self.hide == False:
                displaysurface.blit(self.image, (600, 290))
    
class EventHandler():
    def __init__(self):
        self.enemy_count = 0
        self.battle = False
        self.enemy_generation = pygame.USEREVENT + 1
        self.stage = 1
        self.stage_enemies = []
        for x in range(1, 21):
            self.stage_enemies.append(int((x ** 2 / 2) + 1))

            
    def stage_handler(self):
        # Code for the Tkinter stage selection window
        self.root = Tk()
        self.root.geometry('200x170')
            
        button1 = Button(self.root, text = "Twilight Dungeon", width = 18, height = 2,
                        command = self.world1)
        button2 = Button(self.root, text = "Skyward Dungeon", width = 18, height = 2,
                        command = self.world2)
        button3 = Button(self.root, text = "Hell Dungeon", width = 18, height = 2,
                        command = self.world3)
            
        button1.place(x = 40, y = 15)
        button2.place(x = 40, y = 65)
        button3.place(x = 40, y = 115)
            
        self.root.mainloop()

    def world1(self):
        
        pygame.time.set_timer(self.enemy_generation, 2000)
        castle.hide = True
        self.battle = True

    def world2(self):
        self.battle = True
        # Empty for now
    
    def world3(self):
        self.battle = True    
        # Empty for now

    def next_stage(self):  # Code for when the next stage is clicked            
        self.stage += 1
        self.enemy_count = 0
        print("Stage: "  + str(self.stage))
        pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))

background = Background()
ground = Ground()
enemy = Enemy()

Enemies = pygame.sprite.Group()

ground_group = pygame.sprite.Group()
ground_group.add(ground)

player = Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

castle = Castle()
handler = EventHandler()

hit_cooldown = pygame.USEREVENT + 1

while game_start.waiting == False:
    for event in pygame.event.get():
        if event.type == hit_cooldown:
            player.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == handler.enemy_generation:
            if handler.enemy_count < handler.stage_enemies[handler.stage - 1]:
                enemy = Enemy()
                Enemies.add(enemy)
                handler.enemy_count += 1

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                  if handler.battle == True and len(Enemies) == 0:
                        handler.next_stage()
            if event.key == pygame.K_e and 450 < player.rect.x < 550:
                handler.world1()
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
    castle.update()
    displaysurface.blit(player.image, player.rect)

    # enemy.update()
    # enemy.move()
    # enemy.render()
    for entity in Enemies:
      entity.update()
      entity.move()
      entity.render()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
    player.gravity_check()

