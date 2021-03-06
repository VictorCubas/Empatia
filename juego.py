#!/usr/bin/env python
# -*- coding: utf-8 -*-

#--------
# Módulos
#--------
import sys
import pygame
import os
import time
from pygame.locals import *
from ElMapa import ElMapa
from MundoReal import MundoReal
from Jugador import Jugador
from Companiero import Companiero
from Preguntas import Preguntas
from Hud import Hud
from Malo import Malo
from Clock import Clock

#-----------
# Constantes
#-----------

ANCHO = 780
ALTO = 595
TILE_ANCHO = 60
TILE_ALTO = 85
BLANCO = (255, 255, 255)
ROJO = (255,0,0)
FPS = 120 #Frames por segundo

#------
#Clases
#------

def main( ):
    global mapa, block_list, all_sprites_list#, xMapa, yMapa, yMapaDim, xMapaDim
    global DICC_IMAGENES, JUGADOR_IMAGEN, ventana

    #block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    ventana = pygame.display.set_mode( ( ANCHO, ALTO ) )
    pygame.display.set_caption( "Juego" )

    #------------------------	
    # Diccionario de imagenes
    #------------------------

    DICC_IMAGENES = { 'mesa' : pygame.image.load( 'imagenes/mesa.png' ),
					  'jugador' : pygame.image.load( 'imagenes/jugador.png' ),
                      'pisoSombra' : pygame.image.load( 'imagenes/piso4.png' ),
                      'pisoNormal' : pygame.image.load( 'imagenes/pisoNormal.png' ),
                      'companiero1' : pygame.image.load( 'imagenes/companiero1.png' ),
                      'malo': pygame.image.load('imagenes/malo.png'),
                      'fondo' : pygame.image.load('imagenes/trans4.png'),
					}


    FPSreloj = pygame.time.Clock( )
    jugador = Jugador( TILE_ANCHO, TILE_ALTO, DICC_IMAGENES[ 'jugador' ] )

    jugador.setPosicionInicial( 360, 425 )
    y = int ( ANCHO / TILE_ANCHO )
    x = int ( ALTO / TILE_ALTO )

    hud = None
    malo1 = None
    malo2 = None
    malo3 = None
    companiero1 = None
    companiero2 = None
    companiero3 = None
    mundoReal = None
    mapaLogico = None
    listaMapa = None

    preguntas = Preguntas( DICC_IMAGENES[ 'fondo' ] )

    #all_sprites_list.add(jugador) #se usará una vez que tengamos más personajes

    moverSeCompaniero1 = None
    moverSeCompaniero2 = None
    moverSeCompaniero3 = None
    ir_a = None
    incremento = None
    direccion = None
    SPEED = 0.1
    #SPEED_MALO = 0.08
    moverJugadorA = None

    gameover = False
    jugarDenuevo = True
    #para la demostracion

    quedarSe = False
    respuesta = None
    muestraPregunta = True
    modoPregunta = False
    esMalo = False
    modoPausa = False
    respuestaJugador = None
    msjGameOver = True

    clock = None

    while True:

        FPSreloj.tick( FPS )

        if jugarDenuevo:
            #ESTO NO ME GUSTA
            #INICIALIZACION

            malo1 = Malo( DICC_IMAGENES[ 'malo' ], (6, 2), TILE_ANCHO, TILE_ALTO )
            malo2 = Malo( DICC_IMAGENES[ 'malo' ], (1, 0), TILE_ANCHO, TILE_ALTO )
            malo3 = Malo( DICC_IMAGENES[ 'malo' ], (0, 12), TILE_ANCHO, TILE_ALTO )

            jugador.setPosicionInicial( 360, 425)

            mundoReal = MundoReal( TILE_ANCHO, TILE_ALTO, ANCHO, ALTO )
            mapaLogico = ElMapa( x, y, jugador.rect.y / TILE_ALTO, jugador.rect.x / TILE_ANCHO)
            listaMapa = mapaLogico.leerMapa( 'mapa.txt' )
            mundoReal.dibujarMundoReal( listaMapa, ventana, DICC_IMAGENES )
            companiero1 = Companiero( 2, 8, TILE_ANCHO, TILE_ALTO )
            companiero2 = Companiero( 2, 2, TILE_ANCHO, TILE_ALTO )
            companiero3 = Companiero( 4, 5, TILE_ANCHO, TILE_ALTO )
            hud = Hud( )

            clock = Clock()
            moverSeCompaniero1 = False
            moverSeCompaniero2 = False
            moverSeCompaniero3 = False
            quedarSe = False
            ir_a = None
            incremento = None
            direccion = None
            moverJugadorA = None

            gameover = False

            msjGameOver = True
            respuesta = None
            muestraPregunta = True
            modoPregunta = False
            esMalo = False
            respuestaJugador = None

            jugarDenuevo = False

        if not( modoPregunta ):
            mundoReal.dibujarMundoReal( listaMapa, ventana, DICC_IMAGENES )
            jugador.draw( ventana )
            companiero1.draw( ventana )
            companiero2.draw( ventana )
            companiero3.draw( ventana )
            malo1.draw( ventana )
            malo2.draw( ventana )
            malo3.draw( ventana )

            hud.draw( ventana, esMalo )

            if gameover:
                if msjGameOver == True:
                    print "game over =("
                    msjGameOver = False
                game_over( ventana )

            esMalo = False

        clock.mainClock( ventana, gameover, modoPregunta, modoPausa )

        pygame.display.flip()

        if modoPausa == False and modoPregunta == False and gameover == False:
            if ir_a and quedarSe == False:
                if jugador.moverSe( incremento, ir_a, mapaLogico ):
                    actualizaElIndiceDelJugador( mapaLogico, direccion )
                    ir_a = None
                    incremento = None
                    direccion = None
    
                    tupla = companiero1.debeInteractuar( mapaLogico, jugador, listaMapa,TILE_ANCHO, TILE_ALTO )
                    if tupla:
                        modoPregunta = tupla[ 1 ]
                        moverSeCompaniero1 = tupla[ 0 ]
    
                        if modoPregunta:
                            muestraPregunta = True

                    tupla = companiero2.debeInteractuar( mapaLogico, jugador, listaMapa,TILE_ANCHO, TILE_ALTO )
                    if tupla:
                        modoPregunta = tupla[ 1 ]
                        moverSeCompaniero2 = tupla[ 0 ]
                        muestraPregunta = True

                    tupla = companiero3.debeInteractuar( mapaLogico, jugador, listaMapa,TILE_ANCHO, TILE_ALTO )
                    if tupla:
                        modoPregunta = tupla[ 1 ]
                        moverSeCompaniero3 = tupla[ 0 ]
                        muestraPregunta = True
    
                #continue
    
            if malo1.maloMain( jugador.posObjMatriz, mapaLogico, listaMapa, modoPregunta, TILE_ANCHO, TILE_ALTO, ir_a):
                gameover = True
            elif malo2.maloMain( jugador.posObjMatriz, mapaLogico, listaMapa, modoPregunta, TILE_ANCHO, TILE_ALTO, ir_a):
                gameover = True
            elif malo3.maloMain( jugador.posObjMatriz, mapaLogico, listaMapa, modoPregunta, TILE_ANCHO, TILE_ALTO, ir_a):
                gameover = True


            if ir_a and quedarSe == False:
                continue

            if moverSeCompaniero1:
                tupla = companiero1.interactuando( modoPregunta, listaMapa )
                modoPregunta = tupla[ 1 ]
                moverSeCompaniero1 = tupla[ 0 ]

                continue
            elif moverSeCompaniero2:
                tupla = companiero2.interactuando( modoPregunta, listaMapa )
                modoPregunta = tupla[ 1 ]
                moverSeCompaniero2 = tupla[ 0 ]

                continue
            elif moverSeCompaniero3:
                tupla = companiero3.interactuando( modoPregunta, listaMapa )
                modoPregunta = tupla[ 1 ]
                moverSeCompaniero3 = tupla[ 0 ]

                continue


        if modoPregunta:
            if muestraPregunta:
                print "Ha entrado en modo pregunta"
                print "esperando respuesta..."
                preguntas.dibujarPregunta( ventana )
                muestraPregunta = False

            if respuestaJugador:
                modoPregunta = False
                if respuestaJugador == '4':
                    esMalo = True

                respuestaJugador = None

            #blocks_hit_list = pygame.sprite.spsritecollide(jugador, block_list, True)

            #all_sprites_list.draw(ventana)  #se usará una vez que tengamos más personajes

            #if moverJugadorA == None: #con esto se evita que e mueva en otra direccion durante el movimiento

        for event in pygame.event.get( ): # event handling loop. Captura eventos del teclado una vez que se haya
                                    #presionado una tecla
            if event.type == QUIT:
                pygame.quit  
                sys.exit( 0 )

            elif event.type == KEYDOWN:
                if gameover:
                    if event.key == K_SPACE:
                        jugarDenuevo = True
                    elif event.key == K_ESCAPE:
                        pygame.quit
                        sys.exit( 0 )
                    
                elif modoPregunta:
                    if event.key == K_1:
                        respuestaJugador = '1'
                    if event.key == K_2:
                        respuestaJugador = '2'
                    if event.key == K_3:
                        respuestaJugador = '3'
                    if event.key == K_4:
                        respuestaJugador = '4'

                elif event.key == K_RIGHT:
                    moverJugadorA = "DERECHA"
                elif event.key == K_LEFT:
                    moverJugadorA = "IZQUIERDA"
                elif event.key == K_DOWN:
                    moverJugadorA = "ABAJO"
                elif event.key == K_UP:
                    moverJugadorA = "ARRIBA"
                elif event.key == K_SPACE:
                    if not( modoPausa ):
                        modoPausa = True
                    else:
                        modoPausa = False
                elif event.key == K_q:
                    if not( quedarSe ):
                        quedarSe =  True
                    else:
                        quedarSe = False

        if moverJugadorA != None:
            puedeMoverse = mapaLogico.estaLibre( moverJugadorA, mapaLogico )

            if puedeMoverse:
                #esMalo = True
                ir_a = jugador.getPosicionsObjetivo( moverJugadorA, mapaLogico )
                pos_actual = jugador.posicionActual( mapaLogico.getXDelJugador( ) , mapaLogico.getYDelJugador( ) )
                incremento = ( ( ( ir_a[ 0 ] - pos_actual[ 0 ] ) * SPEED ), ( ( ir_a[ 1 ] - pos_actual[ 1 ] ) * SPEED ) )
                direccion = moverJugadorA


    return 0

def game_over( ventana ):
    jugarDenuevo = False

    fuente = pygame.font.Font(None, 100 )
    game_over = fuente.render("GAME OVER", 1, BLANCO )

    pos = (182, 212 )
    ventana.blit( game_over, pos )

    fuente = pygame.font.Font(None, 40)
    playAgain = fuente.render("Jugar de nuevo - Espacio", 1, ROJO )
    pos = (220, 302)
    ventana.blit( playAgain, pos )

    quitGame = fuente.render("Salir del juego - Escape", 1, ROJO )
    pos = (232, 337)
    ventana.blit( quitGame, pos )

def actualizaElIndiceDelJugador( mapaLogico, moverJugadorA ):
    if moverJugadorA == "DERECHA":
        mapaLogico.yMas( )
    elif moverJugadorA == "IZQUIERDA":
        mapaLogico.yMenos( )
    elif moverJugadorA == "ABAJO":
        mapaLogico.xMas( )
    elif moverJugadorA == "ARRIBA":
        mapaLogico.xMenos( )

if __name__ == '__main__':
   pygame.init( )
   main( )
