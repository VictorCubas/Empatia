import random
import pygame
from pygame.locals import *

APPLE = 'M'

class Apple( ):
    x_y = None

    def __init__(self, imagen ):
        self.image = pygame.image.load( imagen )
        self.rect = self.image.get_rect( )
        self.rect.x = None
        self.rect.y = None

    def draw( self, ventana, tileAncho, tileAlto ):
        if self.x_y:
            self.rect.x = tileAncho * self.x_y[ 1 ]
            self.rect.y = tileAlto * self.x_y[ 0 ]
            ventana.blit( self.image, self.rect )

    def findPlace( self, mapa ):
        x = random.randInt( 7 )
        y = random.randInt( 13 )

        if mapa[x][y] == '0':
            return (x, y)

        return None

    def appleMain( self, mapa ):
        x_y = self.findPlace( mapa )
        x = self.x_y[ 0 ]
        y = self.x_y[ 1 ]

        if self.x_y:
            mapa[ x ][ y ] = APPLE
