# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwi_oLazyYiEAxX8uZUCHaCbAdIQ_AUoAXoECAIQAw'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    valor = soup.find_all('div', class_='fxKbKc')

    if valor:
        print(valor[0].text)
    else:
        print("Valor não encontrado")
else:
    print(f'Erro ao acessar a página. Código de status: {response.status_code}')