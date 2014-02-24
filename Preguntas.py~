#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------------
# Módulos
#----------------------------------------------------------------------------------------------
import sys
import os
import pygame
import random
from pygame.locals import *
from ConfigParser import SafeConfigParser

#----------------------------------------------------------------------------------------------
# Constantes
#----------------------------------------------------------------------------------------------
NEGRO = (0, 0, 0)
BLANCO = (255,255,255)
COLORFUENTE = NEGRO

# Posicion del rectangulo en pantalla
XPOSRECT = 500
YPOSRECT = 300

# Posicion de la pregunta en pantalla
XPOSPRE = 100
YPOSPRE = 110

# Posicion de la opcion 1 en la pantalla 
XPOSOP1= 100
YPOSOP1 = 140

# Posicion de la opcion 2 en la pantalla
XPOSOP2 = 100
YPOSOP2 =  170

# Posicion de la opcion 3 en la pantalla
XPOSOP3 = 100
YPOSOP3 = 200

# Posicion de la opcion 4 en la pantalla
XPOSOP4 = 100
YPOSOP4 = 230

#----------------------------------------------------------------------------------------------
# Diccionario de Opciones, si no es filosofia pokemon
#----------------------------------------------------------------------------------------------
DICC_OPCIONES={ 
                '1' : 'Saludar',
                '2' : 'Responder' }


class Preguntas:

    def __init__(self):
        self.parser = SafeConfigParser()
        self.parser.read('config.ini')
        self.fuentePregunta = pygame.font.Font('freesansbold.ttf', 30)
        self.numeroPregunta = None
        self.fuente = None
        self.puntaje = 0

    def dibujarPregunta(self, ventana):

        rectanguloPregunta = pygame.Rect(100,100,XPOSRECT,YPOSRECT)
        pygame.draw.rect(ventana, BLANCO, rectanguloPregunta)

        self.numeroPregunta = random.randint(1,3)

        #obtiene la pregunta
        pregunta = self.parser.get('Pregunta' + str(self.numeroPregunta), 'pregunta')

        #se agrega acentos al texto
        pregunta = unicode(pregunta, "UTF-8")

        pregunta = self.fuentePregunta.render( pregunta , 1, COLORFUENTE)
        ventana.blit(pregunta, (XPOSPRE, YPOSPRE))

        fuenteOpciones = pygame.font.Font('freesansbold.ttf', 30)

        opcion1 = fuenteOpciones.render('1) '+self.parser.get('Pregunta' + str(self.numeroPregunta), 'opcion1'), 1,  COLORFUENTE)
        ventana.blit(opcion1, (XPOSOP1, YPOSOP1))

        opcion2 = fuenteOpciones.render('2) '+self.parser.get('Pregunta' + str(self.numeroPregunta), 'opcion2'), 1, COLORFUENTE)
        ventana.blit(opcion2, (XPOSOP2, YPOSOP2))

        opcion3 = fuenteOpciones.render('3) '+self.parser.get('Pregunta' + str(self.numeroPregunta), 'opcion3'), 1, COLORFUENTE)
        ventana.blit(opcion3, (XPOSOP3, YPOSOP3))
      
        opcion4 = fuenteOpciones.render('4) '+self.parser.get('Pregunta' + str(self.numeroPregunta), 'opcion4'), 1, COLORFUENTE)
        ventana.blit(opcion4, (XPOSOP4, YPOSOP4))

#----------------------------------------------------------------------------------------------
# Hay que ver si estas funciones deben estar o no en jugador o en el main principal :)
#----------------------------------------------------------------------------------------------
    def elegirOpcion(self, pregunta):
        respuestaJugador = None
        
        for event in pygame.event.get( ):

            if event.type == QUIT:
                pygame.quit
                sys.exit( 0 )

            elif event.type == KEYDOWN:
                if event.key == K_1:
                    respuestaJugador = '1'
                if event.key == K_2:
                    respuestaJugador = '2'
                if event.key == K_3:
                    respuestaJugador = '3'
                if event.key == K_4:
                    respuestaJugador = '4'

        return respuestaJugador
