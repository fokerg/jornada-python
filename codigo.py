# Acessar a url https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.click -> escrever um texto
# pyautogui.click -> apertar 1 tecla
# pyautogui.click -> atalho (combinação de teclas)

pyautogui.PAUSE = 2

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Fazer login
pyautogui.click(x=397, y=396)
pyautogui.write("fokerg@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

# Importar a base de dados de produtos
# Cadastrar 1 produto
# Repetir o cadastro para todos os produtos