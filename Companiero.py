#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import string
import random
SPEED = 0.1

class Companiero( ):
    yaEsHora = -1        
    posXEnLaMatriz = 0
    posYEnLaMatriz = 0
    yaInteractuo = False
    yAnterior = 0
    si_interactua = False
    ir_a_del_compa = None
    pos_actual_compa = None
    incremento = None

    def __init__( self, x, y, tileAncho, tileAlto ):
        self.posXEnLaMatriz = x
        self.posYEnLaMatriz = y
        self.image = pygame.image.load( 'imagenes/companiero1.png' )
        self.rect = self.image.get_rect( )
        self.rect.x = y * tileAncho
        self.rect.y = x * tileAlto

    def draw( self, ventana ):
        "Muestra al personaje en pantalla."
        ventana.blit( self.image, self.rect )

    def posicionActual( self, tileAncho, tileAlto ):
        pos_actual = ( tileAncho * self.posYEnLaMatriz  , tileAlto * self.posXEnLaMatriz )
        return pos_actual

    def setPosicionMatriz( self, mapaMatriz, nro ):
        mapaMatriz[ self.posXEnLaMatriz ][ self.yAnterior ] = str(nro)

    def siInteractua( self, x, y, tileAncho ):
        porLaIzquierda = False
        porLaDerecha = False
        #if x == self.posXEnLaMatriz and not( self.yaInteractuo ):
        if x == self.posXEnLaMatriz:

            if ( y - self.posYEnLaMatriz == -2 or y - self.posYEnLaMatriz == -1):
                #IZQUIERDA
                porLaIzquierda = True

                #marca como ya interactuado                
                #self.yaInteractuo = True

            if (y - self.posYEnLaMatriz >= 0 and y - self.posYEnLaMatriz <= 2):
                #print "self.posYEnLaMatriz: %d" % self.posYEnLaMatriz
                #pygame.time.wait(5000)
                #DERECHA
                porLaDerecha = True

                #marca como ya interactuado
                #self.yaInteractuo = True

            if porLaIzquierda or porLaDerecha:
                return True

        return False

    def moverSe( self, ir_a, incremento ):
        #print "moviendose..."
        self.rect.x += incremento[ 0 ]
        self.rect.y += incremento[ 1 ]
        #print "%d, %d" % ( self.rect.x, self.rect.y )

        distx = abs( ir_a[ 0 ] - self.rect.x ) 
        disty = abs( ir_a[ 1 ] - self.rect.y )
        tdistx = ( abs( incremento[ 0 ] ) * 1 )
        tdisty = ( abs( incremento[ 1 ] ) * 1 )

        if  distx <= tdistx and disty <= tdisty:
            self.rect.x = ir_a[ 0 ]
            self.rect.y = ir_a[ 1 ]

            #self.yaInteractuo = True
            return True
        else:
            return False

    def getPosicionObjetivo( self, pos_actual_jugador, tileAncho ):
        ir_a = None

        self.yAnterior = self.posYEnLaMatriz
        #print "anterior: %d" % self.yAnterior
        
        if self.rect.x > pos_actual_jugador[ 0 ] and abs(self.rect.x - pos_actual_jugador[ 0 ]) != tileAncho:
            #por la izquierda
            ancho_objetivo = self.rect.x - tileAncho

            #guardamos el valor de 'y' para utilizar lo en setPosicionMatriz para evitar el clonado
            self.yAnterior = self.posYEnLaMatriz

            self.posYEnLaMatriz -= 1

            #if ancho_objetivo
            ir_a = ( ancho_objetivo, self.rect.y )

        if self.rect.x < pos_actual_jugador[ 0 ] and abs(self.rect.x - pos_actual_jugador[ 0 ]) != tileAncho:
            #por la derecha
            ancho_objetivo = self.rect.x + tileAncho

            #guardamos el valor de 'y' para utilizar lo en setPosicionMatriz para vitar el clanado
            self.yAnterior = self.posYEnLaMatriz

            self.posYEnLaMatriz += 1
            ir_a = ( ancho_objetivo, self.rect.y )

        return ir_a

    def getPosX( self ):
        return self.posXEnLaMatriz

    def getPosY( self ):
        return self.posYEnLaMatriz

    def xMas( self ):
        self.posXEnLaMatriz = self.posXEnLaMatriz + 1

    def yMas( self ):
        self.posYEnLaMatriz = self.posYEnLaMatriz + 1

    def xMenos( self ):
        self.posXEnLaMatriz = self.posXEnLaMatriz - 1
    def yMenos( self ):
        self.posYEnLaMatriz = self.posYEnLaMatriz - 1

  
    #def companieroMain( self, mapaLogico, jugador, tileAncho ):
    
    def debeInteractuar( self, mapaLogico, jugador, listaMapa, tileAncho, tileAlto ):
        modoPregunta = False
        xDelJugador = mapaLogico.getXDelJugador( )
        yDelJugador = mapaLogico.getYDelJugador( )

        #yaEsHora = 1
        self.si_interactua = self.siInteractua( xDelJugador, yDelJugador, tileAncho )

        if self.si_interactua:
            self.yaEsHora = random.randint(0, 5)
            #print "%d, %d" % (xDelJugador, yDelJugador)
            #print "yaEsHora: %d" % self.yaEsHora
            #pygame.time.wait(3000)
            if self.yaEsHora == 1:
                #pygame.time.wait(2000)
                self.pos_actual_compa = self.posicionActual( tileAncho, tileAlto )
                pos_actual = jugador.posicionActual( xDelJugador, yDelJugador ) 
            #print "jugador"
            #print pos_actual
                self.ir_a_del_compa = self.getPosicionObjetivo( pos_actual, tileAncho ) #TILE_ANCHO para moverse a la siguiente casilla
            #print "companiero"
            #print self.ir_a_del_compa

            #print "%d, %d" % ( self.posXEnLaMatriz, self.posYEnLaMatriz)
                if self.ir_a_del_compa:
            #si el jugador esta al alcance del companiero y no este en la casilla siguiente
                    a = ( self.ir_a_del_compa[ 0 ] - self.pos_actual_compa[ 0 ] ) * SPEED
                    b = ( self.ir_a_del_compa[ 1 ] - self.pos_actual_compa[ 1 ] ) * SPEED
                    self.incremento = ( a , b )

                else:
                #cuando el jugador esta pegado al companiero
                    modoPregunta = True

                #para que no vuelva a dibujar miestras el jugador se mueve
                #print incremento
            #print "incremento"
            #print self.incremento
                if self.incremento != None:
                    self.setPosicionMatriz( listaMapa, 0 )
            
            else:
                self.si_interactua = False

            return (self.ir_a_del_compa, modoPregunta)

    def interactuando( self, modoPregunta, listaMapa ):
        if self.yaEsHora == 1:
            '''print "ir_a_del_compa"
            print self.ir_a_del_compa
            print "modoPregunta: %d" % modoPregunta'''
            if self.ir_a_del_compa and not( modoPregunta ):
                #print self.incremento
                #print "[4][5]: %s" % listaMapa[4][5]
                #print "[4][6]: %s" % listaMapa[4][6]
                if self.moverSe( self.ir_a_del_compa, self.incremento ):
                    if self.si_interactua:
                        modoPregunta = True
   
                        a = ( self.pos_actual_compa[ 0 ] - self.ir_a_del_compa[ 0 ] ) * SPEED
                        b = ( self.pos_actual_compa[ 1 ] - self.ir_a_del_compa[ 1 ] ) * SPEED

                        self.ir_a_del_compa = self.pos_actual_compa
                        self.incremento = ( a , b )
                        self.si_interactua = False
                    else:
                        #recupera su posicion anterior
                        self.posYEnLaMatriz = self.yAnterior
                        self.ir_a_del_compa = None
                        #print " se movio ya***********"
                        #print listaMapa[4][5]
                        #print listaMapa[4][6]
                        #pygame.time.wait(3000)

                        self.pos_actual_compa = None
                        self.incremento = None
                        self.yaEsHora = -1
                        self.setPosicionMatriz( listaMapa, 3 )
                        #print "[4][5]: %s" % listaMapa[4][5]
                        #print "[4][6]: %s" % listaMapa[4][6]
                        #pygame.time.wait(3000)

            #print "modoPregunta: %d" % modoPregunta
            return (self.ir_a_del_compa, modoPregunta)

