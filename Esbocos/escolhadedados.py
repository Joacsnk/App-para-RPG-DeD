from random import randint
class Dados():
    
    def __init__(self):
        self.opcao = 0
        self.opcaorepetida = 0
    
    def interface(self): # GUI simples
        print('---Dados---\n')
        
    def escolherOpcao(self):
        self.opcao = int(input('\nESCOLHA A QUANTIDADE DE LADOS (OU ''0'' PARA SAIR): '))
        
    def processarOpcao(self):
        if self.opcao == 0:
            from interface import Menu 
            print('\n' * 130)
            menu = Menu()
            menu.iniciar()
        elif self.opcao > 0  and self.opcao < 4:
            print('\n' * 130)
            print('ERRO - - - Quantidade de lados insuficiente\n')
            self.inicio()
        elif self.opcao > 0:
            self.exibirRolagemDados()
        elif self.opcao < 0:
            print('\n' * 130)
            print('ERRO - - -Número inválido\n')
            self.inicio()
            
    def exibirRolagemDados(self):
        print('\n' * 130)
        print('O DADO CAIU NO NÚMERO: {}'.format(self.rolagemDados()))
        self.processarOpcaoRepetida()
    
    def rolagemDados(self):
        return randint(1, self.opcao)
    
    def processarOpcaoRepetida(self):
        self.opcaorepetida = int(input('ROLAR NOVAMENTE(1)\nTROCAR NÚMERO DOS DADOS(2)\nSAIR(3): '))
        match self.opcaorepetida:
            case 1:
                print('\n' * 130)
                self.exibirRolagemDados()
            case 2:
                print('\n' * 130)
                self.escolherOpcao()
            case 3:
                from interface import Menu 
                print('\n' * 130)
                menu = Menu()
                menu.iniciar()
            case _:
                print('\n' * 130)
                print('ERRO - - - Valor incorreto\n')
                self.processarOpcaoRepetida()
    
    def inicio(self):
        self.interface()
        self.escolherOpcao()
        self.processarOpcao()
