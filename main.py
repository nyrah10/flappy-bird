import random
import sys
import pygame
from pygame.locals import *

# Constants
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'resources/sprites/kittysmall.png'
BACKGROUND = 'resources/sprites/bg.jpeg'
PIPE = 'resources/sprites/pipe.png'


# Define the welcomeScreen function
def welcomeScreen():
  # Initialize positions
  playerx = int(SCREENWIDTH / 5)
  playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
  messagex = int(SCREENWIDTH / 5)
  messagey = int(SCREENHEIGHT * 0.13)
  basex = 0

   # Drawing Rectangle for playbutton
  playbutton = pygame.Rect(108,222,68,65)

  while True:
    for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYDOWN
                                and event.key == K_ESCAPE):
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN and (event.key == K_SPACE
                                      or event.key == K_UP):
        # Code to start the game or perform related actions
        pass
      
       #This will make the cursor to arrow again if we move out our cursor from playbutton
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
      if pygame.mouse.get_pos()[0] > playbutton[0]  and pygame.mouse.get_pos()[0] < playbutton[0] + playbutton[2]:
                if pygame.mouse.get_pos()[1] > playbutton[1]  and pygame.mouse.get_pos()[1] < playbutton[1] + playbutton[3]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    pygame.mouse.get_pos()

                if playbutton.collidepoint(pygame.mouse.get_pos()): #checking if mouse is collided with the play button
            
                 if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #checking if mouse has been clicked
                    mainGame()

    # Update screen
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))
    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
    SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def mainGame():
  playerx = int(SCREENWIDTH / 5)
  playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
  basex = 0

  while True:
    for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYDOWN and event.key == K_UP):
        return

    # Update player position
    playery += 5  # Example: Move player downward by 5 pixels per frame

    # Check for collisions with ground
    if playery >= GROUNDY:
      playery = GROUNDY

    # Display elements on screen
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))
    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


if __name__ == "__main__":
  pygame.init()
  FPSCLOCK = pygame.time.Clock()
  pygame.display.set_caption('Flappy Kitty With Cleo Catra')

  # Load game resources
  GAME_SPRITES['numbers'] = (
    # Load numbers here
  )
  GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
  GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
  GAME_SPRITES['message'] = pygame.image.load(
    'resources/SPRITES/messagewithkitty.png').convert_alpha()
  GAME_SPRITES['base'] = pygame.image.load(
    'resources/SPRITES/base.png').convert_alpha()
  GAME_SPRITES['pipe'] = (pygame.transform.rotate(
    pygame.image.load(PIPE).convert_alpha(),
    180), pygame.image.load(PIPE).convert_alpha())

  GAME_SOUNDS['die'] = pygame.mixer.Sound('resources/audio/die.wav')
  GAME_SOUNDS['hit'] = pygame.mixer.Sound('resources/audio/hit.wav')
  GAME_SOUNDS['point'] = pygame.mixer.Sound('resources/audio/point.wav')
  GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('resources/audio/swoosh.wav')
  GAME_SOUNDS['wing'] = pygame.mixer.Sound('resources/audio/wing.wav')

  while True:
    welcomeScreen()
    mainGame()

while True:
  for event in pygame.event.get():
    ##game closes if user clicks on cross or escape button##
    if event.type== QUIT or (event.type== KEYDOWN and event.key == K_ESCAPE):
        pygame.quit()
        sys.exit()

    import pygame
from pygame.locals import *

def main():
    pygame.init()
    # Initialize other game-related settings
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
                
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                handle_jump_event()
                
        # Update game logic and draw game graphics
        
        pygame.display.update()

def handle_jump_event():
    # Handle the jump event logic here
    pass

if __name__ == "__main__":
    main()

    

    
else:
    SCREEN.blit(GAME_SPRITES['background'], (0, 0))  # Corrected the blit line
    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
    SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int (SCREENHEIGHT/2)
    basex = 0

#CREATING PIPES IN THE GAME#
getRandomPipe()

pipe = [ {'x': x value for pipe, 'y': y1} #values for upper pipe
         {'x': x value for pipe, 'y': y2}  #values for lower pipe
         ]
y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 *offset)) #COORDINATES MAY BE OFF SO MIGHT CHANGE#
y1 = pipeHeight - y2 + offset
  
pipe = [
{'x':pipeX,'y':-y1}, #upperpipes
{'x':pipeX,'y':y2}
]
return PIPE

#Creating new upper and lower pipes in game#
newPipe1= getRandomPipe()
newPipe2= getRandomPipe()

#upper pipe list#
upperPipes=[
   {'X':SCREENWIDTH + 200, 'y':newPipe1[0]['y']}
   'X':SCREENWIDTH + 200 + (SCREENWIDTH/2),'y':newPipe2[0]['y']}
]

#lower pipe list#
lowerPipes = [
   {'x':SCREENWIDTH + 200, 'y':newPipe1[1]['y']},
   {'x':SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[1]['y']}
]

pipeVelX = -4
playerVelY = -9
playerMaxVelY = 10 
playerMinVelY = -8
playerAccY = 1
 
playerFlapAccv = -8 # velocity while flapping
playerFlapped = False # It is true only when the bird is flapping

if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

                    #if player hits bottom of screen#
if playerFlapped:
        playerFlapped = False           
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

# move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
 
        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])
 
        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

while True:
   for event in pygame.event.get():
      
      if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
         pygame.quit()
         sys.exit()

         #sprites blit#

         SCREEN.blit (GAME_SPRITES)['background'], (0, 0))
    for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
        SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
        SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
    pygame.display.update()
    FPSCLOCK.tick(FPS)
