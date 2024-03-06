import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 640
altura =  480
Preto = (0,0,0)

tela = pygame.display.set_mode ((largura,altura))
pygame.display.set_caption ('Sprites')

class Sapo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites =[]
        self.sprites.append (pygame.image.load('animation-master/attack_1.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_2.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_3.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_4.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_5.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_6.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_7.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_8.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_9.png'))
        self.sprites.append (pygame.image.load('animation-master/attack_10.png'))
        self.atual = 0
        self.image =self.sprites [self.atual]
        self.image = pygame.transform.scale(self.image, (128*3,64*3))
        self.rect =self.image.get_rect ()
        self.rect.topleft =  300 ,255

        self.animar = False
    def atacar (self):
         self.animar = True 
    def update(self):
        if  self.animar == True:   
             self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
        self.image = self.sprites [int (self.atual)]
        self.image = pygame.transform.scale(self.image, (128*3,64*3))

todas_as_sprites  = pygame.sprite.Group()      
sapo = Sapo()   
todas_as_sprites.add(sapo)
imagem_fundo = pygame.image.load('cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo,(largura,altura))
relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill ((Preto))
    for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
         exit()
        if event.type == KEYDOWN:
           sapo.atacar() 
    tela.blit(imagem_fundo,(0,0))
    todas_as_sprites.draw(tela) 
    todas_as_sprites.update()    
    pygame.display.flip() 