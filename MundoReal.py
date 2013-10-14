#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pygame.locals import *
import pygame

class MundoReal():
    tileAncho = 0
    tileAlto = 0
    dimensionAncho = 0
    dimensionAlto = 0
    def __init__(self, tileAnch, tileAlt, ancho, alto):
        self.tileAncho = tileAnch
        self.tileAlto = tileAlt
        self.dimensionAlto = alto
        self.dimensionAncho = ancho

    def dibujarMundoReal( self, mapa, ventana, diccImagenes ):
        for yVentana in range (len(mapa)):	
            for xVentana in range ( len ( mapa[ yVentana ] ) ):
                if yVentana < len(mapa) - 1:
                    ventana.blit( diccImagenes[ 'pisoNormal' ], ( self.tileAncho * xVentana, self.tileAlto * yVentana ) )
                elif yVentana == len(mapa) - 1:
                    ventana.blit( diccImagenes[ 'pisoSombra' ], ( self.tileAncho * xVentana, self.tileAlto * yVentana ) )
                if mapa[yVentana][xVentana] == '3':
                    ventana.blit( diccImagenes[ 'companiero1' ], ( self.tileAncho * xVentana, self.tileAlto * yVentana ) )
                if mapa[yVentana][xVentana] == '#':
                    ventana.blit( diccImagenes[ 'mesa' ], ( self.tileAncho * xVentana, self.tileAlto * yVentana ) )

                if mapa[yVentana][xVentana] == '@':
                    ventana.blit( diccImagenes[ 'malo' ], ( self.tileAncho * xVentana, self.tileAlto * yVentana ) )

