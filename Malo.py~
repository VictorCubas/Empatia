import pygame
from pygame.locals import *
import random
import copy

SPEED_MALO = 0.05
GAME_OVER = "gameover"
CASI_GAME_OVER = True
MALO_SIMBOLO = '@'
class Malo( ):
    i_nuevo = None
    j_nuevo = None
    casi_gameover = False
    ir_a_malo = None
    siguientePosMat = None
    flag = None
    increm = None
    tileAncho = None
    tileAlto = None

    def __init__( self, imagen, posEnLaMatriz, tile_ancho, tile_alto ):
        #self._game_data = game_data
        self.pos_maloMatriz = posEnLaMatriz
        self.imagenMalo = pygame.image.load( imagen )
        self.rect = self.imagenMalo.get_rect()
        self.rect.x = tile_ancho * posEnLaMatriz[ 1 ]
        self.rect.y = tile_alto * posEnLaMatriz[ 0 ]
        self.tileAlto = tile_alto
        self.tileAncho = tile_ancho

    def draw( self, ventana ):
        ventana.blit( self.imagenMalo, self.rect )

    def posActualMundoReal( self, tileAncho, tileAlto ):
        pos_actual = ( tileAncho * self.pos_maloMatriz[ 1 ], tileAlto * self.pos_maloMatriz[ 0 ] )
        return pos_actual

    def posObjMundoReal( self, pos_aMoverseMatriz, tileAncho, tileAlto ):
        x = pos_aMoverseMatriz[ 0 ]
        y = pos_aMoverseMatriz[ 1 ]
        #print pos_aMoverseMatriz
        pos_objetivo = ( tileAncho * y, tileAlto * x )
        return pos_objetivo

    def moverSe( self, ir_a, incremento ):
        #print "pos_malo"
        #print self.pos_maloMatriz
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

    def siGameOver( self, ir_a_jugador, posObjJugador, xJugador, yJugador ):
        a = xJugador == self.i_nuevo and yJugador == self.j_nuevo
        b = xJugador == self.pos_maloMatriz[0] and yJugador == self.pos_maloMatriz[1]
        if a and not(self.casi_gameover):
            print "CASI GAME OVER"
            print ir_a_jugador
            #pygame.time.wait(5000)
            #if ir_a_jugador == None:
            self.casi_gameover = True
            return True

    def getPorcentaje( self ):
        self.rect.x

    def findPosMatriz( self, posObjJugador,mapa, x, y ):
        i = self.pos_maloMatriz[ 0 ]
        j = self.pos_maloMatriz[ 1 ]

        self.i_nuevo = i
        self.j_nuevo = j

        if posObjJugador:
            xObjJugador = posObjJugador[1]
            yObjJugador = posObjJugador[0]

        if i > x:
            r = random.randint( 0, 1 )
            if j < y:
                if r == 0 and mapa[ i - 1 ][ j ] == '0':
                    self.i_nuevo = i - 1
                elif mapa[ i ][ j + 1 ] == '0':
                    self.j_nuevo = j + 1
                else:
                    self.i_nuevo = i - 1
            elif j > y:
                if r == 0 and mapa[ i - 1][ j ] == '0':
                    self.i_nuevo = i - 1
                elif mapa[ i ][ j - 1 ] == '0':
                    self.j_nuevo = j - 1
                else:
                    self.i_nuevo = i - 1
            else:
                #cuando estan sobre la misma columna
                if mapa[ i - 1 ][ j ] == '0':
                    self.i_nuevo = i - 1
                
        elif i < x:
            r = random.randint(0, 1)
            if j < y:
                if r == 0 and mapa[ i + 1 ][ j ] == '0':
                    self.i_nuevo = i + 1
                elif mapa[ i ][ j + 1 ] == '0':
                    self.j_nuevo = j + 1
                else:
                    self.i_nuevo = i + 1
            elif j > y:
                if r == 0 and mapa[ i + 1 ][ j ] == '0':
                    self.i_nuevo = i + 1
                elif mapa[ i ][ j - 1 ] == '0':
                    self.j_nuevo = j - 1
                else:
                    self.i_nuevo = i + 1
            else:
                if mapa[ i + 1 ][ j ] == '0':
                    self.i_nuevo = i + 1

        elif x == i and j == y:
            return GAME_OVER
        else:
            #cuando estan sobre la misma columna
            self.i_nuevo = i
            if j < y:
                if mapa[ i ][ j + 1 ] == '0':
                    self.j_nuevo = j + 1
                else:
                    r = random.randint( 0, 1 )
                    self.j_nuevo = j

                    if r == 0 and mapa[ i - 1][ j ] == '0':
                        self.i_nuevo = i - 1
                    elif mapa[ i + 1][ j ] == '0':
                        self.i_nuevo = i + 1
            elif j > y:
                if mapa[ i ][ j - 1 ] == '0':
                    self.j_nuevo = j - 1
                else:
                    r = random.randint( 0, 1 )
                    self.j_nuevo = j

                    if r == 0 and mapa[ i - 1][ j ] == '0':
                        self.i_nuevo = i - 1
                    elif mapa[ i + 1][ j ] == '0':
                        self.i_nuevo = i + 1

        '''if x == i_nuevo and y == j_nuevo:
        #if posObjJugador != None and xObjJugador == i_nuevo and yObjJugador == j_nuevo:
            print "aca  "
            print self.pos_maloMatriz
            print "(%d, %d)" % (i_nuevo, j_nuevo)
            print "(%d, %d)" % (x, y)
            print posObjJugador
            pygame.time.wait(5000)
            self.casi_gameover = True'''

        return ( self.i_nuevo, self.j_nuevo )
        

    def setMatriz( self, posicion_actual, mapa, caracter ):
        #se guarda la posicion actual
        #caracter puede ser '@' o '0'

        if caracter == MALO_SIMBOLO:
            #se setea la posicion del malo
            self.pos_maloMatriz = posicion_actual

        x = self.pos_maloMatriz[ 0 ]
        y = self.pos_maloMatriz[ 1 ]

        #puede ser seteado con '0' cuando su mueva de su luegar o con '@' cuando
        #se posicione en la nueva posicion
        mapa[ x ][ y ] = caracter

    def maloMain( self, posObjJugador, mapaLogico, listaMapa, modoPregunta, tileAncho, tileAlto, ir_a_jugador ):
        gameover = False

        #print "ir_a_jugador"
        #print ir_a_jugador

        xDelJugador = mapaLogico.getXDelJugador( )
        yDelJugador = mapaLogico.getYDelJugador( )

        if self.siguientePosMat == None:
            self.siguientePosMat = self.findPosMatriz( posObjJugador, listaMapa, xDelJugador, yDelJugador )

            if self.siguientePosMat == GAME_OVER:
                gameover = True
                return gameover
            #elif self.siguientePosMat == CASI_GAME_OVER:
            #   self.casi_gameover = True

            self.flag = False
        if self.flag == False:
                self.flag = True
                self.ir_a_malo = self.posObjMundoReal( self.siguientePosMat, tileAncho, tileAlto )
                pos_actual_malo = self.posActualMundoReal( tileAncho, tileAlto )

                a = ( self.ir_a_malo[ 0 ] - pos_actual_malo[ 0 ] ) * SPEED_MALO
                b = ( self.ir_a_malo[ 1 ] - pos_actual_malo[ 1 ] ) * SPEED_MALO
                self.increm = ( a , b )

                self.setMatriz( None, listaMapa, '0')

        
        if self.ir_a_malo and not( modoPregunta ):
            moviendose = self.moverSe( self.ir_a_malo, self.increm )
            if moviendose:
                self.setMatriz( self.siguientePosMat, listaMapa, '@')
                self.increm = None
                self.ir_a_malo = None
                self.siguientePosMat = None

        if self.siGameOver(ir_a_jugador, posObjJugador, xDelJugador, yDelJugador):
           print "+++game over+++"
           gameover = True
           return gameover

