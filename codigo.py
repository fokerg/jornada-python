# Acessar a url https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.click -> escrever um texto
# pyautogui.click -> apertar 1 tecla
# pyautogui.click -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Fazer login
pyautogui.click(x=397, y=396)
pyautogui.write("fokerg@gmail.com")

pyautogui.press("tab") # para passar para o campo senha
pyautogui.write("123456")

pyautogui.press("tab") # passei para o botão
pyautogui.press("enter")

# Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 
    # Cadastrar 1 produto
    pyautogui.click(x=438, y=279)

    # preencher os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # apertar para enviar

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)
# Repetir o cadastro para todos os produtos