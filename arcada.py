import pygame

win_width = 900
win_height = 700
FPS = 60
move_right = False
move_left = False
view_right = True
x_fon = 0

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('АРКАДА')
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_pic, img_x, img_y, img_width, img_height, img_speed):
        self.image = pygame.transform.scale(pygame.image.load(img_pic), (img_width, img_height))
        self.rect = self.image.get_rect()
        self.rect.x = img_x
        self.rect.y = img_y
        self.speed = img_speed

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def right(self):
        #global x_fon
        self.rect.x -= 5  
        
    def left(self):
        #global x_fon
        self.rect.x += 5  
            
class Player(GameSprite):
    def right(self):
        self.rect.x += 5
    def left(self):
        self.rect.x -= 5
        
scene = GameSprite('wood.jpg', 0, 0, 4000, 700, 0)
hero = Player('hero.png', 250, 420, 70, 120, 5)

game = True
finish = False

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                if not view_right:
                    hero.image = pygame.transform.flip(hero.image, True, False)
                    view_right = True
                move_right = True  
            if e.key == pygame.K_LEFT:
                if view_right:
                    hero.image = pygame.transform.flip(hero.image, True, False)
                    view_right = False      
                move_left = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                move_right = False  
            if e.key == pygame.K_LEFT:
                move_left = False
            
    if move_right:
        if x_fon < 3680:
            x_fon += 5
            if x_fon >= 0 and x_fon <= 3100:
                scene.right()
            if x_fon < 0 or x_fon > 3100:
                hero.right()
    
    if move_left:
        if x_fon > -240:
            x_fon -= 5
            if x_fon >= 0 and x_fon <= 3100:
                scene.left()
            if x_fon < 0 or x_fon > 3100:
                hero.left()
    
    scene.reset()
    hero.reset()

    pygame.display.update()
    clock.tick(FPS)