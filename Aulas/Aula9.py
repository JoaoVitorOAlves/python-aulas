# janela para selecionar a pasta do nosso computador
import os
from tkinter.filedialog import askdirectory

nome_pasta_selecionada = askdirectory()
print(nome_pasta_selecionada)

lista_arquivos = os.listdir(nome_pasta_selecionada)
print(lista_arquivos)
# fazer o backup dos arquivos que estão nessa pasta

