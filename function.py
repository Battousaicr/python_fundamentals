# Nombre
# Bloque de codigo
# Pasar datos -> Parametros
# Resultado

# VARIABLES GLOBALES
VARIABLE_GLOBAL1 = "TEXTO"

def mi_primer_funcion():
    #Variables locales
    variable1 = 0
    total = variable1 + 100
    nombre = "Jose"
    return total, nombre

def persona(param_nombre, edad, fechNac):
    nombre_local = param_nombre
    edad_local = edad
    fecha_nac_local = fechNac 
    return nombre_local, edad_local, fecha_nac_local

# Llamar una funcion

#fecha_nac1 = persona()
#print(type(persona()))
persona1 = persona("JJ Brenes",18,"01/20/2005")
persona("Olde",13,"01/20/2010")

