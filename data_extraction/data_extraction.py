from bs4 import BeautifulSoup
import requests
import polars as pl
import json, os

class Extraction:
    three_columns = [
        "exp_espumantes",
        "exp_suco",
        "exp_uva",
        "exp_vinho",
        "imp_espumantes",
        "imp_uvas_frescas",
        "imp_uvas_passas",
        "imp_suco",
        "imp_vinho"
    ]

    def __init__(self):
        self.url_default = "http://vitibrasil.cnpuv.embrapa.br/index.php?"

    def open_files(self, path): 
        base_dir = os.path.dirname(__file__)
        full_path = os.path.join(base_dir, path)
        with open(full_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_url(self, option, ano):
        options_url = self.open_files("urls.json")
        
        for keys, values in options_url.items():
            if isinstance(values, list):
                for item in values:
                    if option in item:
                        return "{}ano={}&{}".format(self.url_default, ano, item[option])
            elif keys == option:
                return "{}ano={}&{}".format(self.url_default, ano, values)

    def request_csv(self, option, ano, columns):
        df = pl.read_csv(f"./data_extraction/data/{option}.csv", separator=";", encoding="utf8")

        if option in self.three_columns:
            df = df.rename({ano: columns[1], f"{ano}.1": columns[2]})
        else:
            df = df.rename({ano: columns[1]})
        
        return df.select(columns).to_pandas().to_html(index=False)

    
    def request_site(self, option, ano):
        url = self.get_url(option, ano)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            tables = soup.find_all('table', "tb_base tb_dados")

            if tables:
                for i, table in enumerate(tables):
                    rows = table.find_all('tr')
                    if rows:
                        headers = [th.text.strip() for th in rows[0].find_all('th')]
                        data = []
                        for row in rows[1:]:
                            cells = [td.text.strip() for td in row.find_all('td')]
                            data.append(cells)
                        if headers and data:
                            df = pl.DataFrame(data, schema=headers)
                        elif data:
                            df = pl.DataFrame(data)
                return df.to_pandas().to_html(index=False)