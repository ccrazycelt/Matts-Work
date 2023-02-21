import pygame
import os
import sys

def main():
    # track the player's position, the screen draws from (0,0) in the top left
    player_x = 0
    player_y = 355

    # init the pygame module
    pygame.init()

    # control the main game loop with a boolean
    exit_game = False

    # load the background sprite, note we read the image from a file
    # and we use os.path.join to put the right "separator" between the 
    # folder name and file
    background = pygame.image.load(os.path.join("sprites","forest-background.png"))
    
    # TODO: now load the player sprite
    player = pygame.image.load(os.path.join("sprites","mage.png"))

    # set the screen resolution to the size of the background
    screen = pygame.display.set_mode(background.get_size())

    # set the title of the game
    pygame.display.set_caption("My cool game")


    # loop until we get a quit event
    while not exit_game:
        # pygame is event driven, so we have to get the events
        # because it needs to read input and draw events
        for event in pygame.event.get():
            # handle quit events
            if event.type == pygame.QUIT:
                exit_game = True

            # TODO: check for user input and update the player position
            
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_x += 50
                if event.key == pygame.K_a:
                    player_x -= 50
                
            
            # draw the background first
            screen.blit(background, (0,0))

            # TODO: now draw the player
            screen.blit(player, (player_x,player_y))
            

            # now flip the buffers! this puts the one we were blitting to in front
            pygame.display.flip()

    # clean up resources that pygame used
    pygame.quit()
    # and totally exit game/module
    sys.exit()

# run the main function if you execute this python file, note that
# importing this will not actually run main(), you'd have to do it yourself
if __name__ =="__main__":
    # call the main function
    main()