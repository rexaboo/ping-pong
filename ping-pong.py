from pygame import *
font.init()

color_back = (0, 225, 255)
width_w = 600
height_w = 500
window = display.set_mode((width_w, height_w))
window.fill(color_back)




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < width_w - 80:
            self.rect.x += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < width_w - 80:
            self.rect.x += self.speed



racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

font = font.SysFont('comicsans', 45)

lose_1 = font.render('FIRST PLAYER LOSE!', True, (106, 179, 61))
lose_2 = font.render('SECOND PLAYER LOSE!', True, (106, 179, 61))

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    racket1.reset()
    racket2.reset()
    ball.reset()


    clock.tick()
    display.update()
