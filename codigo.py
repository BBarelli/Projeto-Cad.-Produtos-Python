import pyautogui
import time
import pandas as pd


# consulta ao gpt
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
pyautogui.write('Senha001')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

time.sleep(1)

# Passo 4: Cadastrar Todos os Produto

for linha in tabela.index:  # Para cada linha da minha tabela
    pyautogui.click(x=-921, y=263)

    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # Necessário tratar o valor int pra string (utilizando o str)
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    # Tratamento condicional pra que o campo desconsidere o 'NaN'
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    # subir o scroll ou descer
    pyautogui.scroll(10000)
