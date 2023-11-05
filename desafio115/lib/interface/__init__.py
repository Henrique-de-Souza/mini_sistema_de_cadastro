from time import sleep

c = (
    '\033[m',            #0 sem cor
    '\033[1;31m',        #1 vermelho
    '\033[1;42m',        #2 verde
    '\033[1;43m',        #3 amarelo
    '\033[1;44m',        #4 azul
    '\033[1;45m',        #5 roxo
    '\033[7;40m'         #6 branco
)

# FUNÇÃO QUE PERMITE APENAS LER UM NÚMERO INTEIRO ----------------------------------------------------------------------
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(c[1]+'ERRO: Digite um número inteiro válido!'+c[0])
            continue
        except KeyboardInterrupt:
            print(c[1]+'O usuário preferiu não informar um número'+c[0])
            return 0
        else:
            return n

# FUNÇÃO DE ESTILIZAÇÃO DDE LINHAS -------------------------------------------------------------------------------------
def linha(tamanho=42):
    return '='* tamanho


# FUNÇÃO DE ESTILIZAÇÃO DE UM CABEÇALHO --------------------------------------------------------------------------------
def cabecalho(text):
    print(linha())
    print(text.center(42))
    print(linha())


# FUNÇÃO DE ESTILIZAÇÃO DO MENU ----------------------------------------------------------------------------------------
def menu(lista):
    cabecalho('\033[35mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m ')
    return opc
