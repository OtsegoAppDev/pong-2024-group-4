import pygame as pygame

def MoveBall():
    global ballSpeedx, ballSpeedy, ballLocation, ball
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
        
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
        
    if ballLocation[1]< 0:
        ballSpeedy = -ballSpeedy
        
    if ballLocation[1] > screenHeight:
        ballSpeedy = -ballSpeedy
        
        

    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0)
    
def MovePaddle():
    global PadASpeed, PadA, PadBSpeed, PadB
    PadA = PadA.move(0, PadASpeed)
    PadB = PadB.move(0, PadBSpeed)
    if PadA.top <=0:
        print("Top of Screen")
        PadA = PadA.move(0,2)
        PadASpeed = 0
        PadA = PadA.move(0,PadASpeed)
    if PadB.top <=0:
        print("Top of Screen")
        PadB = PadB.move(0,2)
        PadBSpeed = 0
        PadB = PadB.move(0,PadBSpeed)
    if PadA.bottom >=600:
        print("bottom of Screen")
        PadA = PadA.move(0,-2)
        PadASpeed = 0
        PadA = PadA.move(0,PadASpeed)
    if PadB.bottom >=600:
        print("bottom of Screen")
        PadB = PadB.move(0,-2)
        PadBSpeed = 0
        PadB = PadB.move(0,PadBSpeed)
        
        

    
    
    
    
    
    pygame.draw.rect(window, white, PadA)
    pygame.draw.rect(window, white, PadB)
def drawCenterLine():
    global screenWidth, screenHeight
    pygame.draw.line(window, white, (screenWidth//2,0), (screenWidth//2, screenHeight))
    
    
    
    
def drawScore(font):
    global scoreA, scoreB, ballLocation
    
    text= font.render(str(scoreA), True, red )
    window.blit(text,(200,30))
    text= font.render(str(scoreB), True, red)
    window.blit(text,(700,30))
     
    if ballLocation[0]<=0:
        scoreB = scoreB+1
        ballLocation = [500, 300]
    if ballLocation[0]>=1000:
        scoreA = scoreA+1
        ballLocation = [500, 300]


def gameOver():
    global scoreA, scoreB
    if scoreA == 7:
        text = font.render(('Player1 Wins'), True, red )
        window.blit(text,(500,300))
        
    if scoreB == 7:
        text = font.render(('Player2 Wins'), True, red )
        window.blit(text,(500,300))
    if scoreA ==8:
        scoreA = 0
        scoreB = 0
    if scoreB ==8:
        scoreB = 0
        scoreB = 0
        
def changeSize(Size):
    global radius
    radius = Size
    
    
    
 
    
    
    
timer = pygame.time.Clock()

screenWidth=1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = 6
ballSpeedy = 3
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
radius = 20
ballLocation = [500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))



scoreA=0
scoreB=0
pygame.font.init()
font = pygame.font.Font(None,24)
PadA = pygame.Rect((0,150), (25,200))
PadASpeed = 0
PadB = pygame.Rect((975,150), (25,200))
PadBSpeed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PadBSpeed = -5
            if  event.key == pygame.K_DOWN:
                PadBSpeed = 5
            if event.key == pygame.K_s:
                PadASpeed = 5
            if  event.key == pygame.K_w:
                PadASpeed = -5
            if event.key == pygame.K_1:
                changeSize(10)
            if event.key == pygame.K_2:
                changeSize(20)
            if event.key == pygame.K_3:
                changeSize(30)
            if event.key == pygame.K_4:
                changeSize(40)
            if event.key == pygame.K_5:
                changeSize(50)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PadBSpeed = 0
            if event.key == pygame.K_DOWN:
                PadBSpeed = 0
            if event.key == pygame.K_s:
                PadASpeed = 0
            if event.key == pygame.K_w:
                PadASpeed = 0
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
   
       
    timer.tick(60)
    window.fill(black)
    drawCenterLine()
    drawScore(font)
    MoveBall()
    gameOver()
    MovePaddle()
    pygame.display.flip()
    #check quit event
    #check up, down, spacebar event