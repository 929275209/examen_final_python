"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""

def numero_menor_mayor(lista_numeros):
    if not lista_numeros:
        return {},{}
    numero_menor=min(lista_numeros)
    numero_mayor=max(lista_numeros)
    return{"min":numero_menor,"max":numero_mayor}
numero= [4,7,10,4,1,0]
resultado=numero_menor_mayor(numero)
print(resultado)



