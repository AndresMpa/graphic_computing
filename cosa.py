import pygame

pygame.init()


def Cart_conv(o, p):
    ptfin = [0, 0]
    ptfin[0] = o[0] + p[0]
    ptfin[1] = o[1] - p[1]
    return ptfin


def Poligono_Lineas(win, color, list):
    pygame.draw.polygon(win, color, list, 3)


def PoligonoSolido(win, color, list):
    pygame.draw.polygon(win, color, list)


def Traslacion(pt, cuant):
    ptfin = [0, 0]
    ptfin[0] = pt[0] + cuant[0]
    ptfin[1] = pt[1] + cuant[1]
    return ptfin


ROJO = [250, 0, 0]
VERDE = [0, 250, 0]

AnchoPantalla = 1000
AltoPantalla = 800
Origen = [500, 500]

Fin = False

AlzadaA = [0, 0]
AlzadaB = Traslacion(AlzadaA, [250, 0])
AlzadaC = Traslacion(AlzadaB, [0, -150])
AlzadaD = Traslacion(AlzadaA, [0, -150])
AlzadaE = Traslacion(AlzadaC, [0, -150])
AlzadaF = Traslacion(AlzadaE, [-150, 0])
AlzadaG = Traslacion(AlzadaC, [-150, 0])

AlzadaRectanguloInferior = [AlzadaA, AlzadaB, AlzadaC, AlzadaD]
AlzadaCuadradoSuperiror = [AlzadaC, AlzadaE, AlzadaF, AlzadaG]

PerfilA = [0, 0]
PerfilB = Traslacion(PerfilA, [100, 0])
PerfilC = Traslacion(PerfilB, [200, 0])
PerfilD = Traslacion(PerfilC, [100, 0])
PerfilE = Traslacion(PerfilD, [0, -150])
PerfilF = Traslacion(PerfilC, [0, -150])
PerfilG = Traslacion(PerfilC, [0, -300])
PerfilH = Traslacion(PerfilB, [0, -300])
PerfilI = Traslacion(PerfilB, [0, -150])
PerfilJ = Traslacion(PerfilA, [0, -150])

PerfilRectanguloIzquierdo = [PerfilA, PerfilB, PerfilI, PerfilJ]
PerfilRectanguloCentral = [PerfilB, PerfilC, PerfilG, PerfilH]
PerfilRectanguloDerecho = [PerfilC, PerfilD, PerfilE, PerfilF]

ventana = pygame.display.set_mode([AnchoPantalla, AltoPantalla])

while not Fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True
    Poligono_Lineas(ventana, ROJO, AlzadaRectanguloInferior)
    Poligono_Lineas(ventana, ROJO, AlzadaCuadradoSuperiror)
    Poligono_Lineas(ventana, VERDE, PerfilRectanguloIzquierdo)
    Poligono_Lineas(ventana, VERDE, PerfilRectanguloCentral)
    Poligono_Lineas(ventana, VERDE, PerfilRectanguloDerecho)
    pygame.display.flip()
