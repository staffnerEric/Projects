import pygame

pygame.init()  
pygame.font.init()
base_font = pygame.font.Font(None, 32)
user_text = ''
user_text2 = ''
input_rect = pygame.Rect(100, 500, 140, 32)
input_rect2 = pygame.Rect(500, 500, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
plus=True
  
active = False
active2 = False
win=pygame.display.set_mode((900, 900))

life1 = pygame.font.SysFont('comicsans', 100)
life2 = pygame.font.SysFont('comicsans', 100)
points1=8000
points2=8000

def printlifepoints():
    global user_text, active, active2, user_text2, plus, points1, points2
    pygame.draw.rect(win, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
        
    pygame.draw.rect(win, color, input_rect2)
    text_surface2 = base_font.render(user_text2, True, (255, 255, 255))
    win.blit(text_surface2, (input_rect2.x+5, input_rect2.y+5))
    input_rect2.w = max(100, text_surface2.get_width()+10)
    leb = life1.render(str(points1), 1,(0 ,0 ,0))
    lob = life2.render(str(points2), 1,(0 ,0 ,0))
    win.blit(leb, (100, 300))
    win.blit(lob, (500, 300))

def main():
    global user_text, active, active2, user_text2, plus, points1, points2
    
    clock = pygame.time.Clock()
    while True:
        win.fill((0,0,255))
        printlifepoints()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                
                else:
                    active = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                
                else:
                    active2 = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-len(user_text)]
                else:
                    user_text += event.unicode
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text2 = user_text2[:-len(user_text2)]
                else:
                    user_text2 += event.unicode
        calculate=False
                    
        key=pygame.key.get_pressed()
        if key[pygame.K_LALT]:
            user_text=user_text[:-len(user_text)]
            
        if key[pygame.K_RCTRL]:
            user_text2=user_text2[:-len(user_text2)]
            
        if key[pygame.K_LSHIFT]:
            if plus==True:
                plus=False
                pygame.time.delay(300)
            else:
                plus=True
                pygame.time.delay(300)
            
        if key[pygame.K_LCTRL]:
            calculate= True
            
        if active:
            color = color_active
            
        elif plus==False:
            color= color_active
            
        else:
            color = color_passive
            
        if active2:
        
            color = color_active
        
        elif plus==False:
            color= color_active
            
        else:
            color = color_passive
        
        if plus==True and calculate==True:
            if not user_text == "":
                points1 -= int(user_text)
            if not user_text2 == "":
                points2 -= int(user_text2)
            pygame.time.delay(300)
        
        if plus==False and calculate==True:
            if not user_text == "":
                points1 += int(user_text)
            if not user_text2 == "":
                points2 += int(user_text2)
            pygame.time.delay(300)
        
        
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
main()
