import defs

defs.limparTerminal()

while True:
    escolha = defs.menu()

    if escolha == '1':
        defs.cadastro()
    elif escolha == '2':
        defs.mostrarDados()
    elif escolha == '3':
        defs.clientesCadastrados()
    elif escolha == '4':
        defs.relatorio()
    elif escolha == '0':
        print('\033[1;36m''Volte sempre e até a proxima!''\033[0;0m')
        break
    else:
        defs.limparTerminal()
        defs.criarBarra()
        print('\033[1;31m''Insira uma opção válida!''\n033[0,0m')
        defs.criarBarra()


