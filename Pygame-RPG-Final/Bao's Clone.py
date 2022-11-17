import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *
import numpy
from music_manager import MusicManager
#import coin

# freq, size, channel, buffsize
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()  # Begin pygame
#flags = FULLSCREEN | DOUBLEBUFs



# Music and Sound
soundtrack = ["background_village.wav", "battle_music.wav", "gameover.wav"]
swordtrack = [pygame.mixer.Sound("sword1.wav"), pygame.mixer.Sound("sword2.wav")]
fsound = pygame.mixer.Sound("fireball_sound.wav")
hit = pygame.mixer.Sound("enemy_hit.wav")


mmanager = MusicManager()
mmanager.playsoundtrack(soundtrack[0], -1, 0.05)

#Game Options
font_used = "arial"
num = 1

# Declaring variables to be used through the program
vec = pygame.math.Vector2
HEIGHT = 600
WIDTH = 900
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# Create the display
#displaysurface = pygame.display.set_mode((WIDTH, HEIGHT), flags, 32)
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


# light shade of the button 
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 
  
# defining a font
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16) 
text = regularfont.render('LOAD' , True , color_light)

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
    k = pygame.transform.scale(i, (180, 250))
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
    k = pygame.transform.scale(i, (180, 250))
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
    k = pygame.transform.scale(i, (180, 250))
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
    k = pygame.transform.scale(i, (180, 250))
    attack_ani_L_scaled.append(k)

# Jump animation for the right jump up
jump_ani_up = [pygame.image.load(f"Knight_0{num}__JUMP_007.png"), pygame.image.load(f"Knight_0{num}__JUMP_008.png"), pygame.image.load(f"Knight_0{num}__JUMP_009.png")]
#Resize the image
jump_ani_up_scaled = []
for i in jump_ani_up:
    k = pygame.transform.scale(i, (180, 250))
    jump_ani_up_scaled.append(k)

# Jump animation for the left jump up
jump_ani_up_L = [pygame.image.load(f"Knight_0{num}__JUMP_007_L.png"), pygame.image.load(f"Knight_0{num}__JUMP_008_L.png"), pygame.image.load(f"Knight_0{num}__JUMP_009_L.png")]
#Resize the image
jump_ani_up_L_scaled = []
for i in jump_ani_up_L:
    k = pygame.transform.scale(i, (180, 250))
    jump_ani_up_L_scaled.append(k)

# Animations for the Health Bar
health_ani = [pygame.image.load("heart0.png").convert_alpha(), pygame.image.load("heart.png").convert_alpha(),
              pygame.image.load("heart2.png").convert_alpha(), pygame.image.load("heart3.png").convert_alpha(),
              pygame.image.load("heart4.png").convert_alpha(), pygame.image.load("heart5.png").convert_alpha()]


#Game_play class
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imgbg = pygame.image.load("HomeBG.png")
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


