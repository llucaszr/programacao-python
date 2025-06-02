from log import Log
from sistema import Sistema

print("======== Bem vindo ao analisador de arquivos ========\n\nEscreva abaixo o seu nome.")
nome = input("Nome: ")
Log.AtualizarLog("nome", nome)
agora = Sistema.DataHora()
Log.AtualizarLog("Comecou",agora)
data = Sistema.ReceberDados()
while True:
    print("\n\n======== Escolha uma opção ========\n\n[ 1 ] - Informações gerais do arquivo.\n[ 2 ] - Remover dados vazios do arquivo, e substituir os nulos de attendance pela sua média.\n[ 3 ] - Mostrar soma dos Dados em Attendance e dados em algum tipo de registro.\n[ 4 ] - Consultar dados estatísticos de uma coluna.\n[ 5 ] - Gráfico de dispersão.\n[ 6 ] - Gráfico de barras.\n[ 7 ] - Gráfico em pizza.\n[ 8 ] - Sair.\n")
    while True:
        try:
            entrada = int(input("Digite Aqui: "))
            Log.AtualizarLog("Menu",entrada)
            if type(entrada) != int or entrada > 8 or entrada < 1:
                raise TypeError
            else:
                break
        except TypeError:
            print("Digite os dados corretamente.")
        except ValueError:
            print("Digite os dados corretamente.")
    print("\n\n")
    if entrada == 1:
        Sistema.PrintInformacoes(data)
    elif entrada == 2:
        Sistema.RemoverDados(data)
    elif entrada == 3:
        Sistema.MostrarDados(data)
    elif entrada == 4:
        Sistema.ConsultaColuna(data)
    elif entrada == 5:
        Sistema.GraficoDispersao(data)
    elif entrada == 6:
        Sistema.GraficoBarras(data)
    elif entrada == 7:
        Sistema.GraficoPizza(data)
    elif entrada == 8:
        print("Programa encerrado com sucesso.\n======== Obrigado por ter usado nosso sistema! ========")
        agora = Sistema.DataHora()
        Log.AtualizarLog("Acabou",agora)
        Log.FinalizarLog()
        break