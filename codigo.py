# FAQ DO CÓDIGO:
'''
# Dica: Inicie deixandesclarecendo o que precisa ser feito.
# Entra no sistemas da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# import time  # Biblioteca para adiconar tempo na transição entre as telas (time.sleep(1))

 import pyautogui (permite controlar o mouse/teclado/tela do computador - usando python)

 pyautogui.click --> clique em algum lugar
 pyautogui.press --> aperta 1 tecla
 pyautogui.write --> escrever um texto
 pyautogui.hotkey --> apertar um combinação de teclas
 pyautogui.PAUSE --> definir uma configuração
 pyautogui.click(button = rigth) // pyautogui.click(clicks = 2) dual clicks 
 print(pyautogui.position()) --> descobrir a posição do mouse em um campo dá um time.sleep(5) e...-->pyautogui.position(x=1883, y=624)

'''

import pyautogui
import time
import pandas as pd

# Definir o tempo de transição entre as telas
pyautogui.PAUSE = 1

# Abri o chrome
pyautogui.press('win')

# Na área de trabalho → Novo → Atalho..."C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2" // Dê o nome "Chrome - Chrome - Power up"
# Execute o comando abaixo
pyautogui.write('Chrome - Power up')
pyautogui.press('enter')

# Digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Passo 2: Login
pyautogui.click(x=-948, y=380)
pyautogui.write('breno.barelli4@gmail.com')
pyautogui.press('tab')

# Senha
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

#Passo 4: Cadastrar 1 Produto 
time.sleep(4)
print(pyautogui.position())

'''
Passo 4: Cadastrar 1 Produto 
Passo 5: Repertir para todos os produtos

'''
