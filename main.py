from bs4 import BeautifulSoup as bs
from requests import get

# Super Lima LTDA-ME
BASE = "https://nfstock.alterdata.com.br"


def get_xml(keynfe):
    response = get(f"{BASE}/Consulta/laender/Consulta/Buscar?chave={keynfe}")
    soup = bs(response.text, "html.parser")
    href = soup.find("a").attrs["href"]
    response = get(f"{BASE}{href}")
    return response.text


def parse_xml(xmlnfe):
    clear = ["pRedBC", "vBC", "pICMS", "vICMS"]  # Fields to clear
    soup = bs(xmlnfe, "xml")
    for tag in clear:
        for value in soup.findAll(tag):
            value.string = "0"
    return str(soup.nfeProc)