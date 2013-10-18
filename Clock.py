import pygame
from pygame.locals import *
import sys
#import so
from datetime import datetime

BLANCO = (255,255,255)

class Clock( ):
    initialTime = -1
    initialSec = -1
    sec_anterior = -1
    initialMin = -1
    min_anterior = -1
    minutos = -1
    #flag = -1
    sec_toShow = -1

    #def __init__( self ):

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
        #print "aaaaaa"

    def mainClock( self, ventana, gameover ):
        if not( gameover ):
            if self.initialTime == -1:
                self.initialTime = self.getTime( )
                self.initialTime = self.get_min_sec( self.initialTime )
                self.initialSec = int( self.initialTime[ 3 ] + self.initialTime[ 4 ] )
                #self.initialMin = int( self.initialTime[ 0 ] + self.initialTime[ 1 ] )

            currentTime = self.getTime( )
            currentTime = self.get_min_sec( currentTime )
            currentSec = int( currentTime[ 3 ] + currentTime[ 4 ] )
            #currentMin = int( currentTime[ 0 ] + currentTime[ 1 ] )

            self.sec_toShow = currentSec - self.initialSec
            #self.min_toShow = currentMin - self.initialMin
    
            if currentSec < self.initialSec:
    
                self.sec_toShow = currentSec + (60 - self.initialSec)
    
                if self.sec_anterior != self.sec_toShow:
                    #print self.sec_toShow
                    self.sec_anterior = self.sec_toShow

                    if self.sec_toShow == 0:
                        self.minutos += 1

                    #if self.min_anterior != self.min_toShow:
                    #    self.min_anterior = self.min_toShow
                    self.showTime( self.minutos , self.sec_toShow, ventana )
                    #else:
                    #    self.showTime( self.min_anterior, self.sec_toShow, ventana )
                    #self.showTime( self.sec_toShow, ventana )
                else:
                    self.showTime( self.minutos, self.sec_anterior, ventana )
            else:
                #print currentMin
                if self.sec_anterior != self.sec_toShow:
                    self.sec_anterior = self.sec_toShow

                    if self.sec_toShow == 0:
                        self.minutos += 1
    
                    #if self.min_anterior != self.min_toShow:
                        #print "hola"
                        #print "(%d, %d)" % (self.min_anterior, self.min_toShow)
                    #    self.min_anterior = self.min_toShow
                    self.showTime( self.minutos , self.sec_toShow, ventana )
                    #else:
                    #    self.showTime( self.min_anterior, self.sec_toShow, ventana )
    
                else:
                    self.showTime( self.minutos, self.sec_anterior, ventana )
        
        else:
            self.showTime( self.minutos, self.sec_anterior, ventana )


