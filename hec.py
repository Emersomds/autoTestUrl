import requests

url = "http://127.0.0.1:8000"

lista_de_arquivos = open('lista-de-arquivos-comuns.txt')

for linha in lista_de_arquivos.readlines():
    url_teste = url + "/" + linha.replace("\n","")
    print(url_teste)
    requisicao = requests.get(url_teste)
    if(requisicao.status_code == 200):
        print("[+] Deretório ou arquivo encontrado: ", linha.replace("\n",""))
    else:
        print("[X] Diretório ou arquivo não encontrado (" + str(requisicao.status_code) + "):", linha.replace("\n",""))   
