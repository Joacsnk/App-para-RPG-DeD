import dados
def inicio ():
    print('---------------D&D---------------\n')
    escolhainterfaceinicial = int(input('DADOS (1)\n\nESCOLHA SUA OPÇÃO: '))
    match escolhainterfaceinicial:
        case 1:
            dados.escolha_de_dados()
if __name__ == "__main__":
    inicio()