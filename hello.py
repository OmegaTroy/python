print('hola mundo')

#*?  typos de datos
name = 'julian' #* String
num = 22 #* Int
altura = 1.56 #* Float
luz_perndida = True #* Booleanos

#TODO variables 

#*? Concatenacion
bienvenida = 'hola ' + name + ' como estas?'
bienvenida = f'hola {name} como estas?'

#*? borrar variables 
del altura


#TODO Operadores de pertenecia (in y not in)

#*? para buscar en una cadena de texto es una ( IN )
print('hola' in bienvenida) #* true

#*? para comprobar si no esta en una cadena de texto ( not in )
print('pedro' not in bienvenida) #* false


#TODO Datos Compuestos

#*? listas: una lista es con [], las listas si se modifican
lista = ['javaScript','node','express','python']

#*? tuplas: una tupla es con (), las tuplas no se modifican
tupla = ('javaScript','node','express','python')

#*? conjunto (set): un conjunto es con {}, los conjuntos son datos desordenados y se pueden modificar
conjunto = {'javaScript','node','express','python'}

#*? diccionario (dict)
diccionario = {
  'nombre': 'one piece',
  'cap':'indefinidos',
  'genero': 'aventura y peleas'
}