from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time, json
import requests
from bs4 import BeautifulSoup
import os

# Inicializar o navegador
browser = webdriver.Edge()

def extract_urls(data):
    urls = []
    for value in data.values():
        if isinstance(value, list):
            urls.extend(value)  # Adiciona todas as URLs da lista
        elif isinstance(value, str):
            urls.append(value)  # Adiciona a URL única
    return urls

def urls():
    with open("./data_extraction/urls.json", "r") as file:
        return extract_urls(json.load(file))


def requests_download(url):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Procurar links para arquivos CSV na página
        csv_links = soup.find_all("a", href=True)
        for link in csv_links:
            if link['href'].endswith(".csv"):
                csv_url = link['href']
                # Se o link for relativo, adicionar a URL base
                if not csv_url.startswith("http"):
                    csv_url = url + csv_url

                # Fazer download do arquivo CSV
                csv_response = requests.get(csv_url)
                if csv_response.status_code == 200:
                    file_name = os.path.join("C:\\Users\\Overthrive\\Documents\\faculdade_ml\\tech_chalenge\\project\data_extraction\data", csv_url.split("/")[-1])
                    with open(file_name, "wb") as file:
                        file.write(csv_response.content)
                    print(f"Arquivo {file_name} baixado com sucesso.")
                else:
                    print(f"Erro ao baixar o arquivo {csv_url}.")
    else:
        print("Não foi possível acessar o site.")

    print("Processo concluído.")


