import math

def dms2dec(grad, min, seg):
    """
    Convierte coordenadas de grados minutos a segundos a decimal
    """
    if grad > 0:
        dec = grad + min/60.0 + seg/3600.0
    else:
        dec = grad - min/60.0 - seg/3600.0

    return dec


def distancia12(lat1, lon1, lat2, lon2):
    """
    Obtiene la distancia y el angulo (acimut) entre entre dos puntos de
    coordenadas geograficas P1 a P2
    """

    #  Conversion de GMS a DEC y posteriormente a radianes
    lat1rad = math.radians(dms2dec(*lat1))
    lon1rad = math.radians(dms2dec(*lon1))

    lat2rad = math.radians(dms2dec(*lat2))
    lon2rad = math.radians(dms2dec(*lon2))

    #  Si las latitudes y longitudes son iguales se encuentran en el mismo sitio geografico
    if lat1rad == lat2rad and lon1rad == lon2rad:
        return 0, 0

    #  Calculo de la distancia P1 a P2
    a = math.sin(lat1rad)*math.sin(lat2rad)
    b = math.cos(lat1rad)*math.cos(lat2rad)*math.cos(lon2rad - lon1rad)
    D = math.acos(a + b)  # Formula (2)

    d = 111.18*math.degrees(D)  # Formula (1)

    #  Calculo del angulo del P1 al P2
    ang_n = math.sin(lat2rad) - math.cos(D)*math.sin(lat1rad)
    ang_d = math.sin(D)*math.cos(lat1rad)

    try:
        ang12 = math.acos(round((ang_n / ang_d), 3))  # Formula (3)
    except:
        ang12 = 0

    #  Ajuste del angulo de conformidad con la condicion sin(lon2-lon1)
    if math.sin(lon2rad - lon1rad) < 0:
        ang12 = 360 - math.degrees(ang12)
    else:
        ang12 = math.degrees(ang12)

    # Regresa distancia y angulo
    return round(d, 2), round(ang12, 2)


# P1 --> Punto en Colombia
lat1 = (1, 35, 55)    # 1 35 55 N
lon1 = (-77, 43, 21)  # 77 43 21  W

# P2 --> Punto en Peru
lat2 = (-5, 33, 48)   # 5 33 48 S
lon2 = (-76, 27, 27)  # 76 27 27 W

distancia, angulo = distancia12(lat1, lon1, lat2, lon2)

print(
'''Distancia = {distancia} km
Angulo = {angulo} grados'''.format(distancia=distancia, angulo=angulo)
)
