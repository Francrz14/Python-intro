#%% Strings

print("Hola, ")
print("Esto es una nueva línea.")

print("Esto es una oración.", "Esto va en la misma línea.")

#%% String multilínea

"""
    comentario
"""
my_new_str = """
    Esto es un string de
    varias líneas.
"""

my_new_str2 = '''
    También funciona con comillas
    simples y
'''

my_new_str3 = """
    Si quiero 'comillas' dentro de
    string también puedo.
"""

print(my_new_str, my_new_str2, my_new_str3)

#%% Strings como arrays

my_new_str = "Este string es un array de chars y añado algo."

# Imprimimos cada palabra en una línea tomando cada caracter 
# del string como array de chars
palabra = ""
for char in my_new_str:
    if char != " ":
        palabra += char
    else:
        print(palabra)
        palabra = ""
print(palabra)
#%% Len

my_new_str = "String aleatorio para calcular len."
print("Longitud del str (con espacios):", len(my_new_str))

caracteres = 0
for char in my_new_str:
    if char != " ":
        caracteres += 1

print("Longitud del str (sin espacios):", caracteres)

# Ej. Descartar de un string una serie de caracteres -> @ # / 
chars_a_descartar = ["@", "#", "/"]
chars_aceptados = ["a", "b", "c"]
my_str = "Este stri#ng ti@ene cara//cteres incorrectos@#/."

# 1. Ignoramos chars en schars_a_descartar
caractered = 0
for char in my_str:
    if char not in chars_a_descartar:
        caracteres += 1
print(f"El str tiene {len(my_str)} caracteres en total y {caracteres} caracteres validos")

# 2. Limpiamos el str en una copia del str
my_new_str =""
carecteres = 0
for char in my_str:
    if char not in chars_a_descartar:
        my_new_str += char
        caracteres += 1
print(f"Longitud total del str es {len(my_str)} y caracteres válidos: {caracteres}.")
print("String original:", my_str)
print("Nuevo string:", my_new_str)

#%% Substring en strings

my_str = "Programar en Python3 mola mucho"
my_sub_str = "Python3"

print(my_sub_str in my_str)

# Ejemplo para comprobar substrings en str
asunto = "Este mail es para pepe"

if "Pepe" or "pepe" in asunto:
    print("Pepe ha recibido email:", True)
else: 
    print("Pepe no ha recibido emails.")

if "Juan" not in asunto:
    print("Juan no ha recibido emails")
