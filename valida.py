def Nome():
    while True:
        nome = input("Nome Completo: ")
        if nome == '':
            print("Error! Entrada invalida! ")
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print("Digite um nome valido")
                break
        else:
            return nome.strip(' ')

def Senha():
    while True:
       senha = input('Senha: ')
       if senha == '':
            print("Error! Entrada vazia! ")
            continue
       return senha.strip(' ')

def Email():
    email = input('Email: ')
    if email == '':
        print('Error! Entrada vazia.: ')
    elif '@' and '.com' in email:
        return email.strip(' ')
    else:
        print('Email Inválido! Deve conter "@"e ".com" ')

def Data():
    data = input('Nascimento (dd/mm/aaaa): ')
    if data == '':
        print('Error! Entrada inválida')


    temp = ''.join(data.split('/'))
    if not temp.isnumeric():
        print('Insira uma data válida')


    if data.count('/') == 2 and data != '//':
        dia, mes, ano = data.split('/')
        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
            return data.strip(' ')
        else:
            print('Dia/Mes/Ano Inválido(s)! ')
    else:
        print('A data deve seguir o padrão de dd/mm/aaaa')
        return


def Login():
    login = input("Login: ")
    if login == '':
        print("Error! Entrada inválida.")

    return login.strip(' ')

def Fone():
    while True:
        tele = input("Telefone (Apenas Números): ")
        if tele == '':
            print('Error! Entrada Inválida. ')
            continue
        elif not tele.isnumeric():
            print('Insira apenas números.')
            continue
        else:
            if 9 <= len(tele) <= 11:
                return tele
            else:
                print('O número deve ter entre 9 - 11 carcteres.')

def ender():
    while True:
        print('==== <''\033[1;32m''Seu endereço Completo!''\033[0;0m')
        dados = {
            'Rua': input('Rua: '),
            'Numero': input('Numero: '),
            'Complemento': input('Complemento: '),
            'Bairro': input('Bairro: '),
            'CEP': input('CEP: '),
            'Cidade': input('Cidade: '),
            'Referencia': input('Rferencia: '),
        }
        return dados





