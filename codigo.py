import pyautogui
import time

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
time.sleep(2)

# Passo 2: Login
pyautogui.click()
time.sleep(5)
print(pyautogui.position(x=1883, y=624))
pyautogui.press('enter')


'''

Passo 3: Importar a base de dados
Passo 4: Cadastrar 1 Produto 
Passo 5: Repertir para todos os produtos

'''
