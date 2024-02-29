import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Defina o nome do arquivo e a URL do formulário
nomedoarquivo = "teste.xlsx"
urldoforms ="https://docs.google.com/forms/d/e/1FAIpQLSdZ32pJyCQ08E3Ajvp8E_Zy8xo6cN3rswKb-ROIe9ywwH56ow/viewform?usp=sf_link"

# Leia o arquivo Excel
df = pd.read_excel(nomedoarquivo)

# Inicie o loop para cada linha do arquivo Excel
for index, row in df.iterrows():
    print("index: " + str(index) + " E o nome do fulano é " + row["NOME"])
    
    # Inicie o driver do Chrome
    chrome = webdriver.Chrome(executable_path='chromedriver.exe')
    chrome.get(urldoforms)

    time.sleep(3)

    # Encontre os elementos pelo XPath e insira os valores
    elemento_texto_nome = chrome.find_element(By.XPATH, '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/input')
    elemento_texto_telefone = chrome.find_element(By.XPATH, '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div[11]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div/div[2]/input')

    elemento_texto_nome.send_keys(row["NOME"])
    elemento_texto_telefone.send_keys(row["TELEFONE"])

    # Feche o navegador
    chrome.quit()
