import requests
import schedule
import time
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("URL_PRODUTO")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

def main():
    try:
        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            print(f"✅ Conexão estabelecida! Código de status: {req.status_code}")
            site = BeautifulSoup(req.text, 'html.parser')

            title = site.find("h1", class_="ui-pdp-title")
            title = title.text.strip() if title else "Título não encontrado"

            price = site.find("span", class_="andes-money-amount__fraction")
            price = price.text.strip() if price else "Preço não encontrado"
            
            hours = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            nome_arquivo = "Dados.csv"

            with open(nome_arquivo, mode="a", newline="", encoding="utf-8") as arquivo_csv:
                writer = csv.writer(arquivo_csv)

                if arquivo_csv.tell() == 0:
                    writer.writerow(["Data/Hora", "Título", "Preço"])

                writer.writerow([hours, title, f"R${price}"])

            print(f"📂 Dados salvos em '{nome_arquivo}' com sucesso!")

        else:
            print(f"❌ Erro ao acessar a página. Código de status: {req.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a página: {e}")

schedule.every().hours.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)