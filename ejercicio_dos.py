"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(numero):
    if numero <2:
        return False
    for i in range(2,int(numero**0.5)+1):
        if numero % i ==0:
            return False
        return True
    def filtrar_numeros_primos(lista_numeros):
        return list(filter(es_primo,lista_numeros))
    numeros=[2,5,7,9,4,2,8]
    numeros_primos=filtrar_numeros_primos(numeros)
    print(numeros_primos) 

   
