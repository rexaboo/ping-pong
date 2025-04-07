from pygame import *
font.init()

color_back = (0, 225, 255)
width_w = 600
height_w = 500
window = display.set_mode((width_w, height_w))





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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < width_w - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < width_w - 80:
            self.rect.y += self.speed



racket1 = Player('racket.png', 30, 200, 90, 150, 4)
racket2 = Player('racket.png', 520, 200, 90, 150, 4)
ball = GameSprite('ball.png', 200, 200, 70, 40, 10)

font = font.SysFont('comicsans', 45)

lose_1 = font.render('FIRST PLAYER LOSE!', True, (106, 179, 61))
lose_2 = font.render('SECOND PLAYER LOSE!', True, (106, 179, 61))

lol_x = 3
lol_y =3

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill(color_back)
        racket1.update1()
        racket2.update2()
        ball.rect.x += lol_x
        ball.rect.y += lol_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            lol_x *= -1
            lol_y *= 1
        if ball.rect.y > height_w - 50 or ball.rect.y < 0:
            lol_y *= -1
        if ball.rect.x  < 0:
            finish = True
            window.blit(lose_1, (150, 335))
            game = True
        if ball.rect.x > width_w:
            finish = True   
            window.blit(lose_2, (150, 335))
            game = True
    

        ball.reset()

        racket1.reset()
        racket2.reset()
    clock.tick(FPS)
    display.update()
