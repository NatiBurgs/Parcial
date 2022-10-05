'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
from funciones import *

def starwars_app():
    lista_a_cargar = cargar_json("C:/Users/rocio/Desktop/Labo 1/Laboratorio1-Python/Parcial/PP_STARWARS/data.json")
    lista_starwars = lista_a_cargar[:]
    contenido = lista_starwars[:]

    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()

        if validar_respuesta(respuesta,"^[1-6]{1}$")==True:
            pass

        if(respuesta=="1"):
            key = "height"
            order = "asc"
            contenido = (nahuel_sort(lista_starwars,key,order))
            mostrar_lista(contenido)

        elif(respuesta == "2"):
            key = "height"
            contenido = buscar_max_genero(lista_starwars,key)
            mostrar_lista(contenido)

        elif(respuesta=="3"):
            key = "mass"
            order = "asc"
            contenido = nahuel_sort(lista_starwars,key,order)
            mostrar_lista(contenido)
            

        elif(respuesta=="4"):
            key = "name"
            personaje = input("Qué personaje desea buscar? \n")
            if personaje:
                mostrar_lista(buscador_personajes(lista_starwars,key,personaje))
            
        elif(respuesta=="5"):
            exportar_csv(contenido,"C:/Users/rocio/Desktop/Labo 1/Laboratorio1-Python/Parcial/PP_STARWARS/data.csv")
            print("Se ha realizado correctamente!")

        elif(respuesta=="6"):
            print("CHAU")
            break


starwars_app()

