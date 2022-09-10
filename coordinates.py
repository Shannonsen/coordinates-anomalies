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

cities = []


class temp:
     def __init__(self, feb, jun, dic):
        self.feb = feb
        self.jun = jun
        self.dic = dic
class city:
    def __init__(self, name, latitude, longitude, tempEsp, tempMin, tempMax):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.tempEsp = tempEsp
        self.tempMin = tempMin
        self.tempMax = tempMax


cities.append(city("Aguascalientes", (21, 52, 51), (102, 17, 46), temp(15, 22.5, 14), temp(4, 16, 4), temp(23.8, 32.9, 21.8)))
cities.append(city("Mexicali", (32, 39, 48), (115, 28, 4), temp(15.3, 33.2, 13.1), temp(-8, 9.1, -8), temp(34, 51.4, 31.3)))
cities.append(city("La Paz", (24, 8, 55), (110, 18, 24), temp(10, 23, 11), temp(6, 18, 6), temp(29, 41, 28)))
cities.append(city("San Francisco de Campeche", (19, 50, 55), (90, 31, 31), temp(24.7, 29.2, 24), temp(13, 17, 12.3), temp(39, 43, 40)))
cities.append(city("Tuxtla Gutierrez", (16, 45, 11), (93, 6, 56), temp(24.3, 27.2, 23.3),temp(9.8, 17.5, 8.1), temp(40.1, 41.2, 36.6)))
cities.append(city("Chihuahua", (28, 38, 12), (106, 4, 35), temp(11.8, 27.6, 9.4), temp(-18, 9.4, -12), temp(32, 41.2, 28)))
cities.append(city("Ciudad de México", (19, 25, 10), (99, 8, 44), temp(16.2, 19.5, 14.9),temp(-4.2, 0, -3), temp(33.5, 33.5, 29.4)))
cities.append(city("Saltillo", (25, 25, 23), (100, 59, 31), temp(13.6, 23.2, 12.7),temp(-14.4, 6.5, -18), temp(33, 40.5, 31)))
cities.append(city("Victoria de Durango", (24, 1, 22), (104, 39, 16),temp(12.2, 22.2, 11.3),temp(-12, 3.5, -10), temp(32, 38.9, 32)))
cities.append(city("Chilpancingo de los Bravo", (17, 33, 7), (99, 30, 5),temp(21.1, 24.1, 19.9),temp(0.5, 3.4, 0.8), temp(39.6, 36.3, 34)))
cities.append(city("Pachuca de Soto", (20, 7, 21), (98, 44, 10), temp(12.1, 15.6, 11.6),temp(-6, 0, -7), temp(29, 33.0, 26.0)))
cities.append(city("Guadalajara", (20, 40, 36), (103, 20, 51), temp(18.4, 23.9, 17.5),temp(0, 10, -1), temp(38, 38.5, 33)))
cities.append(city("Toluca de Lerdo", (19, 17, 32), (99, 39, 14), temp(11.4, 15.7, 10.7),temp(-6.6, 3.8, -5), temp(30, 31, 31)))
cities.append(city("Morelia", (19, 42, 10), (101, 11, 32), temp(8.5, 5.5, 7.5),temp(7, 14, 7), temp(24, 27, 22)))
cities.append(city("Cuernavaca", (18, 55, 7), (99, 14, 3), temp(19.9, 22.9, 18.9),temp(5.9, 10, 5), temp(37, 36, 34)))
cities.append(city("Tepic", (21, 30, 0), (104, 54, 0), temp(18, 23.4, 18.3),temp(0.4, 4.7, 2.5), temp(33.2, 37.6, 45.5)))
cities.append(city("Monterrey", (25, 40, 17), (100, 18, 31), temp(16.6, 27.9, 15.1),temp(-7.0, 11.5, 9.1), temp(39.5, 45, 38.0)))
cities.append(city("Oaxaca de Juarez", (17, 3, 38), (96, 43, 31), temp(19, 22.1, 17.7),temp(0, 7.9, -4.5), temp(37, 40, 34)))
cities.append(city("Puebla de Zaragoza", (19, 3, 5), (98, 13, 4), temp(15, 19.4, 14.5 ),temp(-1.5, 5.0, -6.0), temp(32, 34, 30.5)))
cities.append(city("Santiago de Queretaro", (20, 35, 17), (100, 23, 17),temp(16.2, 21.9, 15.5),temp(-1.8, 4.5, -1.5), temp(30, 35.5, 28.2)))
cities.append(city("Chetumal", (18, 29, 38), (88, 17, 52), temp(24.4, 28.6, 23.68),temp(5, 18.5, 0), temp(36.5, 37.5, 39)))
cities.append(city("San Luis Potosi", (22, 8, 59), (100, 58, 30), temp(14.7, 20.4, 6.4),temp(-6.5, 6, -12), temp(35, 37, 29.5)))
cities.append(city("Cualiacán", (24, 47, 25), (107, 23, 16), temp(20.1, 29.5, 20.2),temp(1, 10, 3), temp(42, 46.5, 37)))
cities.append(city("Hermosillo", (29, 4, 30), (110, 57, 30),temp(18.5, 31.8, 17.1),temp(-5, 15.2, -7), temp(38, 49.5, 36)))
cities.append(city("Villahermosa", (17, 59, 13), (92, 55, 10), temp(24.5, 32.6, 24.1),temp(12.1, 21.2, 10.9), temp(38, 48.3, 38)))
cities.append(city("Ciudad Victoria", (23, 44, 10), (99, 8, 46), temp(18.2, 28.3, 17.2),temp(-3, 12.5, -6), temp(39, 48.5, 39)))
cities.append(city("Xalapa - Enriquez", (19, 31, 52), (96, 54, 57), temp(16.5,21.1,16.4),temp(0,9,0.9), temp(33.4,36,32.5)))
cities.append(city("Mérida", (20, 58, 0), (89, 37, 0), temp(20.4, 28.5, 20),temp(5, 14, 5), temp(38.5, 41.5, 38.5)))

# P2 --> Punto en Peru - Ejemplo
lat2 = (-5, 33, 48)   # 5 33 48 S
lon2 = (-76, 27, 27)  # 76 27 27 W

for capital in cities:
    distancia, angulo = distancia12(capital.latitude, capital.longitude, lat2, lon2)
    print(
        """ Ciudad = {nombre}
Distancia = {distancia} km
Angulo = {angulo} grados""".format(
            nombre=capital.name,distancia=distancia, angulo=angulo
        )
    )

