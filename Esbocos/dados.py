from random import randint
def escolha_de_dados():
    import interface
    pagina = True
    while pagina == True:
        print('---Dados---\n')
        tipo_de_dado = int(input('\nESCOLHA A QUANTIDADE DE LADOS (OU ''0'' PARA SAIR): '))
        if tipo_de_dado == 0:
            print('\n' * 130)
            interface.inicio()
        elif tipo_de_dado > 0:
            x = True
            while x == True:
                print('\n' * 130)
                print('O DADO CAIU NO NÚMERO: {}'.format(queda_dados(tipo_de_dado)))
                rolagem = int(input('ROLAR NOVAMENTE(1)\nTROCAR NÚMERO DOS DADOS(2)\nSAIR(3): '))
                match rolagem:
                    case 1:
                        x = True
                    case 2:
                        print('\n' * 130)
                        x = False
                    case 3:
                        x = False
                        pagina = False
                        print('\n' * 130)
                        interface.inicio()
        else:
            print('ERRO - - - Valor incorreto\n')
def queda_dados(lados_dado):
    return randint(1, lados_dado)