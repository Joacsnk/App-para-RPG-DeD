from os import system as sy
from time import sleep as sl
from random import randint, randrange
from colorama import init, Fore

init()
cor_erro = Fore.RED
cor_secundaria = Fore.WHITE

def inicio_Interface(tempo1, tempo2):
    sl(tempo1)
    sy('cls')
    sl(tempo2)

def erro(mensagem, tempo):
    sy('cls')
    sl(0.7)
    print(cor_erro + mensagem + cor_secundaria)
    sl(tempo)
    sy('cls')
    sl(0.7)

def rolagem(lados, porcem):
    if porcem:
        return randrange(10, lados + 1, 10)
    else:
        return randint(1, lados)