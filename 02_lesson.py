# Data Type - int 
x = 1
y = 35656222554887711
z = -3255522
total = x + y
# len() - contar la cantidad de caracteres en string SIEMPRE tiene que ser string
cantidad_digitos = len(str(y))

print(total)
print(cantidad_digitos)

# Variable /  nombre = valor
# Configuracion

nombre1 = "persona 1" # El valor de la variable es Glauco. 
contrasena = "kljsd"
unsername = 'jartavia'
_abck = 'laksjdfoaijfalksf'
numero = 8
secret = contrasena + " : " + str(numero)
print(secret + "\n") # \n -> agregar una break line
texto1 = "Para que"


# type(secret) imprimir el tipo 
# Codigo del programa
#print("El nombre 1 es:  nombre1 tiene una cookie: _abck")
hostname = "www.akamai.com"
print("https://" + hostname + "/login")

hostname = "www.avis.com"
print("https://" + hostname + "/login")

# Data Type - float

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z)) 

suma2 = x + 1
print(type(suma2))


x = 35e3 # 35 x 10 ** 3 
y = 12E4 # 12 + 10 ** 4
z = -87.7e100

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z)) 

# Data Type - complex(i+j)

x = 3+5j
y = 5j
z = -5j

print(y)
print(type(x))


# Type Conversation

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
