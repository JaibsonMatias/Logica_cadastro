import valida
import datetime
import os


# função para limpar o terminal
def limparTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


# função para criar uma barra de traços
def criarBarra():
    return print('-' * 32)


data = datetime.datetime.now()  # atualição para pegar a data
dia = data.day
mes = data.month
ano = data.year


def menu():
    print('-------<<<< ''\033[1;96m''Idéias Sublimaticas''\033[0;0m'' >>>> -------')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Clientes     |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Clientes     |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Clientes Cadastrados     |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatótios     |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair     |"')
    print("-----------------------------------------")
    opcao = input('\033[1;36m''Insira a Opção desejada: ')
    return opcao

def cadastro():
    limparTerminal()
    print('------- < ''\033[1;92m''Cadastrar Usuário''\033[0,0m'' > -------')
    nome = valida.Nome()
    login = valida.Login()

    lerLogin = open('logins.txt', 'r')
    for linha in lerLogin.readlines():
        valores = linha.split('-')
        if login == valores[1].split('-')[1].strip():
            limparTerminal()
            criarBarra()
            print('\033[1;31m''Login já existente!''\033[0;0m')
            criarBarra()
            return
    lerLogin.close()

    senha = valida.Senha()
    email = valida.Email()
    data = valida.Data()
    fone = valida.Fone()
    ender = valida.ender()

    limparTerminal()
    criarBarra()
    print('\033[1;32m''Cliente casdastrado com sucesso!!''\033[0;0m')
    criarBarra()

    logins = open('Logins.txt', 'a')
    logins.write(
        f'Nome: {nome} -Login: {login} -Senha: {senha} -Email: {email} -Data: {data} -Telefone: {fone} -Endereço: {ender}')
    logins.close()
    return

def mostrarDados():
    limparTerminal()
    print('======= <<< ''\033[1;33m''Dados do Cliente''\033[0;0m')
    criarBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0;0m')
    criarBarra()
    userlogin = input('Login: ')
    usersenha = input('Senha: ')

    valida = False
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        if userlogin in valores[1] and usersenha in valores[2]:
            limparTerminal()
            criarBarra()
            print('\033[1;32m''Cliente logado! Dados do usuario: ''\033[0;0m')
            criarBarra()
            for percorre in range(len(valores)):
                if valores[percorre].split(':')[0] == 'Endereco':
                    dictEndereco = eval(valores[percorre].split('Endereco:')[1])
                    for chave in dictEndereco:
                        print(f'{chave}: {dictEndereco[chave]}')
                else:
                    print(valores[percorre])
            criarBarra()
            valida = True
            logins.close()
            break

    if not valida:
        limparTerminal()
        criarBarra()
        print('\033[1;31m''Erro! Login ou senha inválido(s)''\033[0;0m')
        criarBarra()

def clientesCadastrados():
    limparTerminal()
    print('======= Clientes Cadastrados =======')
    logins = open('logins.txt', 'r')
    for linha in logins.readlines():
        l = linha.split('-')
        print('\033[1;92m'f'{l[0]} | {[1]}''\033[0;0m')
    criarBarra()
    return

def relatorio():
    countCliente = 0
    nomess = []

    logins = open('logins.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0])
        countCliente += 1


    limparTerminal()
    arquivo = open("dados.txt", "w+")
    arquivo.write('Relatorios de Clientes \n')
    arquivo.write('\n')
    arquivo.write(f'A loja Ideias sublimadas possui {countCliente} cliente(s) \n')

    for i in range(len(nomess)):
        arquivo.write(str(f'{i +1}.{nomess[i].split(":")[1]} \n'))
    arquivo.write(f'São Paulo, {dia}/{mes}/{ano}.')
    criarBarra()
    print('\033[1;32m'"Relatório gerado em 'dados.txt'"'\033[0;0m')
    criarBarra()
    arquivo.close()
    return
