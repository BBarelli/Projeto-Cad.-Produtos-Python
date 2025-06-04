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

pd.set_option('display.max_columns', None)  # mostra todas as colunas
pd.set_option('display.expand_frame_repr', False)  # impede quebra de linha


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
pyautogui.write('testando@gmail.com')
pyautogui.press('tab')

# Senha
pyautogui.write('1234567')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 Produto
time.sleep(4)
pyautogui.click(x=-921, y=263)

codigo = 'MOLO000251'
pyautogui.write(codigo)
pyautogui.press('tab')

marca = 'Logitech'
pyautogui.write(marca)
pyautogui.press('tab')

tipo = 'Logitech'
pyautogui.write(tipo)
pyautogui.press('tab')

categoria = '1'
pyautogui.write(categoria)
pyautogui.press('tab')

preco_unitario = '25.95'
pyautogui.write(preco_unitario)
pyautogui.press('tab')

custo = '6.5'
pyautogui.write(custo)
pyautogui.press('tab')

obs = ''
pyautogui.write(obs)
pyautogui.press('tab')
# Texto vazio em obs
'''
Passo 4: Cadastrar 1 Produto 
Passo 5: Repertir para todos os produtos

'''
