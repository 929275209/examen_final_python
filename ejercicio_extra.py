"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
# Crear el diccionario con 5 tiendas comerciales
tiendas_comerciales = {
    1: {"nombre": "Tienda A", "horario": "9AM-6PM"},
    2: {"nombre": "Tienda B", "horario": "10AM-7PM"},
    3: {"nombre": "Tienda C", "horario": "8AM-5PM"},
    4: {"nombre": "Tienda D", "horario": "11AM-8PM"},
    5: {"nombre": "Tienda E", "horario": "10:30AM-6:30PM"}
}

# Función para editar el nombre de una tienda comercial
def editar_nombre_tienda(id_tienda, nuevo_nombre):
    tiendas_comerciales[id_tienda]["nombre"] = nuevo_nombre

# Función para actualizar el horario de atención de una tienda comercial
def actualizar_horario_atencion(id_tienda, nuevo_horario):
    tiendas_comerciales[id_tienda]["horario"] = nuevo_horario

# Función para eliminar una tienda comercial
def eliminar_tienda(id_tienda):
    del tiendas_comerciales[id_tienda]

# Ejemplo de uso de las funciones
print("Diccionario de tiendas comerciales antes de las modificaciones:")
print(tiendas_comerciales)

# Realizar las modificaciones
editar_nombre_tienda(2, "Nueva Tienda B")
actualizar_horario_atencion(3, "7AM-4PM")
eliminar_tienda(5)

print("\nDiccionario de tiendas comerciales después de las modificaciones:")
print(tiendas_comerciales)