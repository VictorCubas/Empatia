import pygame
from pygame.locals import *
import sys
#import so
from datetime import datetime

BLANCO = (255,255,255)

class Clock( ):
    initialTime = None
    sec_anterior = -1
    minutes = 0
    seconds = 0
    sec_toShow = -1
    starting = True

    def get_min_sec( self, time ):
        mi_sec = time[14] + time[15] + time[16] + time[17] + time[18]
        return mi_sec

    def getTime( self ):
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return currentTime

    def showTime( self, minToShow, secToShow, ventana ):
        if minToShow < 10:
            minToShow = '0' + str( minToShow )
        else:
            minToShow = str( minToShow )        

        if secToShow < 10:
            secToShow = '0' + str( secToShow )
        else:
            secToShow = str( secToShow )

        timeToShow = minToShow + ':' + secToShow

        fuente = pygame.font.Font( None, 30 )
        time = fuente.render(timeToShow, 1, BLANCO )

        pos = (30, 60 )
        ventana.blit( time, pos )

    #def timeStoped( self, ):

    def mainClock( self, ventana, gameover, modoPregunta ):
        if modoPregunta:
            self.showTime( self.minutes, self.seconds, ventana )

        elif not( gameover ):

            self.showTime( self.minutes , self.seconds, ventana )

            if not ( self.initialTime ):
                self.initialTime = self.getTime( )
                self.initialTime = self.get_min_sec( self.initialTime )

            currentTime = self.getTime( )
            currentTime = self.get_min_sec( currentTime )
            currentSec = int( currentTime[ 3 ] + currentTime[ 4 ] )

            if self.starting:
                self.sec_anterior = currentSec
                self.starting = False

            #cada vez que exista un cambio en el clock del sistema, exitste un cambio
            #en el clock del juego

            if currentSec != self.sec_anterior:
                self.sec_anterior = currentSec
                if self.seconds < 59:
                    self.seconds += 1
                else:
                    self.minutes += 1
                    self.seconds = 0
        else:
            self.showTime( self.minutes, self.seconds, ventana )

