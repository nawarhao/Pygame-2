#Import necessary libraries
import pygame
#initialize required modules
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500

#initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('adding image and background image')

#load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(), (200,200)
)

penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30))

#initialize font, render text, and set text position
text = pygame.font.Font(None, 36).render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 110))





#create a loop to run till the game is quit by the user
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
    
    #clean the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        display_surface.blit(background_image, (0,0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
            
    #make the changes visible
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
if __name__ == '__main__':
    game_loop()