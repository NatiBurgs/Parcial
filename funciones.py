import re
import json

'''
"results": [
		{
			"name": "Luke Skywalker",
			"height": "172",
			"mass": "77",
			"gender": "male"
		}
'''


def cargar_json(path:str)->list:
    """
    Abre un archivo del tipo json

    Parámetro: path:str
    Retorno: lista
    """
    buffer_dict = []
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["results"]

def validar_respuesta(respuesta:str,patron_regex:str)->bool:
    """
    Toma el str ingresado y realiza un match con el patron y retorna True si es el caso,
    si no retorna False.

    Parámetro: respuesta:str,patron_regex:str
    Retorno: bool
    """
    if respuesta:
        if re.match(respuesta,patron_regex,re.IGNORECASE):
            print("Valor correcto!")
            return True
        else:
            #print("Valor ingresado incorrecto! vuelva a intentarlo")
            return False 

def mostrar_lista(lista:list)->list:
    """
    Recorre una lista ingresada, si no se encuentra vacia la retorna formateada.

    Parátro: list
    Retorno: list
    """
    lista_mostrar = []
    if lista:
        for elemento in lista: 
            lista_mostrar.append(elemento)
            print("Nombre: {0} | Altura: {1} | Mass: {2} | Género: {3}".format(elemento["name"],elemento["height"],elemento["mass"],elemento["gender"]))
        return lista_mostrar 

def buscar_min_max(lista:list,key:str,order:str)->int:
    """
    Busca el mínimo en una lista de elementos dict con clave [key]

    Parámetro: lista de elementos, clave [key]
    Retorna: el índice del elemento encontrado o -1 si se encuentra vacia
    """
    retorno = -1
    if len(lista) > 0:
        i_min_max = 0
        for i in range (len(lista)):
            if (order == "desc" and lista[i][key] < lista[i_min_max][key]) or (order == "asc" and lista[i][key] > lista[i_min_max][key]):
                i_min_max = i
        retorno = i_min_max

    return retorno

def buscar_max_genero(lista:list,key:str)->list:

    lista_genero = []
    i_max = buscar_min_max(lista,key,"asc")
    for personaje in lista:
        lista_genero.append(personaje[i_max])
    return lista_genero    



def nahuel_sort(lista:list,key:str,order:str)->list:
    """
    Realiza un ordenamiento de la lista ingresada. 
    Busca el min/max entre la key de la lista ingresada,
    y lo guarda en una lista nueva vacía. El proceso continúa hasta que la lista ingresada se 
    encuentre vacía, y retorna una lista nueva con valores ordenados. 

    Parámetro: lista:list, key:str, order:str
    Retorno: lista_ordenada:list
    """
    lista_a_ordenar = lista.copy()
    lista_ordenada = []
    while(len(lista_a_ordenar) > 0):
        index_min = buscar_min_max(lista_a_ordenar,key,order)
        elemento = lista_a_ordenar.pop(index_min)
        lista_ordenada.append(elemento)
    return lista_ordenada

def buscador_personajes(lista:list,key:str,personaje:str)->list:
    """
    Recibe una lista y realiza un search del personaje ingresado

    Parámetro: lista:list, key:str, personaje:str
    Retorno: list
    """
    lista_personajes = []
    for elemento in lista:
        if re.search(personaje,elemento[key],re.IGNORECASE):
            lista_personajes.append(elemento)
    return lista_personajes

def exportar_csv(lista:list,path:str)->list:
    """
    Escribe en un archivo csv la lista ingresada.

    Parámetro: lista:list, path:str
    Retorno: lista en archivo csv
    """
    with open(path, "w") as file:
        for elemento in lista:
            file.write("Personaje: {0} | Altura: {1} | Peso: {2}| Género: {3}\n".format(elemento["name"],elemento["height"],elemento["mass"],elemento["gender"]))
