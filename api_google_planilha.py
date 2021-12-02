import gspread
from google.oauth2 import service_account
import pandas as pd

scopes = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

json_file = "credentials.json"
nome_pla = "user"
nome_aba = "data"

def login():
    credentials = service_account.Credentials.from_service_account_file(json_file)
    scoped_credentials = credentials.with_scopes(scopes)
    gc = gspread.authorize(scoped_credentials)
    return gc



def leitor():
    gc = login()
    planilha = gc.open(nome_pla)
    aba = planilha.worksheet(nome_aba)
    dados = aba.get_all_records()
    df = pd.DataFrame(dados)
    return dados


def escritor(lista):
    gc = login()
    planilha = gc.open(nome_pla)
    planilha = planilha.worksheet(nome_aba)
    planilha.append_row(lista, value_input_option='USER_ENTERED')



escreve = ["testeescrita@gmail", "sdlfkals"]

escritor(escreve)

teste = leitor()

print(str(teste))