class Item(pygame.sprite.Sprite):
      def __init__(self, itemtype):
            super().__init__()
            if itemtype == 1: self.image = pygame.image.load("heart.png").convert_alpha()
            elif itemtype == 2: self.image = pygame.image.load("coin.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.type = itemtype
            self.posx = 0
            self.posy = 0
            
      def render(self):
            self.rect.x = self.posx
            self.rect.y = self.posy
            displaysurface.blit(self.image, self.rect)

      def update(self):
            hits = pygame.sprite.spritecollide(self, Playergroup, False)
            # Code to be activated if item comes in contact with player
            if hits:
                  if player.health < 5 and self.type == 1:
                        player.health += 1
                        health.image = health_ani[player.health]
                        self.kill()
                  if self.type == 2:
                        handler.money += 1
                        self.kill()

                  

class FireBall(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.direction  = player.direction
            if self.direction == "RIGHT":
                  self.image = pygame.image.load("fireball1_R.png").convert_alpha()
            else:
                  self.image = pygame.image.load("fireball1_L.png") .convert_alpha()          
            self.rect = self.image.get_rect(center = player.pos)
            self.rect.x = player.pos.x
            self.rect.y = player.pos.y - 120
            
      def fire(self):
            player.magic_cooldown = 0
            # Runs while the fireball is still within the screen w/ extra margin
            if -10 < self.rect.x < 710:
                  if self.direction == "RIGHT":
                        self.image = pygame.image.load("fireball1_R.png").convert_alpha()
                        displaysurface.blit(self.image, self.rect)
                  else:
                        self.image = pygame.image.load("fireball1_L.png").convert_alpha()
                        displaysurface.blit(self.image, self.rect)
                        
                  if self.direction == "RIGHT":
                        self.rect.move_ip(12, 0)
                  else:
                        self.rect.move_ip(-12, 0)   
            else:
                  self.kill()
                  player.magic_cooldown = 1
                  player.attacking = False
            


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"Knight_0{num}__IDLE_000.png")
        self.image = pygame.transform.scale(self.image, (180, 250))
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((150, 580))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"

        # Movement 
        self.jumping = False
        self.running = False
        self.move_frame = 0
        self.jump_frame = 0
        #Combat
        self.attacking = False
        self.cooldown = False
        self.immune = False
        self.special = False
        self.experiance = 0
        self.attack_frame = 0
        self.health = 5
        self.magic_cooldown = 1
        self.mana = 0

        # Sound
        self.slash = 0


    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        self.acc = vec(0, 0.5)

        # Check if running or walking to slow down or speed up
        if abs(self.vel.x) > 0.25:
            self.running = True
        else:
            self.running = False
        # Return pressed key
        key_pressed = pygame.key.get_pressed()

        # Increase the velocity according to the key pressed
        if key_pressed[K_LEFT]:
            self.acc.x = -ACC
        if key_pressed[K_RIGHT]:
            self.acc.x = ACC

        # Calculate velocity
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Update character's position

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

    def gravity_check(self):
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False


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

        if self.attack_frame == 0:
            mmanager.playsound(swordtrack[self.slash], 0.05)
            self.slash += 1
            if self.slash >= 2:
                self.slash = 0

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

    def correction(self):
          # Function is used to correct an error
          # with character position on left attack frames
          if self.attack_frame == 1:
                self.pos.x -= 20
          if self.attack_frame == 10:
                self.pos.x += 20
                
    def player_hit(self):
        if self.cooldown == False:      
            self.cooldown = True # Enable the cooldown
            pygame.time.set_timer(hit_cooldown, 1000) # Resets cooldown in 1 second

            self.health = self.health - 1
            health.image = health_ani[self.health]
            
            if self.health <= 0:
                self.kill()
                mmanager.stop()
                mmanager.playsoundtrack(soundtrack[2], -1, 0.1)
                pygame.display.update()


class Bolt(pygame.sprite.Sprite):
      def __init__(self, x, y, d):
            super().__init__()
            self.image = pygame.image.load("bolt.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = x 
            self.rect.y = y + 20
            self.direction = d
            if self.direction == 0:
                  self.rect.x += 20
            else:
                  self.rect.x -= 20

      def fire(self):
            # Runs while the fireball is still within the screen w/ extra margin
            if -10 < self.rect.x < 710:
                  if self.direction == 0:
                        self.image = pygame.image.load("bolt.png").convert_alpha()
                        displaysurface.blit(self.image, self.rect)
                  else:
                        self.image = pygame.image.load("bolt.png").convert_alpha()
                        displaysurface.blit(self.image, self.rect)
                        
                  if self.direction == 0 and cursor.wait == 0:
                        self.rect.move_ip(10, 0)
                  elif self.direction == 1 and cursor.wait == 0:
                        self.rect.move_ip(-10, 0)   
            else:
                  self.kill()

            # Checks for collision with the Player
            hits = pygame.sprite.spritecollide(self, Playergroup, False)
            if hits:
                  player.player_hit()
                  self.kill()
            

class Enemy2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()   
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.wait = 0
        self.wait_status = False
        self.turning = 0

        self.direction = random.randint(0,1) # 0 for Right, 1 for Left
        self.vel.x = random.randint(2,6) / 3  # Randomised velocity of the generated enemy
        self.mana = random.randint(2, 3)  # Randomised mana amount obtained upon

        if self.direction == 0: self.image = pygame.image.load("enemy2.png").convert_alpha()
        if self.direction == 1: self.image = pygame.image.load("enemy2_L.png").convert_alpha()
        self.rect = self.image.get_rect()  

        # Sets the intial position of the enemy
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 440
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 440


      def turn(self):
            if self.wait > 0:
                self.wait -= 1
                return
            elif int(self.wait) <= 0:
                self.turning = 0
        
            if (self.direction):
                  self.direction = 0
                  self.image = pygame.image.load("enemy2.png").convert_alpha()
            else:
                  self.direction = 1
                  self.image = pygame.image.load("enemy2_L.png").convert_alpha()

      def move(self):
        if cursor.wait == 1: return
        if self.turning == 1:
              self.turn()
              return
        
        # Causes the enemy to change directions upon reaching the end of screen    
        if self.pos.x >= (WIDTH-20):
              self.direction = 1
        elif self.pos.x <= 0:
              self.direction = 0
        #print(self.wait)
            
        # Updates positon with new values
        if self.wait > 60:
              self.wait_status = True
        elif int(self.wait) <= 0:
              self.wait_status = False

        if (self.direction_check()):
              self.turn()
              self.wait = 90
              self.turning = 1
                    

        if self.wait_status == True:
              rand_num = numpy.random.uniform(0, 60) # inc/dec to dec/inc chance
              if int(rand_num) == 30:
                    bolt = Bolt(self.pos.x, self.pos.y, self.direction)
                    Bolts.add(bolt)
              self.wait -= 1 # increase to lower waiting period
                             #(will also lower chance of firing a bolt)
              
        elif self.direction == 0:
            self.pos.x += self.vel.x
            self.wait += self.vel.x
        elif self.direction == 1:
            self.pos.x -= self.vel.x
            self.wait += self.vel.x
            
        self.rect.topleft = self.pos # Updates rect

      def direction_check(self):
            if (player.pos.x - self.pos.x < 0 and self.direction == 0):
                  return 1
            if (player.pos.x - self.pos.x > 0 and self.direction == 1):
                  return 1


      def update(self):
            # Checks for collision with the Player
            hits = pygame.sprite.spritecollide(self, Playergroup, False)

            # Checks for collision with Fireballs
            f_hits = pygame.sprite.spritecollide(self, Fireballs, False)

            # Activates upon either of the two expressions being true
            if hits and player.attacking == True or f_hits:
                  self.kill()
                  mmanager.playsound(hit, 0.05)
                  handler.dead_enemy_count += 1
                  
                  if player.mana < 100: player.mana += self.mana # Release mana
                  player.experiance += 1   # Release expeiriance
                  
                  rand_num = numpy.random.uniform(0, 100)
                  item_no = 0
                  if rand_num >= 0 and rand_num <= 5:  # 1 / 20 chance for an item (health) drop
                        item_no = 1
                  elif rand_num > 5 and rand_num <= 15:
                        item_no = 2

                  if item_no != 0:
                        # Add Item to Items group
                        item = Item(item_no)
                        Items.add(item)
                        # Sets the item location to the location of the killed enemy
                        item.posx = self.pos.x
                        item.posy = self.pos.y 

      def render(self):
            # Displayed the enemy on screen
            displaysurface.blit(self.image, self.rect)



      
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()     
        self.pos = vec(0,0)
        self.vel = vec(0,0)

        self.direction = random.randint(0,1) # 0 for Right, 1 for Left
        self.vel.x = random.randint(2,6) / 2  # Randomised velocity of the generated enemy
        self.mana = random.randint(1, 3)  # Randomised mana amount obtained upon    

        # Sets the intial position of the enemy
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 440
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 440


      def move(self):
        if cursor.wait == 1: return
        
        # Causes the enemy to change directions upon reaching the end of screen    
        if self.pos.x >= (WIDTH-20):
              self.direction = 1
        elif self.pos.x <= 0:
              self.direction = 0

        # Updates positon with new values     
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
            
        self.rect.topleft = self.pos # Updates rect
               
      def update(self):
            # Checks for collision with the Player
            hits = pygame.sprite.spritecollide(self, Playergroup, False)

            # Checks for collision with Fireballs
            f_hits = pygame.sprite.spritecollide(self, Fireballs, False)

            # Activates upon either of the two expressions being true
            if hits and player.attacking == True or f_hits:
                  self.kill()
                  mmanager.playsound(hit, 0.05)
                  handler.dead_enemy_count += 1
                  
                  if player.mana < 100: player.mana += self.mana # Release mana
                  player.experiance += 1   # Release expeiriance
                  
                  rand_num = numpy.random.uniform(0, 100)
                  item_no = 0
                  if rand_num >= 0 and rand_num <= 5:  # 1 / 20 chance for an item (health) drop
                        item_no = 1
                  elif rand_num > 5 and rand_num <= 15:
                        item_no = 2

                  if item_no != 0:
                        # Add Item to Items group
                        item = Item(item_no)
                        Items.add(item)
                        # Sets the item location to the location of the killed enemy
                        item.posx = self.pos.x
                        item.posy = self.pos.y
                 
            # If collision has occured and player not attacking, call the "hit" func.            
            elif hits and player.attacking == False:
                  player.player_hit()
                  
      def render(self):
            # Displayed the enemy on screen
            displaysurface.blit(self.image, self.rect)


class Castle(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.hide = False
            self.image = pygame.image.load("castle.png").convert_alpha()

      def update(self):
            if self.hide == False:
                  displaysurface.blit(self.image, (600, 290))


class EventHandler():
      def __init__(self):
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.battle = False
            self.enemy_generation = pygame.USEREVENT + 2
            self.enemy_generation2 = pygame.USEREVENT + 3
            self.stage = 1
            self.money = 0
            self.world = 0
            

            #Method 1 (Only for one level)
            self.stage_enemies = []
            for x in range(1, 21):
                  self.stage_enemies.append(int((x ** 2 / 2) + 1))

            #Method 2 (Both levels)
            #self.stage_enemies = [ [0]*20 for i in range(1, 3)]
            #print(self.stage_enemies)
            #for i in range(0,2):
                  #for j in range(0, 20):
                        #self.stage_enemies[i][j] = (int(   ( j ** 2/2 ) / 2 )  * (i + 1) + 1 )

            print(self.stage_enemies)

            
            
      def stage_handler(self):
            # Code for the Tkinter stage selection window
            self.root = Tk()
            self.root.geometry('200x170')
            
            button1 = Button(self.root, text = "Skyward Dungeon", width = 18, height = 2,
                            command = self.world1)
            button2 = Button(self.root, text = "Gerudo Dungeon", width = 18, height = 2,
                            command = self.world2)
            button3 = Button(self.root, text = "Hell Dungeon", width = 18, height = 2,
                            command = self.world3)
             
            button1.place(x = 40, y = 15)
            button2.place(x = 40, y = 65)
            button3.place(x = 40, y = 115)
            
            self.root.mainloop()
      
      def world1(self):
            self.root.destroy()
            background.imgbg = pygame.image.load("Map1BG.png").convert_alpha()
            ground.imgground = pygame.image.load("map1ground.png").convert_alpha()
            pygame.time.set_timer(self.enemy_generation, 2000)
            button.imgdisp = 1
            self.world = 1
            castle.hide = True
            self.battle = True
            
            mmanager.playsoundtrack(soundtrack[1], -1, 0.05)
            

      def world2(self):
            self.root.destroy()
            background.imgbg = pygame.image.load("Map2BG.png").convert_alpha()
            ground.imgground = pygame.image.load("desert_ground.png").convert_alpha()
            pygame.time.set_timer(self.enemy_generation2, 2000)
            self.world = 2
            button.imgdisp = 1
            castle.hide = True
            self.battle = True

            mmanager.playsoundtrack(soundtrack[1], -1, 0.05)
 

      def world3(self):
            self.root.destroy()
            background.imgbg = pygame.image.load("Map3BG.png").convert_alpha()
            ground.imgground = pygame.image.load("desert_ground.png").convert_alpha()
            pygame.time.set_timer(self.enemy_generation2, 2000)
            self.world = 3
            button.imgdisp = 1
            castle.hide = True
            self.battle = True

            mmanager.playsoundtrack(soundtrack[1], -1, 0.05)
            
 
      def next_stage(self):  # Code for when the next stage is clicked            
            self.stage += 1
            #print("Stage: "  + str(self.stage))
            self.enemy_count = 0
            self.dead_enemy_count = 0
            if self.world == 1:
                  pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))
            elif self.world == 2:
                  pygame.time.set_timer(self.enemy_generation2, 2200 - (30 * self.stage))

      def update(self):
            if self.dead_enemy_count == self.stage_enemies[self.stage - 1]:
                  self.dead_enemy_count = 0
                  stage_display.clear = True
                  stage_display.stage_clear()

      def home(self):
            # Reset Battle code
            pygame.time.set_timer(self.enemy_generation, 0)
            pygame.time.set_timer(self.enemy_generation2, 0)
            self.battle = False
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.stage = 1
            self.world = 0

            # Destroy any enemies or items lying around
            for group in Enemies, Items:
                  for entity in group:
                        entity.kill()
            
            # Bring back normal backgrounds
            castle.hide = False
            background.imgbg = pygame.image.load("HomeBG.png").convert_alpha()
            ground.imgground = pygame.image.load("map1ground.png").convert_alpha()

      


class HealthBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("heart5.png").convert_alpha()

      def render(self):
            displaysurface.blit(self.image, (10,10))


class StageDisplay(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.text = headingfont.render("STAGE: " + str(handler.stage), True, color_dark)
            self.rect = self.text.get_rect()
            self.posx = -100
            self.posy = 100
            self.display = False
            self.clear = False

      def move_display(self):
            # Create the text to be displayed
            self.text = headingfont.render("STAGE: " + str(handler.stage), True, color_dark)
            if self.posx < 720:
                  self.posx += 6
                  displaysurface.blit(self.text, (self.posx, self.posy))
            else:
                  self.display = False
                  self.posx = -100
                  self.posy = 100


      def stage_clear(self):
            button.imgdisp = 0
            self.text = headingfont.render("STAGE CLEAR!", True , color_dark)
            
            if self.posx < 720:
                  self.posx += 10
                  displaysurface.blit(self.text, (self.posx, self.posy))
            else:
                  self.clear = False
                  self.posx = -100
                  self.posy = 100
                  
     

class StatusBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((90, 66))
            self.rect = self.surf.get_rect(center = (500, 10))
            self.exp = player.experiance
            
      def update_draw(self):
            # Create the text to be displayed
            text1 = smallerfont.render("STAGE: " + str(handler.stage) , True , color_white)
            text2 = smallerfont.render("EXP: " + str(player.experiance) , True , color_white)
            text3 = smallerfont.render("MANA: " + str(player.mana) , True , color_white)
            text4 = smallerfont.render("FPS: " + str(int(FPS_CLOCK.get_fps())) , True , color_white)
            self.exp = player.experiance

            # Draw the text to the status bar
            displaysurface.blit(text1, (585, 7))
            displaysurface.blit(text2, (585, 22))
            displaysurface.blit(text3, (585, 37))
            displaysurface.blit(text4, (585, 52))

class Cursor(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("cursor.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.wait = 0

      def pause(self):
            if self.wait == 1:
                  self.wait = 0
            else:
                  self.wait = 1

      def hover(self):
          if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 345:
                pygame.mouse.set_visible(False)
                cursor.rect.center = pygame.mouse.get_pos()  # update position 
                displaysurface.blit(cursor.image, cursor.rect)
          else:
                pygame.mouse.set_visible(True)
                

class PButton(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.vec = vec(700, 20)
            self.imgdisp = 0

      def render(self, num):
            if (num == 0):
                  self.image = pygame.image.load("home_small.png").convert_alpha()
            elif (num == 1):
                  if cursor.wait == 0:
                        self.image = pygame.image.load("pause_small.png").convert_alpha()
                  else:
                        self.image = pygame.image.load("play_small.png").convert_alpha()
                                    
            displaysurface.blit(self.image, self.vec) 


Enemies = pygame.sprite.Group()

player = Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

background = Background()
ground = Ground()
cursor = Cursor()
button = PButton()

ground_group = pygame.sprite.Group()
ground_group.add(ground)

castle = Castle()
handler = EventHandler()
health = HealthBar()
stage_display = StageDisplay()
status_bar = StatusBar()
Fireballs = pygame.sprite.Group()
Items = pygame.sprite.Group()
Bolts = pygame.sprite.Group()

hit_cooldown = pygame.USEREVENT + 1

while 1:
    player.gravity_check()
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == hit_cooldown:
            player.cooldown = False
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == handler.enemy_generation:
            if handler.enemy_count < handler.stage_enemies[handler.stage - 1]:
                  enemy = Enemy()
                  Enemies.add(enemy)
                  handler.enemy_count += 1
        if event.type == handler.enemy_generation2:
            if handler.enemy_count < handler.stage_enemies[handler.stage - 1]:
                  if handler.enemy_count % 2:
                        enemy = Enemy2()
                  else:
                        enemy = Enemy()
                  Enemies.add(enemy)
                  handler.enemy_count += 1

        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
               if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 345:
                    if button.imgdisp == 1:
                          cursor.pause()
                    elif button.imgdisp == 0:
                          handler.home()


        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN and cursor.wait == 0:
            if event.key == pygame.K_m and player.magic_cooldown == 1:
                  if player.mana >= 6:
                        player.mana -= 6
                        player.attacking = True
                        fireball = FireBall()
                        Fireballs.add(fireball)
                        mmanager.playsound(fsound, 0.3)
            if event.key == pygame.K_n:
                  if handler.battle == True and len(Enemies) == 0:
                        handler.next_stage()
                        stage_display = StageDisplay()
                        stage_display.display = True
            if event.key == pygame.K_e and 630 < player.rect.x < 730:
                handler.stage_handler()
            if event.key == pygame.K_UP:
                player.jump()
            if event.key == pygame.K_SPACE:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True      


    # Player related functions
    player.move()
    player.update()
    if player.attacking == True:
          player.attack() 

    # Display and Background related functions         
    background.render()
    ground.render()
    button.render(button.imgdisp)
    cursor.hover()

    # Render stage display
    if stage_display.display == True:
          stage_display.move_display()
    if stage_display.clear == True:
          stage_display.stage_clear()

    # Rendering Sprites
    castle.update()
    if player.health > 0:
        displaysurface.blit(player.image, player.rect)
    health.render()

    # Status bar update and render
    displaysurface.blit(status_bar.surf, (580, 5))
    status_bar.update_draw()
    handler.update()
    
    for i in Items:
          i.render()
          i.update() 
   
    for ball in Fireballs:
          ball.fire()
    for bolt in Bolts:
          bolt.fire()

    for entity in Enemies:
          entity.update()
          entity.move()
          entity.render()

    pygame.display.update()      
    FPS_CLOCK.tick(FPS)
