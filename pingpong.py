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

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction_x = 1
        self.direction_y = 1 

    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

        if self.rect.y <= 0 or self.rect.y >= win_height - self.rect.height:
            self.direction_y *= -1 

        if sprite.collide_rect(self, player1) or sprite.collide_rect(self, player2):
            self.direction_x *= -1  

        if self.rect.x < 0:
            global score2
            score2 += 1
            self.reset_ball()
        if self.rect.x > win_width:
            global score1
            score1 += 1
            self.reset_ball() 

    def reset_ball(self):
        self.rect.x = win_width // 2  
        self.rect.y = win_height // 2  
        self.direction_x *= -1 

win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("background.png"), (win_width, win_height))

player1 = Racket1('racket.png', 0, 350, 10)
player2 = Racket2('racket.png', 645, 350, 10)
ball = Ball('ball.png', win_width // 2, win_height // 2, 7) 

sprites = sprite.Group()
sprites.add(player1)
sprites.add(player2)
sprites.add(ball)  


score1 = 0
score2 = 0
winning_score = 5  

font.init()
font_score = font.Font(None, 36)
font_winner = font.Font(None, 64)

running = True
finish = False
winner_text = ""
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

        score_text = font_score.render(f"Player 1: {score1}   Player 2: {score2}", True, (255, 255, 255))
        window.blit(score_text, (win_width // 2 - score_text.get_width() // 2, 10))
        if score1 >= winning_score:
            winner_text = "Player 1 Wins!"
            finish = True
        elif score2 >= winning_score:
            winner_text = "Player 2 Wins!"
            finish = True

        display.update() 
        clock.tick(FPS)
    else:
        window.blit(background, (0, 0))
        win_text_render = font_winner.render(winner_text, True, (255, 0, 0))
        window.blit(win_text_render, (win_width // 2 - win_text_render.get_width() // 2, win_height // 3))

        info_text = font_score.render("Press SPACE to play again or ESC to quit", True, (255, 255, 255))
        window.blit(info_text, (win_width // 2 - info_text.get_width() // 2, win_height // 2))

        display.update()

        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    score1 = 0
                    score2 = 0
                    ball.reset_ball()
                    finish = False
                elif e.key == K_ESCAPE:
                    running = False

        clock.tick(FPS)

quit()
