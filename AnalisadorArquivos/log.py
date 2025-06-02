import os

class Log:
    primeiro = True
    #Atualizar o Log
    def AtualizarLog(oq_entrou, entrada):
        arquivo_existe = os.path.exists("./data/Log.csv")

        try:
            with open("./data/Log.csv", "a") as data:
                if not arquivo_existe:
                    data.write(f"Oque,Entrada\n{oq_entrou},{entrada}\n")
                else:
                    data.write(f"{oq_entrou},{entrada}\n")
            Log.primeiro = False 
        except FileNotFoundError:
            pass

    #Finalizar Log
    def FinalizarLog():
        try:
            with open("./data/Log.csv", "a") as data:
                data.write("\n")
        except FileNotFoundError:
            pass