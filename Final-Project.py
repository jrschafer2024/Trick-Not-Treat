#Author: Jessica Schafer
#Date: December 10, 2021
#Description: This is the program for my final project, a floor maze
#             game that is Halloween inspired.


import pygame, sys, random
pygame.init()

#Initializing global variables
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
LIVES = 3

def titleScreen():
    #Loading and blitting the titlescreen image
    background = pygame.image.load("TitleScreen.png")
    background = pygame.transform.scale(background, (800,600))
    background = background.convert()

    clock = pygame.time.Clock()
    keepGoing = True

    screen.blit(background, (0,0))
    pygame.display.flip()

    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()

def choosePlayer():
    blue = (0,0,255)

    #Displaying the witch character
    witch = pygame.image.load("WitchFront(B).png")
    witch.set_colorkey(blue)
    witch = pygame.transform.scale(witch, (100,200))
    witch = witch.convert()

    #Displaying the vampire character
    vampire = pygame.image.load("VampireFront(B).png")
    vampire.set_colorkey(blue)
    vampire = pygame.transform.scale(vampire, (115,200))
    vampire = vampire.convert()

    #Displaying the pumpkin character
    pumpkin = pygame.image.load("PumpkinFront(B).png")
    pumpkin.set_colorkey(blue)
    pumpkin = pygame.transform.scale(pumpkin, (115,200))
    pumpkin = pumpkin.convert()

    #Displaying the mummy character
    mummy = pygame.image.load("MummyFront(B).png")
    mummy.set_colorkey(blue)
    mummy = pygame.transform.scale(mummy, (115,190))
    mummy = mummy.convert()

    #Building the background
    background = pygame.image.load("Forest.jpg")
    background = pygame.transform.scale(background, (800,600))
    background = background.convert()

    #Building the text labels (for choices and instructions)
    font = pygame.font.SysFont("comic sans ms", 45)
    Choose_txt = font.render("Choose your character", 45, (0,255,0))
    one = font.render("1", 10, (0,255,0))
    two = font.render("2", 10, (0,255,0))
    three = font.render("3", 10, (0,255,0))
    four = font.render("4", 10, (0,255,0))

    kids = ["WitchMirror(B).png", "VampireMirror(B).png", "PumpkinMirror(B).png", "MummyMirror(B).png"]

    clock = pygame.time.Clock()
    keepGoing = True

    screen.blit(background,(0,0))
    screen.blit(one, (135,360))
    screen.blit(witch, (100,400))
    screen.blit(two, (285,360))
    screen.blit(vampire, (250,410))
    screen.blit(three, (445, 360))
    screen.blit(pumpkin, (410,410))
    screen.blit(four, (595, 360))
    screen.blit(mummy, (560,410))
    screen.blit(Choose_txt, (150,200))
    pygame.display.flip()

    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()
                if event.key==pygame.K_1:               #If they choose the witch:
                    character = "WitchBack(B).png"          #Setting the witch as the main character     
                    kids.remove("WitchMirror(B).png")       #Removing the witch from the list with the rest of the kids
                    characterM = "WitchMirror(B).png"       #Initializing the mirror for the screen that shows if the player loses the game.
                if event.key==pygame.K_2:               #The same steps for if the player chooses any of the other characters
                    character = "VampireBack(B).png"
                    kids.remove("VampireMirror(B).png")
                    characterM = "VampireMirror(B).png"
                if event.key==pygame.K_3:
                    character = "PumpkinBack(B).png"
                    kids.remove("PumpkinMirror(B).png")
                    characterM = "PumpkinMirror(B).png"
                if event.key==pygame.K_4:
                    character = "MummyBack(B).png"
                    kids.remove("MummyMirror(B).png")
                    characterM = "MummyMirror(B).png"
                keepGoing = False
    
    return character, kids, characterM

