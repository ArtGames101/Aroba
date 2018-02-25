#----Basic Setup----
import pygame

done = False

#---User Choose Load/New----
print("Would you like to load a project or")
print("create a new project?")
print("1. Load")
print("2. New")
start_user_input = input("> ")
start_user_input = start_user_input.upper()

load_file = ("error")

if start_user_input == "1":
    print("Enter the project you want to open.")
    load_file = input("> ")

elif start_user_input == "2":
    load_file = ("new")

else:
    print("Error")
    done = True

#----Colors----
#--User Interface Colors--
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GREY  = (215,215,215)
GREY = (180,180,180)
DARK_GREY = (100,100,100)
BLUE = (180,180,255)
DARK_BLUE = (100,100,200)
#--Drawing Colors--
DRAW_WHITE = (255,255,255)
DRAW_GREY = (127,127,127)
DRAW_BLACK = (0,0,0)
DRAW_RED = (255,0,0)
DRAW_ORANGE = (255,127,0)
DRAW_YELLOW = (255,255,0)
DRAW_GREEN = (0,255,0)
DRAW_BLUE = (0,0,255)
DRAW_PURPLE = (255,0,255)

#----Basic Setup----
pygame.init()

arial_font_24B = pygame.font.SysFont("arial", 24, True, False)
arial_font_12 = pygame.font.SysFont("arial", 12, False, False)

draw_size = 1
draw_color = DRAW_BLACK
tool = ("draw")

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Brush")

clock = pygame.time.Clock()

#----Loading----
if load_file == "new":
    screen.fill(WHITE)

elif load_file == "error":
    done = True
else:
    open_file = pygame.image.load(load_file).convert()
    screen.blit(open_file, (0,0))

