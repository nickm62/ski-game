import pygame
import random
import sys
from PIL import Image


pygame.init()


GAME_WIDTH = 600
GAME_HEIGHT = 800
GAME_SPEED = 60
SCORE = 0


screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


def load_gif_frames(gif_path):
    gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frame = gif.copy()
            frame = frame.convert("RGBA")
            frame = frame.resize((GAME_WIDTH, GAME_HEIGHT))
            frames.append(pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode))
            gif.seek(len(frames))

    except EOFError:
        pass
    return frames


class SkiGuy:
    def __init__(self):
        global SCORE
        self.x = 50
        self.y = 50
        self.speed = 7
        self.size = 75
        print(self.speed)
        self.image = pygame.image.load("skiguyv2.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
        
    def draw(self):
        
        screen.blit(self.image, (self.x, self.y))
        

    def movement(self):
        global SCORE
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if self.x <= 0:
            self.x = self.x + self.speed
        if self.x >= 550:
            self.x = self.x - self.speed

class Tree:
    def __init__(self):
        self.y = random.randrange(850, 5000)
        self.x = 50
        self.speed = 5
        self.size = 75
        self.image = pygame.image.load("tree.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def draw(self):
        
        screen.blit(self.image, (self.x, self.y))
        
    
    def movement(self):
        global SCORE
        self.speed = 5 + SCORE // 5
        RUNNING = True
        if RUNNING:
            self.y = self.y - self.speed
        if self.y <= 0:
            self.x = random.randrange(0, 550)
            self.y = random.randrange(850, 1000)
            SCORE += 1

class NpcDown:
    def __init__(self):
        self.y = random.randrange(850, 5000)
        self.x = 50
        self.speed = 5
        self.size = 75
        self.image1 = pygame.image.load("npcdown.png")
        self.image1 = pygame.transform.scale(self.image1, (self.size, self.size))
        self.image2 = pygame.image.load("npcdown2.png")
        self.image2 = pygame.transform.scale(self.image2, (self.size, self.size))

    def draw(self):
        randsuit = random.randrange(1, 2)
        if randsuit == 1:
            screen.blit(self.image1, (self.x, self.y))
        else:
            screen.blit(self.image2, (self.x, self.y))
        
    
    def movement(self):
        global SCORE
        self.speed = 5 + SCORE // 5
        RUNNING = True
        if RUNNING:
            self.y = self.y - self.speed
        if self.y <= 0:
            self.x = random.randrange(0, 550)
            self.y = random.randrange(850, 1000)
            SCORE += 1

def check_collision(player, tree):
    
    tree_collision_box = pygame.Rect(tree.x + 10, tree.y + 10, tree.size - 20, tree.size - 20)

    player_collision_box = pygame.Rect(player.x, player.y, player.size, player.size)

    return player_collision_box.colliderect(tree_collision_box)


def npc_check_collision(player, NpcDown):

    NpcDown_collision_box = pygame.Rect(NpcDown.x + 10, NpcDown.y + 10, NpcDown.size - 20, NpcDown.size - 20)

    player_collision_box = pygame.Rect(player.x, player.y, player.size, player.size)

    return player_collision_box.colliderect(NpcDown_collision_box)



    


def show_menu():
    menu_on = True
    gif_frames = load_gif_frames("snow2.gif")  
    gif_frame_count = len(gif_frames)
    current_frame = 0
    frame_delay = 5  
    frame_counter = 0

    
    while menu_on:
        screen.fill((255, 255, 255))
        screen.blit(gif_frames[current_frame], (0, 0))
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            current_frame = (current_frame + 1) % gif_frame_count
        
        banner_image = pygame.image.load("banner.png.png")
        banner_image = pygame.transform.scale(banner_image, (400, 300))
        screen.blit(banner_image, (100, 100))
        font = pygame.font.Font(None, 36)
        start_text = font.render("Press ENTER to Start", True, (0, 0, 0))
        screen.blit(start_text, ((GAME_WIDTH - start_text.get_width()) // 2, 550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_on = False
        pygame.display.flip()

def game_over():
    game_over_active = True

    while game_over_active:
        screen.fill((255, 255, 255))
        score_board2 = pygame.font.Font(None, 36).render(f"Score: {SCORE}", True, (0, 0, 0))
        screen.blit(score_board2, (300, GAME_HEIGHT - 200))

        game_over_text = pygame.font.Font(None, 36).render("Game Over", True, (0, 0, 0))
        screen.blit(game_over_text, (200, GAME_HEIGHT - 550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over_active = False
        pygame.display.flip()

def npccolactive():
    global SCORE
    
    if npc_check_collision(player, npc):
        
        print(f"Game Over! Final Score: {SCORE}")
        player.x = 300
        treeobj.y = random.randrange(850, 3000)
        treeobj2.y = random.randrange(850, 3000)
        treeobj3.y = random.randrange(850, 3000)
        game_over()
        SCORE = 0







player = SkiGuy()
treeobj = Tree()
treeobj2 = Tree()
treeobj3 = Tree()
npc = NpcDown()
show_menu()

caption = pygame.display.set_caption(f"score: {SCORE}")
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    
    screen.fill((255, 255, 255))
    player.draw()
    player.movement()
    treeobj.draw()
    treeobj.movement()
    treeobj2.draw()
    treeobj2.movement()
    treeobj3.draw()
    treeobj3.movement()

    if SCORE >= 25:
        npc.draw()
        npc.movement()
        npccolactive()


    
    if check_collision(player, treeobj) or \
       check_collision(player, treeobj2) or \
       check_collision(player, treeobj3):
       
        print(f"Game Over! Final Score: {SCORE}")
        player.x = 300
        treeobj.y = random.randrange(850, 3000)
        treeobj2.y = random.randrange(850, 3000)
        treeobj3.y = random.randrange(850, 3000)
        game_over()
        SCORE = 0


    
    if check_collision(treeobj, treeobj2):
        treeobj.x + random.randrange(50, 100)
        treeobj2.y + random.randrange(50, 100)
    
    if check_collision(treeobj, treeobj3):
        treeobj.x + random.randrange(50, 100)
        treeobj3.y + random.randrange(50, 100)
    
    if check_collision(treeobj2, treeobj3):
        treeobj2.x + random.randrange(50, 100)
        treeobj3.y + random.randrange(50, 100)
    
    score_board = pygame.font.Font(None, 36).render(f"Score: {SCORE}", True, (0, 0, 0))
    screen.blit(score_board, (10, GAME_HEIGHT - 40))
    speed_board = pygame.font.Font(None, 36).render(f"Speed: {treeobj.speed}", True, (0, 0, 0))
    screen.blit(speed_board, (400, GAME_HEIGHT - 40))

    pygame.display.set_caption("Ski Game")
    pygame.display.flip()
    pygame.time.Clock().tick(GAME_SPEED)
    

    
        






pygame.quit()
sys.exit()

