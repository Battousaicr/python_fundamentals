# Python Syntax - if statemt


number = 10

# Para string e int. 
# Es igual a
if 10 == 0:
    print("SI, es igual que 0")
else:
    print("NO, no es igual. ")

# strip() elimina los espacios al inicio y al final
string1 = " hola esta es una prueba "
string2 = "hola esta es una prueba 654654"
if string1.strip() == string2.strip():
    if 1 == 1:
        print("esto es un if anidado, Nested if.")
    elif 2 != 0:
        print("hola")
    else:
        print("else")

    print("si")
    print(string1.strip())
    print(string2.strip())
else:
    print("no")
    print(string1)
    print(string2)


# Es diferente a
if 10 != 0:
    print("SI, es diferente a 0")
else:
    print("NO, no es diferente. ")

if string1.strip() != string2.strip():
    print("si")
    print(string1.strip())
    print(string2.strip())
else:
    print("no")
    print(string1)
    print(string2)

# Operadores NUMERICOS
# Es mayor que a
if 10 > 0:
    print("SI, es mayor que 0")
else:
    print("NO, no es mayor que 0. ")

# Es menor que a
if 10 < 0:
    print("SI, es menor que 0")
else:
    print("NO, no es menor que 0. ")

# Es menor o igual que a
if -1 <= 0:
    print("SI, es menor o igual que 0")
else:
    print("NO, no es menor ni igual que 0. ")

# Es mayor o igual que a
if -1 >= 0:
    print("SI, es mayor o igual que 0")
else:
    print("NO, no es mayor ni igual que 0. ")



# For loops

list = [1,2,200,4,5]
num = 1 

for i in list:
    if num == i:
        print(i)
        break

db_usernames = ['example@domain.com','jartavia@akamai.com','homer@gmail.com']
username = 'homer@gmail.com'

for usr in db_usernames:
    if usr == username:
        print("login successfully")
        break






# solo para texto: lower() -> Convierte a minisculas

username = "JartAvia@akamai.com"
lower_username = username.lower()
print(lower_username)

# Solo para texto: upper() -> Convierte a mayuscula
username = "JartAvia@akamai.com"
upper_username = username.upper()
print(upper_username)
