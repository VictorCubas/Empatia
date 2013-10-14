#!/usr/bin/env python
import os
class ElMapa():
    xMapa = 0
    yMapa = 0
    xMapaDim = 0
    yMapaDim = 0
    mapa = None
    def __init__(self, x, y, indiceX, indiceY):
        self.xMapaDim = x
        self.yMapaDim = y
        self.xMapa = indiceX
        self.yMapa = indiceY

    def yMas( self ):
        self.yMapa = self.yMapa + 1
    def xMas( self ):
        self.xMapa = self.xMapa + 1
    def yMenos( self ):
        self.yMapa = self.yMapa - 1
    def xMenos( self ):
        self.xMapa = self.xMapa - 1
    def getXDelJugador( self ):
        return self.xMapa
    def getYDelJugador( self ):
        return self.yMapa
    def getDimX( self ):
        return self.xMapaDim
    def getDimY( self ):
        return self.yMapaDim

    def leerMapa(self, archivo):
        assert os.path.exists(archivo), 'No se pudo encontrar el archivo: %s' % (nombreArchivo)
        archivoMapa = open(archivo, 'r')
        contenido = archivoMapa.readlines()
        
        #crea una matriz
        self.mapa = [None] * self.xMapaDim
        for x in range( self.xMapaDim ):
    		self.mapa[ x ] = [None] * self.yMapaDim

        #incializa la matriz con el valor de contenido
        for x in range( self.xMapaDim ):
            for y in range( self.yMapaDim ):
                self.mapa[ x ][ y ] = contenido[ x ][ y ]
        
        print('Se creo mapa')
        archivoMapa.close()
        return self.mapa

    def estaLibre( self, moverJugadorA, mapaLogico ):
        puedeMoverse = False
        yMapa = mapaLogico.getYDelJugador( )
        xMapa = mapaLogico.getXDelJugador( )
        xMapaDim = mapaLogico.getDimX( )
        yMapaDim = mapaLogico.getDimY( )
        mapa = mapaLogico.getMapa()

        if moverJugadorA == "DERECHA":
            if yMapa < yMapaDim - 1:
                if mapa[ xMapa ][ yMapa + 1 ] == '0':
                    puedeMoverse = True

        if moverJugadorA == "IZQUIERDA":
            if yMapa > 0:
                if mapa[ xMapa ][ yMapa - 1 ] == '0':
                    puedeMoverse = True

        if moverJugadorA == "ABAJO":
            if xMapa < xMapaDim - 1:
                if mapa[ xMapa + 1 ][ yMapa ] == '0':
                    puedeMoverse = True

        if moverJugadorA == "ARRIBA":
            if xMapa > 0:
                if mapa[ xMapa - 1 ][ yMapa ] == '0':
                    puedeMoverse = True

        #print(puedeMoverse)
        return puedeMoverse

    def getMapa( self ):
       return self.mapa
