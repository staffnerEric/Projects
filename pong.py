import pygame
import random

pygame.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)
winFONT = pygame.font.SysFont('arial', 50)
winFONT2 = pygame.font.SysFont('arial', 50)
SCORE_FONT2 = pygame.font.SysFont('arial', 50)
randomball=random.randint(1, 2)
richtungballx=4
richtungbally=random.randint(-3,3)
score= 0
score2=0
p1_y =300
p2_y =300
VEL = 10 
ballpos=500
white=(255,255,255)
black=(0,0,0)
win= pygame.display.set_mode((1000, 800))
player2 = pygame.Rect(970, p2_y, 10, 100)
player1 = pygame.Rect(20, p1_y, 10, 100)
ball = pygame.Rect(ballpos, 350, 10, 10)
walltop = pygame.Rect(0, 0, 1000, 10)
wallright = pygame.Rect(990, 0, 10, 800)
wallleft = pygame.Rect(0, 0, 10, 800)
wallbotom = pygame.Rect(0, 790, 1000, 10)
directionVector = [0, 0]

def ballrichtung():
    global ball, player1, player2, richtungballx, wallbotom, walltop, richtungbally, score, score2

    if ball.colliderect(player1):
        richtungballx *= -1
        if richtungballx>0:
            richtungballx += 1
        else:
            richtungballx -= 1
        ball.move_ip(richtungballx,richtungbally)

    if ball.colliderect(player2):
        richtungballx *= -1
        if richtungballx>0:
            richtungballx += 1
        else:
            richtungballx -= 1
        ball.move_ip(richtungballx,richtungbally)

    if ball.colliderect(walltop):
        richtungbally *= -1
        ball.move_ip(richtungballx,richtungbally)

    if ball.colliderect(wallbotom):
        richtungbally *= -1
        ball.move_ip(richtungballx,richtungbally)

    if ball.colliderect(wallleft):
        score2 += 1
        richtungballx= 5
        richtungbally=random.randint(-4,4)
    if ball.colliderect(wallright):
        score += 1
        richtungballx= -5
        richtungbally=random.randint(-4,4)      
def movementball(randomball):
    if randomball == 2:
        ball.move_ip(richtungballx,richtungbally)
    if randomball == 1:
        ball.move_ip(richtungballx,richtungbally)

    pygame.time.delay(5)

def movementp1(keys_pressed, p1_y):
    if keys_pressed[pygame.K_w] and p1_y - VEL > 0: 
        player1.move_ip(0, -10)
        p1_y -= VEL
    if keys_pressed[pygame.K_s] and p1_y + VEL + 100 < 800 - 15:
        player1.move_ip(0, 10)
        p1_y += VEL
    pygame.time.delay(5)

def movementp2(keys_pressed, p2_y):
    if keys_pressed[pygame.K_UP] and p2_y - VEL > 0:
        player2.move_ip(0, -10)
        p2_y -= VEL
    if keys_pressed[pygame.K_DOWN] and p2_y + VEL + 100 < 800 - 15:
        player2.move_ip(0, 10)
        p2_y += VEL
    pygame.time.delay(5)
        
def drawWindow():
    global score, score2
    pygame.draw.rect(win, white, player1)
    pygame.draw.rect(win, white, player2)
    pygame.draw.rect(win, white, ball)
    pygame.draw.rect(win, black, wallright)
    pygame.draw.rect(win, black, wallleft)


def main():
    global winFONT, winFONT2
    pon=True
    while pon:
        pygame.display.update()
        win.fill((0, 0, 0))
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pon=False
        drawWindow()
        keys_pressed = pygame.key.get_pressed()
        ballrichtung()
        score_text = SCORE_FONT.render("Score: "+ str(score), 1, white )
        win.blit(score_text, (10, 10))
        score_text2 = SCORE_FONT2.render("Score: "+ str(score2), 1, white )
        win.blit(score_text2, (800, 10))
        movementball(randomball)
        movementp1(keys_pressed, p1_y)
        movementp2(keys_pressed, p2_y)
        pygame.display.update()
        if score2 >= 10:
            winner_text2 = winFONT2.render("Right Player wins!!!", 1 ,white )
            win.blit(score_text2, (500, 350))
            pygame.time.delay(10000)
            pon=False
        if score >= 10:
            winner_text = winFONT.render("Left Player wins!!!", 1, white)
            win.blit(score_text2, (500, 350))
            pygame.time.delay(10000)
            pon=False
        
if __name__=="__main__":
    
    main()