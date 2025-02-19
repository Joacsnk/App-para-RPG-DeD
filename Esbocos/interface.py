class Menu: #inicio
    
    def __init__(self): #cria e reseta a opcao
        self.opcao = 0
        
    def interface(self): #GUI simples 
        print('---------------D&D---------------\n')
        
    def escolherOpcao(self): #escolhe qual opção será a escolhida
        self.opcao = int(input('DADOS (1)\nSAIR (2)\n\nESCOLHA SUA OPÇÃO: '))
        
    def processarEscolha(self): #processa a escolha e roda a proxima página
        match self.opcao:
            case 1:
                from escolhadedados import Dados #importando o arquivo dos dados
                print('\n' * 130)
                dados = Dados()
                dados.inicio()
            case 2:
                exit()
            case _:
                print('\n' * 130)
                print("ERRO - VALOR INVÁLIDO\n")
                self.escolherOpcao()
                self.processarEscolha()
            
    def iniciar(self):
        self.interface()
        self.escolherOpcao()
        self.processarEscolha()
if __name__ == "__main__":
    jogo = Menu()
    jogo.iniciar()