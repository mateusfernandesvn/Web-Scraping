import requests
from bs4 import BeautifulSoup

url = "https://www.mercadolivre.com.br/novo-echo-show-8-3-geraco-branco/p/MLB44776325#polycard_client=search-nordic&searchVariation=MLB44776325&wid=MLB5237588346&position=6&search_layout=grid&type=product&tracking_id=47b0b92b-4a02-475f-9f75-11913262203f&sid=search"

headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

try:
    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        print(f"Conexão estabelecida com sucesso!  Código de status: {req.status_code}")
        site = BeautifulSoup(req.text, 'html.parser')

        title = site.find("h1", class_="ui-pdp-title")
        title = title.text.strip() if title else "Título não encontrado"

        price = site.find("span", class_="andes-money-amount__fraction")
        price = price.text.strip() if price else "Preço não encontrado"

        print(f"Título: {title}")
        print(f"Preço: R${price}")
    else:
        print(f"Erro ao acessar a página. Código de status: {req.status_code}")

    
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a página: {e}")
