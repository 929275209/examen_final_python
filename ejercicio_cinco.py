"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def datos_personales_alumno(nombre, apellido, edad, grado, seccion):
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Grado": grado,
        "Sección": seccion
    }
    return alumno

# Ejemplo de uso de la función
datos_jose = datos_personales_alumno("Jose", "Alvarez", "30", "APSTI", "III")
print(datos_jose)