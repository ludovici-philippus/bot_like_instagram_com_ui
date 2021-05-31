import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import tkinter.ttk
from tkinter import *
from functools import partial

# Variáveis
TELA = "380x150"
driver = webdriver.Firefox()
perfis = []

# Funções
def enviar():
    driver.get("https://www.instagram.com")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
    if facebook.get():
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[5]/button/span[2]')))
        elem = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]')
        elem.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
        elem = driver.find_element_by_xpath('//*[@id="email"]')
        elem.clear()
        elem.send_keys(entry_email.get())

        elem = driver.find_element_by_xpath('//*[@id="pass"]')
        elem.clear()
        elem.send_keys(entry_senha.get())

        elem = driver.find_element_by_xpath('//*[@id="loginbutton"]')
        elem.click()

        wait.until(EC.visibility_of_element_located('/html/body/div[4]/div/div/div/div[3]/button[2]'))
        elem = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        elem.click()
        entrar_no_perfil()

    elem = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    elem.clear()
    elem.send_keys(entry_email.get())

    elem = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    elem.clear()
    elem.send_keys(entry_senha.get())

    elem = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    elem.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
    elem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    elem.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div')))
    elem = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    elem.click()
    entrar_no_perfil()


def entrar_no_perfil():
    driver.get(f"https://www.instagram.com/{entry_link.get()}/")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')))
    elem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
    elem.click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/ul/div/li/div/div[2]/div/div/div/span/a')))
    for item in driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li/div/div[2]/div/div/div/span/a'):
        perfis.append(item.text)
    
    for perfil in perfis:
        driver.get(f"https://www.instagram.com/{perfil}/")
        try:
            print("Entrou")
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/main/div/div/article/div/div/div/div')))
            elem = driver.find_element_by_xpath('/html/body/div/section/main/div/div/article/div/div/div/div')
            elem.click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div')))
            elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div')
            elem.click()
            print("Saiu")
        except:
            continue
    popup = Toplevel()
    Label(popup, font=72, text="Programa encerrado!").pack()
    janela.after(5000, lambda: janela.destroy())
    driver.close()


# Programa-em-si
janela = Tk()
link_do_perfil = StringVar()
e_mail = StringVar()
senha = StringVar()
facebook = BooleanVar()


lb_link = Label(janela, text="Digite o perfil do Instagram")
lb_link.place(x=0, y=0)

lb_email = Label(janela, text="Digite o email/telefone/nome de usuário")
lb_email.place(x=0, y=25)

lb_senha = Label(janela, text="Digite a sua senha")
lb_senha.place(x=0, y=50)

entry_link = Entry(janela, width="20", textvariable=link_do_perfil)
entry_link.place(x=250, y=0)

entry_email = Entry(janela, width="20", textvariable=e_mail)
entry_email.place(x=250, y=25)

entry_senha = Entry(janela, width="20", textvariable=senha)
entry_senha.place(x=250, y=50)

rbt_facebook = Checkbutton(janela, text="Logar com Facebook", variable=facebook)
rbt_facebook.place(x=0, y=100)

bt_enviar = Button(janela, width="16", text="Enviar", command=enviar)
bt_enviar.place(x=250, y=100)


janela.geometry(TELA)
janela.title("Automatizar Likes no Instagram")
janela.resizable(False, False)
janela.mainloop()