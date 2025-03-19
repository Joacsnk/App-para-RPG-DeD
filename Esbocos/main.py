import defsgeneral as dg
from os import system as sy
from colorama import init, Fore, Style 

class main:
    
    def __init__(self):
        init()

    def cores(self):
        self.cor_principal = Fore.YELLOW
        self.cor_secundaria = Fore.WHITE
        self.cor_erro = Fore.RED 
        
    def iniciar(self, exibir_inicializacao):
        self.cores()
        if exibir_inicializacao:
            self.inicializar()
        self.processar_Escolha(self.gui())
        
    def inicializar(self):
        dg.inicio_Interface(0, 0.7)
        print(self.cor_principal + 'Bem vindo ao Kriv, um programa feito para ajudar mestres e jogadores de RPG\n')
        dg.inicio_Interface(2, 0.5)

    def gui(self):
        print(self.cor_secundaria + '✦ — — — — —', self.cor_principal + 'Kriv', self.cor_secundaria + '— — — — — ✦\n\n')
        print('1.  Rolagem de dados\n')
        print(self.cor_erro + '2.  Sair \n' + self.cor_secundaria)
        return str(input(''))
        
    def processar_Escolha(self, opcao):
        match opcao:
            case "1":
                dg.inicio_Interface(0, 0.7)
                from rolagem_Dados import rolagem_Dados #importando o arquivo dos dados
                rolagem_dados = rolagem_Dados()
                rolagem_dados.inicio(True)
            case "2":
                dg.inicio_Interface(0, 0.5)
                sy("taskkill /F /IM cmd.exe")
            case _:
                dg.erro("Valor incorreto, tente novamente", 1)
                self.iniciar(False)
        
if __name__ == "__main__":
    Main = main()
    Main.iniciar(True)