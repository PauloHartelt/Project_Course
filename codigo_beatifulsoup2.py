# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwi_oLazyYiEAxX8uZUCHaCbAdIQ_AUoAXoECAIQAw'
requisicao = requests.get(url)

# Exemplo extraindo índices

if requisicao.status_code == 200:
    soup = BeautifulSoup(requisicao.text, 'html.parser')
    
    selecao = soup.find_all('div', class_='lkR3Y')

    # print(len(selecao))

    if selecao:

        valores = []

        for tags in selecao:

            valor = tags.find_all('div', class_='YMlKec')[0]

            # print(valor)
            
            if valor:
                 
                 valores.append(valor.text)

            else:
                print("Não foi possível encontrar a informação desejada.")

        print(valores)
                
    else: 
        print("Não foi possível encontrar a informação desejada.")
else:
    print(f'Erro ao acessar a página. Código de status: {requisicao.status_code}')