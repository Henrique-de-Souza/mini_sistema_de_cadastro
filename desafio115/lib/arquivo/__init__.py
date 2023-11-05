from desafio115.lib.interface import *
from time import sleep

# FUNÇÃO ABRIR UM ARQUIVO -------------------------------------------------------------------------------------
def arquivo_existe(nome):
    try:
        tente = open(nome, 'rt')
        tente.close()
    except FileNotFoundError:
        return False
    else:
        return True


# FUNÇÃO PARA CRIAR UM ARQUIVO TXT ---------------------------------------------------------------------------
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# FUNÇÃO PARA LER O ARQUIVO --------------------------------------------------------------------------------
def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um problema ao ler o arquivo')
    else:
        cabecalho('1 - VER PESSOAS CADASTRADAS')
        print(f'{"NOME:":<30}{"IDADE:":>7}')
        sleep(1)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


# FUNÇÃO PARA PERMITIR UM NOVO CADASTRO -------------------------------------------------------------------
def novo_cadastro(arquivo_, nome, idade):
    try:
        a = open(arquivo_, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    try:
        a.write(f'{nome};{idade}\n')
    except:
        print('Houve um ERRO na hora de escrever os dados')
    else:
        print(f"Novo regristo de {nome} adicionado.")
        a.close()
