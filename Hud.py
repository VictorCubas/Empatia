import pygame
import random

BLANCO = ( 255, 255, 255 )
VERDE = ( 0, 255, 0 )
ROJO = ( 255, 0, 0 )

class Hud( ):
    posInicialAncho = 110
    anchoBarraRoja = 0
    posAltoHub = 35
    tamanioTexto = 25

    def __init__( self ):
        self.barraVerde = pygame.Rect(10, self.posAltoHub, 100, 20)

    def draw( self, ventana, esMalo ):

        self.dibujarTexto( ventana )

        pygame.draw.rect( ventana, VERDE, self.barraVerde )

        if esMalo:
            cant_karmaMenos = random.randint( 1, 5 )
            if self.posInicialAncho > 10:
                self.posInicialAncho -= cant_karmaMenos
                self.anchoBarraRoja += cant_karmaMenos

        if self.anchoBarraRoja > 0:          
            self.barraRoja = pygame.Rect( self.posInicialAncho, self.posAltoHub, self.anchoBarraRoja, 20)
            pygame.draw.rect( ventana, ROJO, self.barraRoja )

    def dibujarTexto( self, ventana ):
        self.fuente = pygame.font.Font(None, self.tamanioTexto )
        self.texto = self.fuente.render("karma-Level", 1, BLANCO )

        self.pos = (10, 10 )
        ventana.blit( self.texto, self.pos )
