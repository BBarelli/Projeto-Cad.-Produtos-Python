import pyautogui
import time

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

'''
#Definir o tempo de transição entre as telas
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
time.sleep(2)




'''

Passo 3: Importar a base de dados
Passo 4: Cadastrar 1 Produto 
Passo 5: Repertir para todos os produtos

'''
