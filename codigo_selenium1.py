## pip install selenium
## pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

url = 'https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwi_oLazyYiEAxX8uZUCHaCbAdIQ_AUoAXoECAIQAw'

try:
    response = navegador.get(url)
    
    valor = navegador.find_elements(By.CLASS_NAME, "fxKbKc")

    if valor:
        print(valor[0].text)
    else:
        print("Valor não encontrado")

except Exception as error:
    print(f'Ocorreu um erro: {error}')
    
navegador.quit()