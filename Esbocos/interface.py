import dados
def inicio ():
    print('---------------D&D---------------\n')
    escolhainterfaceinicial = int(input('DADOS (1)\nSAIR (2)\n\nESCOLHA SUA OPÇÃO: '))
    match escolhainterfaceinicial:
        case 1:
            print('\n' * 130)
            dados.escolha_de_dados()
        case 2:
            exit()
if __name__ == "__main__":
    inicio()