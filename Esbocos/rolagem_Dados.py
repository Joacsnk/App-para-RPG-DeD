import defsgeneral as dg
from colorama import init, Fore
class rolagem_Dados():
    
    def inicio(self, exibir_inicializacao):
        self.cores()
        if exibir_inicializacao:
            self.to_roll, self.porcem = self.processar_Escolha(self.gui())
        self.rolar_Dado()
        self.processar_Opcao(self.escolha())
        
    def cores(self):
        init()
        self.cor_principal = Fore.YELLOW
        self.cor_secundaria = Fore.WHITE
        self.cor_erro = Fore.RED 
        self.cor_acerto = Fore.GREEN
        
    def gui(self):
        print(self.cor_secundaria + "┈ ┈ ┈ ┈ ┈ ◦•", self.cor_principal + "Rolagem de Dados", self.cor_secundaria +"•◦ ┈ ┈ ┈ ┈ ┈\n\n")
        print("1.  Rolar D100\n")
        print("2.  Rolar D100(%)\n")
        print("3.  Rolar D20\n")
        print("4.  Rolar D12\n")
        print("5.  Rolar D10\n")
        print("6.  Rolar D8\n")
        print("7.  Rolar D6\n")
        print("8.  Rolar D4\n")
        print(self.cor_erro + "9.  Voltar\n" + self.cor_secundaria)
        return str(input(''))
    
    def processar_Escolha(self, opcao):
        match opcao:
            case "1":
                return 100, False
            case "2":
                return 100, True
            case "3":
                return 20, False
            case "4":
                return 12, False
            case "5":
                return 10, False
            case "6":
                return 8, False
            case "7":
                return 6, False
            case "8":
                return 4, False
            case "9":
                from main import main
                dg.inicio_Interface(0, 0.7)
                Main = main()
                Main.iniciar(False)
            case _:
                dg.erro("Valor incorreto, tente novamente", 1)
                self.inicio(True)

    def rolar_Dado(self):
        dg.inicio_Interface(0, 0.7)
        resultado = dg.rolagem(self.to_roll, self.porcem)
        if resultado == self.to_roll:
            print(self.cor_acerto + "Dado rolado com sucesso!")
            print("Dado: {} (ACERTO CRÍTICO)".format(resultado))
        elif (resultado == 1) or ((resultado == 10) and (self.porcem == True)):
            print(self.cor_erro + "Dado rolado com sucesso!")
            print("Dado: {} (FALHA CRÍTICA)".format(resultado))
        else:
            print(self.cor_principal + "Dado rolado com sucesso!")
            print("Dado: {}".format(resultado))
        
    
    def escolha(self):
        print("\nO que deseja fazer agora?\n\n")
        print(self.cor_secundaria + "1. - Rolar novamente\n")
        print("2. - Escolher outro dado\n")
        print(self.cor_erro + "3 - Voltar\n" + self.cor_secundaria)
        return str(input(''))
        
    def processar_Opcao(self, opcao):
        match opcao:
            case "1":
                self.rolar_Dado()
                self.processar_Opcao(self.escolha())
            case "2":
                dg.inicio_Interface(0, 0.7)
                self.inicio(True)
            case "3":
                from main import main
                dg.inicio_Interface(0, 0.7)
                Main = main()
                Main.iniciar(False)
            case _:
                dg.erro("Valor incorreto, tente novamente", 1)
                self.processar_Opcao(self.escolha())