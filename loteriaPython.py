#   coding: utf-8
import random



def sorteia (num=5):
    array_numero = []
    
    i = 0
    while i < 5:
        numero = random.randint(0, 40)
        if numero not in array_numero:
            array_numero.append(numero)
            array_numero.sort()
            i = i + 1
            

    for i in sorted(array_numero):
        print(array_numero)
    return array_numero
    

def start():
    numero_sorteado = sorteia(40)
    chute = int(input("Chute um numero: "))
    tentativa = 1
    while (chute < 0 or chute > 40) and tentativa <3:
        
        if tentativa == 3:
            print("Tentativas esgotaram")
            return
        print("Número inválido")
        chute = int(input("Chute novamente um numero: "))
        tentativa = tentativa + 1

    if chute in numero_sorteado:
        print("Você acertou")
    else:
        print("Você errou o número") 



def Main():
    start()
    
    

Main()









