import serial

#----------------------Conexion con arduino -------------------

arduino = serial.Serial('COM6', 57600)


# DATOS DE ARDUINO
#   Funciones encargadas de obtener informacion del arduino
#   y organizarlas en listas.

def get_information(s):
    info = s.split(",")
    infofloat = []
    for i in info:
        infofloat.append(float(i))
    return infofloat

    
def get_arduino_data():
    a = arduino.readline()
    a = str(a)
    a = a[2:len(a)-5]
    l = get_information(a)
    return l

# SENSORES
#   Se usan las funciones cradas anteriormente para recolectar
#   los datos segun el sensor.

def acelerometro(): 
    """
    Se obtiene informacion de la forma aceleracion(a), rotacion(g)
    (ax,ay,az,gx,gy,gz)

    Se devuelve la lista l. 
    """
    # a = random.randint(0,100)
    return get_arduino_data()

def pulsioximetro():
    """
    Se obtiene informacion de la forma:
    pulso, concentracion
    """
    return get_arduino_data()


