import pyautogui
import time  # Biblioteca para colocaadiconar tempo na transição entre as telas

# import pyautogui (permite controlar o mouse/teclado/tela do computador - usando python)
# pyautogui.click --> clique em algum lugar
# pyautogui.press --> aperta 1 tecla
# pyautogui.write --> escrever um texto
# pyautogui.hotkey --> apertar um combinação de teclas

'''
Dica: Inicie deixandesclarecendo o que precisa ser feito.

Passo 1: Entra no sistemas da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login'''
# Abri o chrome
pyautogui.press('win')
# Na área de trabalho → Novo → Atalho..."C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2" // Dê o nome "Chrome - Chrome - Power up"
# Execute o comando abaixo
pyautogui.write('Chrome - Power up')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'l')
time.sleep(2)
# Digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

'''
Passo 2: Login
Passo 3: Importar a base de dados
Passo 4: Cadastrar 1 Produto 
Passo 5: Repertir para todos os produtos
'''
