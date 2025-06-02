import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import datetime as dt
from log import Log

class Sistema:
    #Fazer uma função que receba o caminho do arquivo e retorne a mesma com as barras / invertidas para \.
    def ReceberDados():
        while True:
            try:
                caminho = input("Escreva o caminho do arquivo que será analisado: ")
                Log.AtualizarLog("Caminho de arquivo",caminho)
                caminho = caminho.replace("\\","/")
                caminho = caminho.replace('""',"")
                print()
                if "json" in caminho:
                    dados = pd.read_json(caminho)
                    break
                elif "csv" in caminho:
                    dados = pd.read_csv(caminho)
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Caminho incorreto ou arquivo em formato errado.")
            except ValueError:
                print("Caminho incorreto ou arquivo em formato errado.")
            except FileNotFoundError: 
                print("Arquivo não econtrado, tente novamente com um caminho correto.")
            except OSError:
                print("Arquivo não econtrado, tente novamente com um caminho correto.")
        return dados

    #Receber os dados e devolver a quantidade de dados carregados, quantidade de homens e mulheres, quantos registros sem dados sobre a educação dos pais.
    def PrintInformacoes(dados):
        print(f"Total de dados na planilha: {len(dados["Gender"])}")
        print(f"Total de homens: {dados["Gender"].value_counts().get("Male",0)}\nTotal de mulheres: {dados["Gender"].value_counts().get("Female",0)}")
        print(f"Dados sem algum tipo de registro: {(dados.isnull().any(axis=1).sum())}")


    #Receber os dados e remover os dados vazios, e modificando os dados vazios em attendance para a mediana da coluna, e apresentar o somatório de attendance.
    def RemoverDados(dados):
        dados["Attendance (%)"] = dados["Attendance (%)"].fillna((round(dados["Attendance (%)"].median())))
        print(f"\n\nSoma dos dados em Attendance é: {dados["Attendance (%)"].sum()}")
        dados.dropna(subset="Parent_Education_Level",inplace=True)
        print("\nDados nulos relativos à educação dos pais removidos e modificando os nulos em attendance para a mediana da coluna.")

    def MostrarDados(dados):
        print(f"\n\nSoma dos dados em Attendance é: {dados["Attendance (%)"].sum()}")
        print(f"\n\nDados sem algum tipo de registro: {(dados["Parent_Education_Level"].isnull().sum())}")

    #Receber os dados e devolver os dados de média, mediana, moda e desvio padrão de uma coluna dada por um usuário.
    def ConsultaColuna(dados):
        while True:
            try:
                entrada = input("Escolha a coluna a ser consultada: ")
                Log.AtualizarLog("Coluna consultada", entrada)
                if entrada in dados.columns:
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Sua entrada não coincide com nenhuma coluna.")
        
        tipo_dado = dados[entrada].dtypes
        if tipo_dado == "float64" or tipo_dado == "int64":
            return print(f"Moda: {round(dados[entrada].mode()[0])}\nMédia: {round(dados[entrada].mean())}\nMediana: {round(dados[entrada].median())}\nDesvio padrao: {round(dados[entrada].std())}")
        elif tipo_dado == "object":
            return print(f"Moda: {dados[entrada].mode()[0]}")

    #Receber os dados e produzir gráfico de dispersão para “horas de sono” x “nota final”.
    def GraficoDispersao(dados):
        while True:
            try:
                entrada_porcentagem = int(input("Porcentagem da amostra dos dados para o gráfico: "))
                if entrada_porcentagem > 100  or entrada_porcentagem < 0:
                    raise ValueError
                Log.AtualizarLog("Porcentagem amostral grafico de dispersao", entrada_porcentagem)
                break
            except ValueError:
                print("Valor digitado incorreto, tente novamente.")
        dados_sample = dados.sample(n=int(len(dados)*(entrada_porcentagem/100)),random_state=42)
        plt.scatter(dados_sample["Sleep_Hours_per_Night"], dados_sample["Final_Score"])
        plt.xlabel("Horas Dormidas")
        plt.ylabel("Nota Final")
        plt.title("Gráfico de Dispersão")
        plt.show()

    #Receber os dados e produzir gráfico de barras – idade x média das notas intermediárias (midterm_Score).
    def GraficoBarras(dados):
        while True:
            try:
                entrada_porcentagem = int(input("Porcentagem da amostra dos dados para o gráfico: "))
                if entrada_porcentagem > 100  or entrada_porcentagem < 0:
                    raise ValueError
                Log.AtualizarLog("Porcentagem amostral grafico de barras", entrada_porcentagem)
                break
            except ValueError:
                print("Valor digitado incorreto, tente novamente.")
        dados_sample = dados.sample(n=int(len(dados)*(entrada_porcentagem/1000)),random_state=42)
        categorias = [pessoa for pessoa in dados_sample["First_Name"]]
        valores1 = [nota for nota in dados_sample["Age"]]
        valores2 = [nota for nota in dados_sample["Midterm_Score"]]

        x = np.arange(len(categorias)) 
        largura = 0.35

        fig, ax = plt.subplots()
        idade = ax.bar(x - largura/2, valores1, largura, label='Idade')
        nota_mid = ax.bar(x + largura/2, valores2, largura, label='Nota Intermediária')

        ax.set_ylabel('Valores')
        ax.set_xlabel('Categorias')
        ax.set_xticks(x)
        ax.set_xticklabels(categorias)
        ax.legend()

        fig.tight_layout()
        plt.show()

    #Receber os dados e produzir gráfico de pizza para as idades (Agrupadas: até 17; 18 a 21; 21 a 24; 25 ou mais).
    def GraficoPizza(dados):
        dados = dados["Age"]
        dezessete = 0
        dezoito_vinteum = 0
        vinteum_vintequatro = 0
        vintecinco = 0
        for idade in dados:
            if idade < 17:
                dezessete += 1
            elif idade >= 17 and idade < 21:
                dezoito_vinteum += 1
            elif idade >= 21 and idade <= 24:
                vinteum_vintequatro += 1
            elif idade >= 25:
                vintecinco +1

        valores = [dezessete,dezoito_vinteum,vinteum_vintequatro, vintecinco]
        nomes = ["<17","18 a 21","21 a 24", "25>"]
        cores= ["gold", "yellowgreen", "lightcoral", "lightskyblue"]
        plt.pie(valores, labels=nomes, colors=cores)
        plt.title('Distribuição de Idades')
        plt.show()

    def DataHora():
        agora = dt.datetime.now()
        hora = agora.hour
        min = agora.minute
        mes = agora.month
        dia = agora.day
        ano = agora.year
        return f"{hora}:{min}  {dia}/{mes}/{ano}"