from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

# SISTEMA PRINCIPAL -------------------------------------------------------------------------------------
arquivo_ = 'CursoemVideo.txt'
if not arquivo_existe(arquivo_):
    criar_arquivo(arquivo_)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar uma Pessoa', 'Sair do Sistema'] )

    if resposta < 1 or resposta > 3:
            print(c[1] + 'ERRO: Digite uma opção válida' + c[0])

    elif resposta == 1:
        # Opção de listar e exibir as pessoas cadastradas
        ler_arquivo(arquivo_)
        sleep(1)

    elif resposta == 2:
        cabecalho('2 - NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade:')
        novo_cadastro(arquivo_, nome, idade)
        sleep(1)

    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        sleep(1)
        break