# --------Main Program Loop--------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    #--------Game Logic--------
    #----Mouse Info----
    mouse_state = pygame.mouse.get_pressed()[0]
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    
    #----Save----
    if mouse_state == 1 and mouse_x >= 12 and mouse_x <= 88 and mouse_y >= 12 and mouse_y <= 88:
        print("What would you like to name this project?")
        print("Remember to add .png to the end.")
        project_name = input("> ")
        pygame.image.save(screen, project_name)
        done = True
    
    #--------Drawing Code--------
    #----Tool Bar----
    pygame.draw.rect(screen, LIGHT_GREY,(0,0,800,100))
    pygame.draw.line(screen, GREY,(0,100),(800,100),4)
    pygame.draw.line(screen, GREY,(100,0),(100,100),3)
    pygame.draw.line(screen, GREY,(200,0),(200,100),3)
    pygame.draw.line(screen, GREY,(300,0),(300,100),3)
    pygame.draw.line(screen, GREY,(400,0),(400,100),3)
    pygame.draw.line(screen, GREY,(500,0),(500,100),3)
    pygame.draw.line(screen, GREY,(600,0),(600,100),3)
    pygame.draw.line(screen, GREY,(700,0),(700,100),3)
    
    #----Tools----
    #----Save----
    pygame.draw.rect(screen, GREY,(12,12,76,76))
    pygame.draw.rect(screen, DARK_GREY,(12,12,76,76),2)
    save_text = arial_font_24B.render("Save", True, DARK_GREY)
    screen.blit(save_text, (27,35))
     
    #----User Drawing----
    if mouse_state == 1 and mouse_x >= 112 and mouse_x <= 188 and mouse_y >= 12 and mouse_y <= 44 or tool == "draw":
        tool = ("draw")
        pygame.draw.rect(screen, BLUE,(112,12,76,32))
        pygame.draw.rect(screen, DARK_BLUE,(112,12,76,32),2)
        draw_text = arial_font_24B.render("Pen", True, DARK_BLUE)
        screen.blit(draw_text, (133,14))
    else:
        pygame.draw.rect(screen, GREY,(112,12,76,32))
        pygame.draw.rect(screen, DARK_GREY,(112,12,76,32),2)
        draw_text = arial_font_24B.render("Pen", True, DARK_GREY)
        screen.blit(draw_text, (133,14))
    if mouse_state == 1 and tool == "draw" and mouse_y >= 103:
        pygame.draw.line(screen, draw_color,(past_mouse_x,past_mouse_y),(mouse_x,mouse_y),draw_size)
        pygame.draw.circle(screen, draw_color,(mouse_x,mouse_y),corner_size)
    
    #----Fill Screen----
    if mouse_state == 1 and mouse_x >= 112 and mouse_x <= 188 and mouse_y >= 56 and mouse_y <= 88 or tool == "fill":
        tool = ("fill")
        pygame.draw.rect(screen, BLUE,(112,56,76,32))
        pygame.draw.rect(screen, DARK_BLUE,(112,56,76,32),2)
        fill_text = arial_font_24B.render("Fill", True, DARK_BLUE)
        screen.blit(fill_text, (137,58))
    else:
        pygame.draw.rect(screen, GREY,(112,56,76,32))
        pygame.draw.rect(screen, DARK_GREY,(112,56,76,32),2)
        fill_text = arial_font_24B.render("Fill", True, DARK_GREY)
        screen.blit(fill_text, (137,58))
    if mouse_state == 1 and tool == "fill" and mouse_y >= 103:
        pygame.draw.rect(screen, draw_color,(0,103,800,697))
    
    #----Erase----
    if mouse_state == 1 and mouse_x >= 212 and mouse_x <= 288 and mouse_y >= 12 and mouse_y <= 88 or tool == "erase":
        tool = ("erase")
        pygame.draw.rect(screen, BLUE,(212,12,76,76))
        pygame.draw.rect(screen, DARK_BLUE,(212,12,76,76),2)
        draw_text = arial_font_24B.render("Erase", True, DARK_BLUE)
        screen.blit(draw_text, (223,35))
    else:
        pygame.draw.rect(screen, GREY,(212,12,76,76))
        pygame.draw.rect(screen, DARK_GREY,(212,12,76,76),2)
        draw_text = arial_font_24B.render("Erase", True, DARK_GREY)
        screen.blit(draw_text, (223,35))
    if mouse_state == 1 and tool == "erase" and mouse_y >= 103:
        pygame.draw.line(screen, WHITE,(past_mouse_x,past_mouse_y),(mouse_x,mouse_y),30)
        pygame.draw.circle(screen, WHITE,(mouse_x,mouse_y),14)
    
    #----Line Size----
    #--Size 1--
    if mouse_state == 1 and mouse_x >= 312 and mouse_x <= 388 and mouse_y >= 12 and mouse_y <= 28 or draw_size == 1:
        draw_size = 1
        corner_size = 0
        pygame.draw.rect(screen, BLUE,(312,12,76,16))
        pygame.draw.rect(screen, DARK_BLUE,(312,12,76,16),2)
        pygame.draw.line(screen, DARK_BLUE,(320,20),(380,20),1)
    else:
        pygame.draw.rect(screen, GREY,(312,12,76,16))
        pygame.draw.rect(screen, DARK_GREY,(312,12,76,16),2)
        pygame.draw.line(screen, DARK_GREY,(320,20),(380,20),1)
    
    #--Size 3--
    if mouse_state == 1 and mouse_x >= 312 and mouse_x <= 388 and mouse_y >= 32 and mouse_y <= 48 or draw_size == 3:
        draw_size = 3
        corner_size = 0
        pygame.draw.rect(screen, BLUE,(312,32,76,16))
        pygame.draw.rect(screen, DARK_BLUE,(312,32,76,16),2)
        pygame.draw.line(screen, DARK_BLUE,(320,40),(380,40),3)
    else:
        pygame.draw.rect(screen, GREY,(312,32,76,16))
        pygame.draw.rect(screen, DARK_GREY,(312,32,76,16),2)
        pygame.draw.line(screen, DARK_GREY,(320,40),(380,40),3)
    
    #--Size 5--
    
    if mouse_state == 1 and mouse_x >= 312 and mouse_x <= 388 and mouse_y >= 52 and mouse_y <= 68 or draw_size == 5:
        draw_size = 5
        corner_size = 2
        pygame.draw.rect(screen, BLUE,(312,52,76,16))
        pygame.draw.rect(screen, DARK_BLUE,(312,52,76,16),2)
        pygame.draw.line(screen, DARK_BLUE,(320,60),(380,60),5)
    else:
        pygame.draw.rect(screen, GREY,(312,52,76,16))
        pygame.draw.rect(screen, DARK_GREY,(312,52,76,16),2)
        pygame.draw.line(screen, DARK_GREY,(320,60),(380,60),5)
    #--Size 7--
    if mouse_state == 1 and mouse_x >= 312 and mouse_x <= 388 and mouse_y >= 72 and mouse_y <= 88 or draw_size == 7:
        draw_size = 7
        corner_size = 3
        pygame.draw.rect(screen, BLUE,(312,72,76,16))
        pygame.draw.rect(screen, DARK_BLUE,(312,72,76,16),2)
        pygame.draw.line(screen, DARK_BLUE,(320,80),(380,80),7)
    else:
        pygame.draw.rect(screen, GREY,(312,72,76,16))
        pygame.draw.rect(screen, DARK_GREY,(312,72,76,16),2)
        pygame.draw.line(screen, DARK_GREY,(320,80),(380,80),7)
        
    #----Line Color----
    #R O Y
    #G B P
    #W G B
    #--Red--
    if mouse_state == 1 and mouse_x >= 412 and mouse_x <= 432 and mouse_y >= 12 and mouse_y <= 32 or draw_color == DRAW_RED:
        draw_color = DRAW_RED
        pygame.draw.rect(screen, DRAW_RED,(412,12,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(412,12,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_RED,(412,12,20,20))
        pygame.draw.rect(screen, DARK_GREY,(412,12,20,20),2)
    
    #--Orange--
    if mouse_state == 1 and mouse_x >= 440 and mouse_x <= 460 and mouse_y >= 12 and mouse_y <= 32 or draw_color == DRAW_ORANGE:
        draw_color = DRAW_ORANGE
        pygame.draw.rect(screen, DRAW_ORANGE,(440,12,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(440,12,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_ORANGE,(440,12,20,20))
        pygame.draw.rect(screen, DARK_GREY,(440,12,20,20),2)
    
    #--Yellow--
    if mouse_state == 1 and mouse_x >= 468 and mouse_x <= 488 and mouse_y >= 12 and mouse_y <= 32 or draw_color == DRAW_YELLOW:
        draw_color = DRAW_YELLOW
        pygame.draw.rect(screen, DRAW_YELLOW,(468,12,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(468,12,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_YELLOW,(468,12,20,20))
        pygame.draw.rect(screen, DARK_GREY,(468,12,20,20),2)
    
    #--Green--
    if mouse_state == 1 and mouse_x >= 412 and mouse_x <= 432 and mouse_y >= 40 and mouse_y <= 60 or draw_color == DRAW_GREEN:
        draw_color = DRAW_GREEN
        pygame.draw.rect(screen, DRAW_GREEN,(412,40,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(412,40,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_GREEN,(412,40,20,20))
        pygame.draw.rect(screen, DARK_GREY,(412,40,20,20),2)
    
    #--Blue--
    if mouse_state == 1 and mouse_x >= 440 and mouse_x <= 460 and mouse_y >= 40 and mouse_y <= 60 or draw_color == DRAW_BLUE:
        draw_color = DRAW_BLUE
        pygame.draw.rect(screen, DRAW_BLUE,(440,40,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(440,40,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_BLUE,(440,40,20,20))
        pygame.draw.rect(screen, DARK_GREY,(440,40,20,20),2)
    
    #--Purple--
    if mouse_state == 1 and mouse_x >= 468 and mouse_x <= 488 and mouse_y >= 40 and mouse_y <= 60 or draw_color == DRAW_PURPLE:
        draw_color = DRAW_PURPLE
        pygame.draw.rect(screen, DRAW_PURPLE,(468,40,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(468,40,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_PURPLE,(468,40,20,20))
        pygame.draw.rect(screen, DARK_GREY,(468,40,20,20),2)
    
    #--White--
    if mouse_state == 1 and mouse_x >= 412 and mouse_x <= 432 and mouse_y >= 68 and mouse_y <= 88 or draw_color == DRAW_WHITE:
        draw_color = DRAW_WHITE
        pygame.draw.rect(screen, DRAW_WHITE,(412,68,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(412,68,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_WHITE,(412,68,20,20))
        pygame.draw.rect(screen, DARK_GREY,(412,68,20,20),2)
    
    #--Grey--
    if mouse_state == 1 and mouse_x >= 440 and mouse_x <= 460 and mouse_y >= 68 and mouse_y <= 88 or draw_color == DRAW_GREY:
        draw_color = DRAW_GREY
        pygame.draw.rect(screen, DRAW_GREY,(440,68,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(440,68,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_GREY,(440,68,20,20))
        pygame.draw.rect(screen, DARK_GREY,(440,68,20,20),2)
    
    #--Black--
    if mouse_state == 1 and mouse_x >= 468 and mouse_x <= 488 and mouse_y >= 68 and mouse_y <= 88 or draw_color == DRAW_BLACK:
        draw_color = DRAW_BLACK
        pygame.draw.rect(screen, DRAW_BLACK,(468,68,20,20))
        pygame.draw.rect(screen, DARK_BLUE,(468,68,20,20),2)
    else:
        pygame.draw.rect(screen, DRAW_BLACK,(468,68,20,20))
        pygame.draw.rect(screen, DARK_GREY,(468,68,20,20),2)
    
    #----Line Drawing----
    
    #----Square Drawing----
    
    #----Ellipse Drawing----
    
    #----Mouse Info----
    past_mouse_x = mouse_x
    past_mouse_y = mouse_y
    
    #----Version----
    version = arial_font_12.render(".", False, DARK_GREY)
    screen.blit(version, (2,103))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
