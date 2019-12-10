import pygame

def main():
     
    
    pygame.init()
    
    pygame.display.set_caption("The Last Crusader")
     

    
    screen = pygame.display.set_mode((1000,800))
     
    running = True
     
    
    while running:

        player = pygame.image.load("./sprites/crusader.png") # charge l'image "crusader.png" depuis le dossier "sprites" dans la variable "player"
        screen.blit(player, (10,10))

        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                
                running = False
     
     

if __name__=="__main__":
    
    main()
