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

@app.get("/comercializacao/", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "Comercializacao"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    
@app.get("/exportacao/espumantes", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ExpEspumantes"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)

@app.get("/exportacao/suco", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ExpSuco"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    
@app.get("/exportacao/uva", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ExpUva"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    
@app.get("/exportacao/vinho", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ExpVinho"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    

@app.get("/importacao/espumantes", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ImpEspumantes"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    

@app.get("/importacao/uvas_frescas", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ImpFrescas"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)    

@app.get("/importacao/uvas_passas", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ImpPassas"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)    

@app.get("/importacao/suco", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ImpSuco"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)    

@app.get("/importacao/vinhos", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ImpVinhos"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)    

@app.get("/Processamento/americanas_hibridas", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ProcessaAmericanas"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    
@app.get("/Processamento/uvas_mesa", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ProcessaMesa"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    

@app.get("/Processamento/sem_classificacao", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ProcessaSemClass"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)
    

@app.get("/Processamento/viniferas", response_class=HTMLResponse)
def producao(ano='2023'):
    option = "ProcessaViniferas"
    ext = Extraction()
    try:
        return ext.request_site(option, ano)
    except:
        return ext.request_csv(option, ano)