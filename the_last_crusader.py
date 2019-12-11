import pygame

def main():
     
    
    pygame.init()
    
    pygame.display.set_caption("The Last Crusader")
     

    
    screen = pygame.display.set_mode((1000,800), pygame.RESIZABLE) # une fenêtre


    player = pygame.image.load("./sprites/crusader.png").convert() # charge l'image "crusader.png" depuis le dossier "sprites" dans la variable "player"
    player.set_colorkey((0,255,0)) #rend la couleur verte (0,255,0) transparente
        
    screen.blit(player, (50,50)) # place le sprite à l'écran aux coordonnées 10,10 

    pygame.display.flip() # met à jour l'écran

    
    running = True
    
    while running:

        
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                
                running = False
     
     

if __name__=="__main__":
    
    main()
