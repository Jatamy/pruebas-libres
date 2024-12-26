# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))
print("Este es el valor :", my_bool_variable)
# Algunas Funciones del sistema 
print(len(my_string_variable))

# variables en una sola linea ¡cuidado con abusar de esta sintaxis!
name, surname, alias, age = "jatamy", "gomez", "alsahara", 21
print("me llamo:", name, surname,"mi edad es", age, "y mi alias es:", alias)

# inputs
"""
name = input("what is your name? ")
age = input("how old are you? ")
print(name)
print(age)
"""
# cambiando su tipo
name = 23
age = "esdras"
print(name)
print(age)

# forzamos el tipo?
address : str = "mi dreccion"
address = True
address = 32
address = 32.5
print(type(address))