def Intro(kids):
    #Building the background
    blue = (0,0,255)
    background = pygame.Surface(screen.get_size())
    background.fill((53, 1, 135))
    background = background.convert()

    #Building the introduction page that tells the backstory
    font = pygame.font.SysFont("comic sans ms", 12)
    Inst = font.render("click anywhere to continue", 10, (255,255,255))
    text = pygame.image.load("Intro.png")
    text.set_colorkey((0,0,0))
    pygame.transform.scale(text, (800,600))
    text = text.convert()

    #Loading the images of the kids trapped in the mirrors
    mirror_one = pygame.image.load(f"{kids[0]}")
    mirror_one.set_colorkey(blue)
    mirror_one = pygame.transform.scale(mirror_one, (200,300))
    mirror_one = mirror_one.convert()

    mirror_two = pygame.image.load(f"{kids[1]}")
    mirror_two.set_colorkey(blue)
    mirror_two = pygame.transform.scale(mirror_two, (200,300))
    mirror_two = mirror_two.convert()

    mirror_three = pygame.image.load(f"{kids[2]}")
    mirror_three.set_colorkey(blue)
    mirror_three = pygame.transform.scale(mirror_three, (200,300))
    mirror_three = mirror_three.convert()

    #Blitting everything to the screen
    screen.blit(background, (0,0))
    screen.blit(text, (-75,0))
    screen.blit(Inst, (325, 275))
    screen.blit(mirror_one, (100, 300))
    screen.blit(mirror_two, (300, 300))
    screen.blit(mirror_three, (500,300))
    pygame.display.flip()

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()

def letter():
    #Building and blitting the letter image
    background = pygame.image.load("Letter.png")
    background = pygame.transform.scale(background, (800,600))
    background = background.convert()

    clock = pygame.time.Clock()
    keepGoing = True

    screen.blit(background, (0,0))
    pygame.display.flip()

    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()

def Instructions():
    #Building and blitting the instructions
    background = pygame.image.load("Rules.png")
    background = pygame.transform.scale(background, (900,600))
    background = background.convert()
    font = pygame.font.SysFont("comic sans ms", 12)
    click = font.render("click anywhere to continue", 10, (255,255,255))

    clock = pygame.time.Clock()
    keepGoing = True

    screen.blit(background, (-50,0))
    screen.blit(click, (325,550))
    pygame.display.flip()

    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()

    
def Win(): #If the player wins the game:
    background = pygame.Surface(screen.get_size())
    background.fill((7,73,179))
    background = background.convert()

    middle = screen.get_height()/2
    position = ((screen.get_width()/2)-300, screen.get_height()/3)

    #Creating a text label
    font = pygame.font.SysFont("comic sans ms", 30)
    message = font.render("You win!",45, (255,255,255))

    position_two = ((screen.get_width()/2)-300, screen.get_height()/2)

    again = font.render("Do you want to play again? (Y/N)",45,(255,255,255))

    clock = pygame.time.Clock()
    keepGoing = True
    replay = False

    #The game loop - exiting this screen
    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE or pygame.K_n:
                    keepGoing = False
                if event.key==pygame.K_y:
                    keepGoing = False
                    replay = True
        screen.blit(background, (0,0))
        screen.blit(message, position)
        screen.blit(again, position_two)
        pygame.display.flip()

    return replay

def Lose(characterM): #If the player loses the game:
    blue = (0,0,255)
    background = pygame.Surface(screen.get_size())
    background.fill((7,73,179))
    background = background.convert()

    character = pygame.image.load(characterM)
    character.set_colorkey(blue)
    character = pygame.transform.scale(character, (200,300))
    character = character.convert()

    middle = screen.get_height()/2
    position = ((screen.get_width()/2)-300, screen.get_height()/3)

    #Creating a text label
    font = pygame.font.SysFont("comic sans ms", 30)
    message = font.render("You Lose!",45, (255,255,255))

    position_two = ((screen.get_width()/2)-300, screen.get_height()/2)

    again = font.render("Do you want to play again? (Y/N)",45,(255,255,255))

    clock = pygame.time.Clock()
    keepGoing = True
    replay = False

    #The game loop - exiting this screen
    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE or pygame.K_n:
                    keepGoing = False
                if event.key==pygame.K_y:
                    keepGoing = False
                    replay = True
        screen.blit(background, (0,0))
        screen.blit(message, (325,100))
        screen.blit(again, (185,500))
        screen.blit(character, (295,175))
        pygame.display.flip()
        
    return replay

def Thanks(): #If the player chooses not to play again:
    background = pygame.image.load("EndScreen.png")
    background = pygame.transform.scale(background, (900,600))
    background = background.convert()

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing==True:
        screen.blit(background, (-50,0))
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
    else:
        pygame.quit()


class Kids(pygame.sprite.Sprite): #The sprite class for the kids
    def __init__(self,character): #"character" is the character the player chose to use
        blue = (0,0,255)
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(character)
        self.image.set_colorkey(blue)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 360
        self.rect.centery = 500

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.centery-=50
        if keys[pygame.K_DOWN]:
            self.rect.centery+=50
        if keys[pygame.K_RIGHT]:
            self.rect.centerx+=57
        if keys[pygame.K_LEFT]:
            self.rect.centerx-=57

