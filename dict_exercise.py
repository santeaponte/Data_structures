# solicitud del texto al usuario.

texto = input('Ingresa el nombre del archivo:')
try:
  texto = open(texto)
  #print(texto.read())
except:
  print('El archivo no existe.')
  quit()

dict_1 = dict()
list_1 = list()

contador = 0
for correo in texto:
  correo = correo.strip()
  if correo.startswith('From'):
    correo = correo.split()
    #print(correo)
    if len(correo) > 2: # Solo quiero las lineas que contengan toda la info, no las que tengan solo el correo.
      #print(correo[1])
      contador += 1
      list_1.append(correo[1])


for cont in list_1:
  dict_1[cont] = dict_1.get(cont, 0) + 1
  
# for par buscar el máximo en un diccionario   
palabra = None
repetida = -1
for i,j in dict_1.items():
  if j > repetida:
    palabra = i
    repetida = j

print(palabra, repetida)

# otra forma:
  
max_key = max(dict_1 , key = dict_1.get)
max_value = dict_1[max_key]
print(max_key, max_value)
