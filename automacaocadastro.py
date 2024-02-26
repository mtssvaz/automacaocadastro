from selenium import webdriver
from selenium.webdriver.common.by import By

# Instanciar o driver do Firefox
firefox = webdriver.Firefox()

# Abrir o site do Google
firefox.get('http://www.google.com')

# Maximizar a janela do navegador
firefox.maximize_window()

# Localizar o elemento da caixa de pesquisa e enviar as chaves de busca
search_box = firefox.find_element(By.NAME, "q")
search_box.send_keys("teste de busca")