class Label(pygame.sprite.Sprite): #The sprite class for text
    def __init__(self, message, position, font, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.Font = pygame.font.SysFont(f"{font}", int(size))
        self.text = message
        self.pos = position
        self.col = color

    def update(self):
        self.message = font.render(f"{self.text}", 1, (color))
        rect = self.message.get_rect()
        self.rect = self.pos
        
def Type(): #The function used when the players need to answer the riddle
    answer = ""

    #Drawing a rectangular border for the player to type in
    rect = pygame.Rect(200,400,300,100)
    color = (0,0,0)

    #The font they will be using
    font = pygame.font.SysFont("comic sans ms", 20)
    clock = pygame.time.Clock()

    pygame.draw.rect(screen, color, rect, 2)

    #rendering and blitting what the user types
    userInput = font.render(answer, True, (0,0,0))
    screen.blit(userInput,(rect.x+5,rect.y+5))
    pygame.display.flip()

    input_active = True
    
    keepGoing = True
    while keepGoing==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               keepGoing = False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                input_active = True
                answer = ""
            elif event.type==pygame.KEYDOWN and input_active:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()
                if event.key==pygame.K_RETURN:
                    input_active = False
                    keepGoing = False
                elif event.key==pygame.K_BACKSPACE:
                    answer = answer[:-1]  #Removes the last character in "answer"
                else:
                    answer+=event.unicode #Adds the typed characters to "answer"

        #Drawing and blitting everything
        box = pygame.Surface(screen.get_size())
        box.convert()
        box.fill((194,4,4))
        pygame.draw.rect(screen,(194,4,4),rect)
        pygame.draw.rect(screen, color, rect, 2)
        userInput = font.render(answer, True, (0,0,0))
        screen.blit(userInput,(rect.x+5,rect.y+5))
        pygame.display.flip()

    return answer

def riddle():
    #All of the riddles
    one = ["The person who built it sold it.", "The person who bought it never used it.", "The person who used it never saw it.", "What is it?"]
    one_answer = "coffin"

    two = ["How do you spell candy in two letters?"]
    two_answer = "c and y"

    three = ["I have no feet to dance, I have no eyes to see,", "I have no life to live or die but yet I do all three.", "What am I?"]
    three_answer = "fire"

    four = ["I am wrapped but I am not a gift.", "I am kept neatly in a chamber", "and Archologists find me as a great treasure.", "What am I?"]
    four_answer = "mummy"

    five = ["Two men are walking in a graveyard.", "The first man walks to a grave.", "The second man says, \"Who is in that grave?\"", "The first man points to the grave and says,", "\"Brothers and sisters I have none.", "But that man's father is my father's son.\"", "Who is in the grave?"]
    five_answer = "his son"

    six = ["A zombie, a mummy, and a ghost bought a house.", "It has all of the usual rooms except for one.", "What room won't you find?"]
    six_answer = "living room"

    seven = ["I have hundreds of ears, but I can't hear a thing.", "What am I?"]
    seven_answer = "cornfield"

    eight = ["I have a name, but it isn't mine.", "You don't think about me all the time.", "People cry when I'm in their sight.", "Others lie with me all day and night.", "What am I?"]
    eight_answer = "tombstone"

    nine = ["I am different sizes, shapes, and colors.", "Many can see my veins.", "I don't go inside and", "if I fall to the ground I will surely die.", "What am I?"]
    nine_answer = "leaf"

    onezero = ["Poor people have it. Rich people need it.", "If you eat it you die.", "What is it?"]
    onezero_answer = "nothing"

    oneone = ["I have a body, arms, legs, and a head,", "but I am heartless and have no guts.", "What am I?"]
    oneone_answer = "skeleton"

    onetwo = ["I'm tall when I'm young,", "I'm short when I'm old,", "and once a year, I make heavy pumpkins light.", "What am I?"]
    onetwo_answer = "candle"

    onethree = ["Frankenstein's father has three sons.", "The names of two are Snap and Crackle.", "What is the third son called?"]
    onethree_answer = "frankenstein"

    onefour = ["What is dead, cold, hard, and surrounds a cemetery?"]
    onefour_answer = "fence"

    onefive = ["Where do ghosts, mummies, and zombies love to swim?"]
    onefive_answer = "dead sea"

    onesix = ["The more you have, the less you see.", "What is it?"]
    onesix_answer = "darkness"

    oneseven = ["We have no flesh, no feathers, no scales, no bones.", "We do have fingers and thumbs of our own.", "What are we?"]
    oneseven_answer = "gloves"

    oneeight = ["Look in my face, I am somebody.", "Look in my back, I am nobody.", "What am I?"]
    oneeight_answer = "mirror"

    onenine = ["The more you take, the more there are.", "What is it?"]
    onenine_answer = "footsteps"

    twozero = ["What gets bigger the more you take away?"]
    twozero_answer = "hole"

    #Putting the riddles and their answers into lists.
    Riddles = [one, two, three, four, five, six, seven, eight, nine, onezero, oneone, onetwo, onethree, onefour, onefive, onesix, oneseven, oneeight, onenine, twozero]
    correct = [one_answer, two_answer, three_answer, four_answer, five_answer, six_answer, seven_answer, eight_answer, nine_answer, onezero_answer, oneone_answer, onetwo_answer, onethree_answer, onefour_answer, onefive_answer, onesix_answer, oneseven_answer, oneeight_answer, onenine_answer, twozero_answer]
    num = random.randint(0,19)
    challenge = Riddles[num]

    #Building a surface the same size as the screen
    height = (HEIGHT/3)

    box = pygame.Surface(screen.get_size())
    box.convert()
    box.fill((194,4,4))

    font = pygame.font.SysFont("comic sans ms", 20)
    screen.blit(box,(0,0))
    
    #Blitting the elements of the riddles (since they are a list)
    #This prevents the riddle text from going off of the screen.
    for lines in challenge:
        Riddle = font.render(lines, 10, (255,255,255))
        screen.blit(Riddle,(200,height))
        height+=25

    return correct, num

def game(character, correct, num, LIVES): #Actual gameplay
    #Initializing variables (lives, location of the player, and building the background)
    lives = 3
    life = str(lives)
    player = Kids(character)
    player.rect.centerx = 360
    player.rect.centery = 500
    kid = pygame.sprite.Group(player)
    background = pygame.image.load("floor.png")
    background = pygame.transform.scale(background, (800,600))
    background = background.convert()

    #Initializing sound  and font variables
    BoySound = pygame.mixer.Sound("Boy-Saying-Super.wav")
    FlaughSound = pygame.mixer.Sound("Human_Voice_Laugh_Evil_Female_01.mp3")

    font = pygame.font.SysFont("comic sans ms", 20)
    lives_txt = font.render(f"Lives: {life}", 10, (255,255,255))

    #The list of rect pairs the player does not want to move to.
    badSquares = [(60,50),(60,95),(60,140),(60,185),(60,230),(60,275),(60,320),(60,365),(60,410),(60,455),
                  (120,50),(120,95),(120,140),(120,185),(120,230),(120,275),(120,320),(120,365),(120,410),(120,455),
                  (180,50),(180,95),(180,140),(180,185),(180,230),(180,275),(180,320),(180,365),(180,410),(180,455),
                  (240,50),(240,275),(240,320),(240,365),(240,410),(240,455),(360,50),(360,140),(360,185),(360,275),
                  (360,320),(360,365),(360,410),(420,50),(420,140),(420,185),(420,275),(420,320),(420,365),(420,410),
                  (480,50),(480,140),(480,185),(540,50),(540,140),(540,185),(540,230),(540,275),(540,320),(540,365),(540,410),(540,455),
                  (600,50),(600,140),(600,185),(600,230),(600,275),(600,320),(600,365),(600,410),(600,455),
                  (660,140),(660,185),(660,230),(660,275),(660,320),(660,365),(660,410),(660,455),
                  (720,50),(720,95),(720,140),(720,185),(720,230),(720,275),(720,320),(720,365),(720,410),(720,455)]

    keepGoing = True
    clock = pygame.time.Clock()

    while keepGoing==True:
        while lives>0 and player.rect.centery>=0:
            #Drawing and blitting everything to the screen
            screen.blit(background, (0,0))
            screen.blit(lives_txt, (700,550))
            kid.draw(screen) 
            pygame.display.flip()
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                if event.type==pygame.KEYDOWN:
                    if event.type==pygame.K_ESCAPE:
                        keepGoing = False
                        pygame.quit()
                    if event.key==pygame.K_DOWN:                                                #If a player presses the down key and moves the character down:
                        if player.rect.centery+45>=screen.get_height():                             #checking to see if they will go off the screen
                            player.rect.centery-=45
                        player.rect.centery+=45                                                     #if they will not go off the screen, move down 
                        screen.blit(background, (0,0))                                              #redrawing background and character
                        kid.draw(screen)
                        if (player.rect.centerx,player.rect.centery) in badSquares:                 #if they move to a "bad square":
                            riddle()                                                                    #call the riddle function
                            correct, num = riddle()                                                 
                            answer = Type()                                                             #call the type function so they can answer the riddle    
                            if correct[num] not in answer.lower():                                  #if they answer incorrectly:
                                FlaughSound.play()                  
                                player.rect.centerx = 360                                               #Moving the character back to where they started
                                player.rect.centery = 500
                                lives-=1
                                life = str(lives)
                                lives_txt = font.render(f"Lives: {life}", 10, (255,255,255))            #Subtracting one life and blitting that to the screen 
                                keepGoing = True
                            if correct[num] in answer:                                              #if they answer correctly:
                                BoySound.play()
                                player.rect.centerx = player.rect.centerx                               #returning them to where they were 
                                player.rect.centery = player.rect.centery
                                keepGoing = True                                                #repeat these steps for if the up, left, or right arrow keys are pressed
                    if event.key==pygame.K_UP:
                        player.rect.centery-=45
                        screen.blit(background, (0,0))
                        kid.draw(screen)
                        if (player.rect.centerx,player.rect.centery) in badSquares:
                            riddle()
                            correct, num = riddle()
                            answer = Type()
                            if correct[num] not in answer.lower():
                                FlaughSound.play()
                                player.rect.centerx = 360
                                player.rect.centery = 500
                                lives-=1
                                life = str(lives)
                                lives_txt = font.render(f"Lives: {life}", 10, (255,255,255))
                                keepGoing = True
                            if correct[num] in answer:
                                BoySound.play()
                                player.rect.centerx = player.rect.centerx
                                player.rect.centery = player.rect.centery
                                keepGoing = True
                    if event.key==pygame.K_LEFT:
                        if player.rect.centerx-60==0:
                            player.rect.centerx+=60
                        player.rect.centerx-=60
                        screen.blit(background, (0,0))
                        kid.draw(screen)
                        if (player.rect.centerx,player.rect.centery) in badSquares:
                            riddle()
                            correct, num = riddle()
                            answer = Type()
                            if correct[num] not in answer.lower():
                                FlaughSound.play()
                                player.rect.centerx = 360
                                player.rect.centery = 500
                                lives-=1
                                life = str(lives)
                                lives_txt = font.render(f"Lives: {life}", 10, (255,255,255))
                                keepGoing = True
                            if correct[num] in answer:
                                BoySound.play()
                                player.rect.centerx = player.rect.centerx
                                player.rect.centery = player.rect.centery
                                keepGoing = True
                    if event.key==pygame.K_RIGHT:
                        if player.rect.centerx+120>=screen.get_width():
                            player.rect.centerx-=60
                        player.rect.centerx+=60
                        screen.blit(background, (0,0))
                        kid.draw(screen)
                        if (player.rect.centerx,player.rect.centery) in badSquares:
                           if (player.rect.centerx,player.rect.centery) in badSquares:
                            riddle()
                            correct, num = riddle()
                            answer = Type()
                            if correct[num] not in answer.lower():
                                FlaughSound.play()
                                player.rect.centerx = 360
                                player.rect.centery = 500
                                lives-=1
                                life = str(lives)
                                lives_txt = font.render(f"Lives: {life}", 10, (255,255,255))
                                keepGoing = True
                            if correct[num] in answer:
                                BoySound.play()
                                player.rect.centerx = player.rect.centerx
                                player.rect.centery = player.rect.centery
                                keepGoing = True
    
        else:
            keepGoing = False
            
    #Blitting and drawing everything to the screen    
    screen.blit(background, (0,0))
    screen.blit(lives_txt, (600,400))
    kid.update()
    kid.draw(screen)
    screen.blit(lives_txt, (600,400))
    pygame.display.flip()

    return player.rect.centery, lives

def main():
    replay = True
    titleScreen()
    clock = pygame.time.Clock()
    while replay==True: #replay stores whether or not the player wants to play again
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               keepGoing = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.quit()
        character, kids, characterM = choosePlayer()
        correct, num = riddle()
        Intro(kids)
        letter()
        Instructions()
        #Sound that plays when you enter the main game loop
        DreamSound = pygame.mixer.Sound("Dream.wav")
        DreamSound.play()
        playery, Life = game(character, correct, num, LIVES)
        if playery<=0: #If the player makes it to the other side of the maze:
            endSound = pygame.mixer.Sound("End Sound.wav")
            endSound.play()
            replay = Win() #Tell them they win, ask if they want to play again
        elif Life==0: #If the player runs out of lives:
            MlaughSound = pygame.mixer.Sound("Human_Voice_Laugh_Evil_Male_03.mp3")
            MlaughSound.play()
            replay = Lose(characterM) #Tell them they lose, ask if they want to play again.
    else:
        Thanks()
   
main()
pygame.quit()   
