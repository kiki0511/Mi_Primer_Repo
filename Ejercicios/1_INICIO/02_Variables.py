# Variables

my_string_variable = "My string varibale"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variabels en un print
print(type(print(my_string_variable,str(my_int_variable), my_bool_variable)))
print("Esta es el valor de:", my_bool_variable)

# Algunas FC del sistema
print(len(my_string_variable)) # Indica numero total de caracteres

# Variables en una sola linea 
name , surname, alias, age = "Brais" , "Moure", "MoureDev" , 35
print("Me llamo:", name, surname, ". Mi edad es::", age, ". Y mi alias es :",alias)

# Inputs
""""
name = input("Ingrese su nombre: ") 
age = input("Ingrese su edad: ")    
print(name)
print (age) 
"""""
# Cambiamos su tipo
name =35
age = "Brais"
print(name)
print(age)
 
 # Forzamos el tipo
address: str = "Mi direccion"
address = 32
print (type(address)) 