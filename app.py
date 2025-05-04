from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from data_extraction.data_extraction import Extraction


app = FastAPI()

@app.get("/producao/", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "Producao"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
