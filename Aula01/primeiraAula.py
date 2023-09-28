import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.3


# Abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.click(x=1244, y=617)


# entar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# esperar o site carregar
time.sleep(2)




#passo 2 fazer o login
pyautogui.click(x=471, y=369)
pyautogui.write('chrome@gmail.com')
pyautogui.press('tab')
pyautogui.write('senhaChrome')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)


#importar a base de dados


tabela = pandas.read_csv("produtos.csv")
print(tabela)



for linha in tabela.index:

    #cadastrar 1 produto

    pyautogui.click(x=466, y=256)

    # preencher os campos


    codigo = tabela.loc[linha, 'codigo']
    

    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str())

    pyautogui.press('tab')
    pyautogui.press('enter')


    pyautogui.scroll(50000)

