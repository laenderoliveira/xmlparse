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