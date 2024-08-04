import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# Passo 1 - Entrar no sistema

pyautogui.press ('win')
pyautogui.write ('edge')
pyautogui.press ('enter')

time.sleep(0.5)

pyautogui.write ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press ('enter')
pyautogui.press ('f11')

time.sleep(1)

# Passo 2 - Login

pyautogui.click(x=807,y=284)
pyautogui.write('davi@gmail.com')
pyautogui.click(x=1235, y=388)
pyautogui.write('senha123')
pyautogui.press('enter')

time.sleep(1)

# Passo 3 - Importar banco de dados
tabela = pd.read_csv("produtos.csv")
print (tabela)
print (tabela['codigo'])

# Passo 4 - Cadastrar produtos

for linha in tabela.index:
    pyautogui.click(x=1225, y=171)
    pyautogui.write(str(tabela.loc[linha]['codigo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha]['marca']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha]['tipo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha]['categoria']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha]['preco_unitario']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha]['custo']))

    pyautogui.press('tab')
    obs = str(tabela.loc[linha]['obs'])
    if  obs != 'nan':
        pyautogui.write(obs)
    

    pyautogui.press('tab')
    pyautogui.press('enter')