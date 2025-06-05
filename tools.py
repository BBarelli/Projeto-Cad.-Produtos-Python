import pyautogui
import time

# Pausa de 1s na transição de telas
pyautogui.PAUSE = 1

# Acesso ao chrome
pyautogui.press('win')
pyautogui.write('Chrome - Power up')
pyautogui.press('enter')

# Acessando o sitefariasbrito
pyautogui.write('http://tools.evolucional.com.br/configuracao/login')
pyautogui.press('enter')

# Fazendo Login
pyautogui.click(x=-954, y=544)
pyautogui.write('fariasbrito')
pyautogui.press('tab')
pyautogui.write('951817')
pyautogui.press('enter')

# Acessando relatórios
pyautogui.click(x=-1248, y=146)
pyautogui.press('enter')
pyautogui.click(x=-1318, y=292)
pyautogui.press('enter')
#pyautogui.click(x=-1351, y=372)
#pyautogui.press('enter')
