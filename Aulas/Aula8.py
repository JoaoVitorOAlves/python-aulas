import os
# import datetime
# import pyautogui


# pyautogui.press("win")
# print(os.listdir("aquivos"))
# print(datetime.date.today())

lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")
            print("movimentar para a pasta 22", arquivo)
        elif "23" in arquivo:
            print("Movimentar para a pasta 23", arquivo)
           