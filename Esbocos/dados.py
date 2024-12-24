def escolha_de_dados():
    import interface
    tipo_de_dado = int(input('\nD4 (1)\nD6 (2)\nD8 (3)\nD10 (4)\nD20 (5)\nD100 (6)\nSAIR (7)\n\nESCOLHA O TIPO DO DADO: '))
    match tipo_de_dado:
        case 7:
            interface.inicio()