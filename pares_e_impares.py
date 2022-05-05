def Pares_e_Impares(lista_de_numeros):
    
    pares = list()
    impares = list()

    for numero in lista_de_numeros:
        if numero%2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares


def PrintSaida(numeros_pares, numeros_impares):
    
    print(f"\nNúmeros pares: [ ", end="")   
    for numero in numeros_pares:
        print(f"{numero} ", end="")
    print("]")

    print(f"\nNúmeros ímpares: [ ", end="")     
    for numero in numeros_impares:
        print(f"{numero} ", end = "")
    print("]")


def main():

    numeros = [1,2,3,4,5,6,7,8,9,10]

    pares, impares = Pares_e_Impares(numeros)
    PrintSaida(pares, impares)
    print("\nFim!")


if __name__ == "__main__":
    main()