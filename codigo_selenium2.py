## pip install selenium
## pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

url = 'https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwi_oLazyYiEAxX8uZUCHaCbAdIQ_AUoAXoECAIQAw'
response = navegador.get(url)

try:
    selecao = navegador.find_elements(By.CLASS_NAME, "lkR3Y")

    # print(len(selecao))

    if selecao:
        valores = [tags.find_elements(By.CLASS_NAME, "YMlKec")[0].text for tags in selecao]

        print(valores)
    else: 
        print("Não foi possível encontrar a informação desejada.")
        
except Exception as error:
    print(f'Ocorreu um erro: {error}')
    
# Fechar o navegador
navegador.quit()