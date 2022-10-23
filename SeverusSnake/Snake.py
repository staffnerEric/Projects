import pygame
from Blocks import Block
import random
import os


pygame.font.init()
SCORE_FONT = pygame.font.SysFont('comicsans', 50)
Death_FONT = pygame.font.SysFont('comicsans', 100)
black=(0,0,0)
green=(1,255,1)
win=pygame.display.set_mode((900, 900))
playerList = [91]
snape=pygame.image.load(os.path.join("Snape.png"))
snapeHead = pygame.transform.scale(snape,(30,30))
score = 0
clock = pygame.time.Clock()
nFin = True


def gameOver():
    global nFin
    death_text = Death_FONT.render("You Died!!!",1,black )
    win.blit(death_text, (300, 300))
    pygame.display.update()
    nFin = False
    pygame.time.delay(1000)
    
def moveActor(blocks, direction):
    global playerList,score
    # % ist modolo(wenn es geteilt durch das geht mit so und so viel rest)
    if playerList[len(playerList)-1]%30==0 and direction== 1:
        gameOver()
    if playerList[len(playerList)-1]%30==1 and direction== -1 and playerList[len(playerList)-1] !=1 or playerList[len(playerList)-1] ==0:
        gameOver()
    if blocks[int(playerList[len(playerList)-1])+direction].color != (0,0,0):
        playerList.append(playerList[len(playerList)-1]+direction)
        blocks[playerList[0]].color = (0, 255, 0)
        playerList.pop(0)
        blocks[playerList[len(playerList)-1]].color = (0, 0, 0)
        if blocks[int(playerList[len(playerList)-1])+direction].color == (255,0,0):
            playerList.append(playerList[len(playerList)-1]+direction)
            placeApple(blocks)
            score+=1
    elif blocks[int(playerList[len(playerList)-1])+direction].color == (0,0,0) and not direction == 0:
        gameOver()

def actorDirection(direction):
    keyi = pygame.key.get_pressed()
    if keyi[pygame.K_a]:  
        return -1
    if keyi[pygame.K_d]:
        return +1
    if keyi[pygame.K_w]:  
        return -30
    if keyi[pygame.K_s]:
        return +30
    else:
        return direction
    
def createBlocks():
    #place a number of blocks
    blocks = []
    x = 0
    y = 0
    for i in range(30*30+1):
        #create Block and add to list blocks
        b = Block(30, (0, 255, 0), x, y)
        blocks.append(b)
        y+=30
        if i % 30 == 0 and i != 0:
            x+=30
            y = 0
    return blocks

def placeApple(blocks):
    while True:
        rand=random.randint(0, 30*30)
        if blocks[rand].color != (0, 0, 0):
            blocks[rand].color = (255, 0, 0)
            break
        else:
            continue
    
def drawWindow(blocks):
    global score
    for block in blocks:
        b = pygame.Rect(block.y, block.x, block.size, block.size)
        pygame.draw.rect(win, block.color, b)
    pygame.display.update()
    snapeX = blocks[playerList[len(playerList)-1]].x
    snapeY = blocks[playerList[len(playerList)-1]].y
    win.blit(snapeHead,(snapeY, snapeX))
    score_text = SCORE_FONT.render("Score: "+ str(score),1,black )
    win.blit(score_text, (10, 10))
    #place rectangle for every block

def main():
    global nFin
    blocks = createBlocks()
    placeApple(blocks)
    direction = 0
    try:
        while nFin:
            clock.tick(10) 
            drawWindow(blocks)
            direction = actorDirection(direction)
            pygame.display.update()
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    nFin=False
            #move using arrow keys
            moveActor(blocks, direction)
    except:
        gameOver()

        
if __name__ == "__main__":
    main()