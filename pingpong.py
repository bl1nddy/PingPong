from pygame import *

init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket1(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

class Racket2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("background.png"), (win_width, win_height))

player1 = Racket1('racket.png', 0, 350, 10)
player2 = Racket2('racket.png', 645, 350, 10)
sprites = sprite.Group()
players = sprite.Group()
sprites.add(player1)
sprites.add(player2)

running = True
finish = False
FPS = 60
clock = time.Clock()

while running:  
    for e in event.get():
        if e.type == QUIT:
            running = False

    if not finish:
        window.blit(background, (0, 0))
        sprites.update()
        sprites.draw(window)

        display.update() 
        clock.tick(FPS)

quit()