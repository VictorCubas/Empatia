#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

#BLANCO = (255,255,255)
#ROJO = (255,0,0)

class Jugador( ):
    tileAncho = 0
    tileAlto = 0
    posObjMatriz = None

    def __init__(self, tileAnch, tileAlt, imagen ):
        #self.image = pygame.image.load( 'imagenes/jugador.png' )
        self.image = imagen
        self.tileAncho = tileAnch
        self.tileAlto = tileAlt
        self.rect = self.image.get_rect()
#        posicionActual = self.rect

        self.spriteJugador = pygame.sprite.Sprite()
        self.spriteJugador.image = self.image
        self.spriteJugador.rect = self.rect

    def draw(self, ventana):
        "Muestra al personaje en pantalla."
        #ventana.blit(self.image, self.rect)
        ventana.blit( self.spriteJugador.image, self.spriteJugador.rect )

    def setPosicionInicial( self, xPosicion, yPosicion ):
        self.rect.x = xPosicion
        self.rect.y = yPosicion

    def posicionActual( self, x, y ):
        pos_actual = ( self.tileAncho * y  , self.tileAlto * x)
        return pos_actual

    def moverSe( self, incremento, ir_a, mapa ):
        #print "pos_jugador"
        #print "(%d, %d)" % (mapa.getXDelJugador( ), mapa.getYDelJugador( ) )
        #pygame.time.wait(200)
        self.rect.x += incremento[ 0 ]
        self.rect.y += incremento[ 1 ]

        distx = abs( ir_a[ 0 ] - self.rect.x ) 
        disty = abs( ir_a[ 1 ] - self.rect.y )
        tdistx = ( abs( incremento[ 0 ] ) * 1 )
        tdisty = ( abs( incremento[ 1 ] ) * 1 )
    
        if  distx <= tdistx and disty <= tdisty:
            self.rect.x = ir_a[ 0 ]
            self.rect.y = ir_a[ 1 ]

            return True
        else:
            return False

    def getPosicionsObjetivo( self, moverJugadorA, mapaLogico ):
        ir_a = None
        yMapa = mapaLogico.getYDelJugador( )
        xMapa = mapaLogico.getXDelJugador( )
        xMapaDim = mapaLogico.getDimX( )
        yMapaDim = mapaLogico.getDimY( )
        mapa = mapaLogico.getMapa()

        if moverJugadorA == "DERECHA":
            if yMapa < yMapaDim - 1:
                if mapa[ xMapa ][ yMapa + 1 ] == '0':
                    #ir_a = ( xMapa * self.tileAlto, ( yMapa + 1 ) * self.tileAncho )
                    ir_a = ( ( yMapa + 1 ) * self.tileAncho, xMapa * self.tileAlto )
                    self.posObjMatriz = (yMapa + 1, xMapa)

        if moverJugadorA == "IZQUIERDA":
            if yMapa > 0:
                if mapa[ xMapa ][ yMapa - 1 ] == '0':
                    #ir_a = ( xMapa * self.tileAlto, ( yMapa - 1 ) * self.tileAncho )
                    ir_a = ( ( yMapa - 1 ) * self.tileAncho, xMapa * self.tileAlto )
                    self.posObjMatriz = (yMapa - 1, xMapa)

        if moverJugadorA == "ABAJO":
            if xMapa < xMapaDim - 1:
                if mapa[ xMapa + 1 ][ yMapa ] == '0':
                    #ir_a = ( ( xMapa + 1 ) * self.tileAlto, yMapa * self.tileAncho )
                    ir_a = ( yMapa * self.tileAncho, ( xMapa + 1 ) * self.tileAlto )
                    self.posObjMatriz = (yMapa, xMapa + 1)

        if moverJugadorA == "ARRIBA":
            if xMapa > 0:
                if mapa[ xMapa - 1 ][ yMapa ] == '0':
                    #ir_a = ( ( xMapa - 1 ) * self.tileAlto, yMapa * self.tileAncho )
                    ir_a = ( yMapa * self.tileAncho, ( xMapa - 1 ) * self.tileAlto )
                    self.posObjMatriz = (yMapa, xMapa - 1)
        return ir_a

